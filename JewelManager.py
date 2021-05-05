#===========================================#
#               Jewel Manager               #
#===========================================#
#                                           #
#   Author: CookieLover                     #
#   Release Date: 12/24/2017                #
#                                           #
#===========================================#
#                                           #
#   Info:                                   #
#   - target a container to scan its        #
#     contents and show jewelry props;      #
#   - use get to place the item in your     #
#     backpack;                             #
#   - use prev/next to switch page.         #
#                                           #
#===========================================#

import clr

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Collections.Generic import List
from System.Drawing import Point, Color, Size, ContentAlignment
from System.Windows.Forms import (Application, Button, Form,
    Label, FlatStyle, ListView, ListViewItem, View, UserControl)

class Monile(UserControl):
    strName = None
    Caller = None
    lstProps = []
    intSerial = 0
    intCount = 0
    intPage = 0
    
    def __init__(self, props, serial, caller, count, point):
        self.Name = 'Monile{0}'.format(count)
        self.strName = props[0]
        self.lstProps = props[1:]
        self.intSerial = serial
        self.Caller = caller
        self.intCount = count
        self.ControlSetup()
        self.Location = point

    def ControlSetup(self):
        # lblName
        lbl = Label()
        lbl.Location = Point(0,0)
        lbl.Name = 'lblName{0}'.format(self.intCount)
        lbl.Size = Size(160,23)
        lbl.Text = self.strName
        lbl.TextAlign = ContentAlignment.MiddleCenter
        # lwProps
        lw = ListView()
        lw.Location = Point(0,28)
        lw.BackColor = Color.FromArgb(35,35,35)
        lw.ForeColor = Color.FromArgb(231,231,231)
        lw.Name = 'lwProps{0}'.format(self.intCount)
        lw.ShowGroups = False
        lw.Size = Size(160,115)
        lw.View = View.SmallIcon
        lw.Items.Clear()
        for p in self.lstProps:
            lw.Items.Add(ListViewItem(p))
        # btnGet
        btn = Button()
        btn.Location = Point(55, 150)
        btn.Name = 'btnGet{0}'.format(self.intCount)
        btn.Size = Size(50,30)
        btn.FlatStyle = FlatStyle.Flat
        btn.FlatAppearance.BorderSize = 1
        btn.Text = 'Get'
        btn.Click += self.btnGetPressed
        # Monile
        self.Size = Size(160,180)
        self.Controls.Add(btn)
        self.Controls.Add(lw)
        self.Controls.Add(lbl)

    def btnGetPressed(self, sender, args):
        Items.Move(self.intSerial, Player.Backpack, 0)
        self.Caller.RemoveJewel(self.intCount)

class JewelManager(Form):
    Chest = None
    CurPage = 0
    CurVer = '1.0.0'
    Jewelry = [
        0x108A,0x1F09,0x1F08,0x1F06,
        0x1086,0x4211,0x4210,0x4212,
        0x1087,0x4213,0x1088,0x1089,
        0x1F05    
        ]
    Pages = []
    Points = []
    
    def __init__(self, targ):
        self.Chest = Items.FindBySerial(targ)
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(710, 665)
        self.Text = 'JewelManager - v{0}'.format(self.CurVer)

        self.ItemsSetup()
        self.ShowItems()
        if len(self.Pages) > 1:
            self.PagesBtnSetup()

    def propLister(self, item):
        nop = [
            'durability', 'weight', 'lower ammo cost',
            'strength requirement', 'lower requirements',
            'artifact rarity', 'crafted', 'exceptional',
            'insured'
        ]
        Items.WaitForProps(item, 5000)
        return [i for i in Items.GetPropStringList(item) if not any(n for n in nop if n in i.lower())]
    
    def PagesBtnSetup(self):
        btnPrev = Button()
        btnPrev.Location = Point(285, 585)
        btnPrev.Name = 'btnPrev'
        btnPrev.Size = Size(50,30)
        btnPrev.Text = 'Prev'
        btnPrev.FlatStyle = FlatStyle.Flat
        btnPrev.FlatAppearance.BorderSize = 1
        btnPrev.Click += self.PrevPagePressed
        
        btnNext = Button()
        btnNext.Location = Point(355, 585)
        btnNext.Name = 'btnNext'
        btnNext.Size = Size(50,30)
        btnNext.Text = 'Next'
        btnNext.FlatStyle = FlatStyle.Flat
        btnNext.FlatAppearance.BorderSize = 1
        btnNext.Click += self.NextPagePressed
        
        self.Controls.Add(btnPrev)
        self.Controls.Add(btnNext)
        
    def ItemsSetup(self):
        Items.WaitForContents(self.Chest, 5000)
        cont = [i for i in self.Chest.Contains if i.ItemID in self.Jewelry]        
        column = [10, 180, 350, 520]
        row = [10, 200, 385, 570]
        point = []
        for r in row:
            for c in column:
                point.append(Point(c,r))
        pcnt = 0  
        page = []
        for i in xrange(len(cont)):
            m = None
            if i != 0 and i % 12 == 0:
                self.Pages.append(page)
                page = []
                pcnt = len(self.Pages) - 1
            
            item = cont[i]
            props = self.propLister(item)
            if props is None or props == [] or len(props) < 2:
                continue
            page.append(Monile(props, item.Serial, self, i % 12, point[i % 12]))
            
        if len(cont) % 12 != 0:
            self.Pages.append(page)
            
    def ShowItems(self):
        if self.Pages == []:
            return
        for i in xrange(len(self.Pages[self.CurPage])):
            m = self.Pages[self.CurPage][i]
            self.Controls.Add(m)
            
    def RemoveJewel(self, i):
        self.Controls.Remove(self.Pages[self.CurPage][i])
        del(self.Pages[self.CurPage][i])
        
    def PurgePage(self):
        for m in self.Pages[self.CurPage]:
            self.Controls.Remove(m)
            
    def NextPagePressed(self, sender, args):
        if self.CurPage < len(self.Pages) - 1:
            self.PurgePage()
            self.CurPage += 1
            self.ShowItems()
            
    def PrevPagePressed(self, sender, args):
        if self.CurPage > 0 and len(self.Pages) > 0:
            self.PurgePage()
            self.CurPage -= 1
            self.ShowItems()
            

Misc.SendMessage('Target the container you wish to scan.', 82)
chest = Target.PromptTarget()
Items.UseItem(chest)
Misc.Pause(600)
form = JewelManager(chest)
Application.Run(form)
