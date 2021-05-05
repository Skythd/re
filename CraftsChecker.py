#===========================================#
#               Crafts Checker              #
#===========================================#
#                                           #
#   Author: CookieLover                     #
#   Release Date: 10/04/2017                #
#                                           #
#===========================================#
#                                           #
#   What you need:                          #
#   - a bag with crafts in it               #
#   - tools if you want to smelt/cut        #
#                                           #
#   Info:                                   #
#   - the bag mustn't be your backpack      #
#   - if a tool is checked, everything      #
#     that doesn't meet the standards will  #
#     be smelted/cut if possible            #
#   - if you check None, unwanted equips    #
#     will stay inside the bag and wanted   #
#     ones will be put in your backpack     #
#   - the value for properties with no      #
#     value such as Balanced, Exceptional,  #
#     Slayer, etc. is 1                     #
#   - you can add properties not listed     #
#     by filling the box                    #
#                                           #
#===========================================#


import clr, time

clr.AddReference("System.Collections")
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

from System.Collections import *
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, ComboBox, 
    BorderStyle, GroupBox, Label, TextBox, ListBox, Panel, RadioButton,
    FlatStyle)
    
class KeepForm(Form):
    IDs = {
        'scissors' : [0x0F9E, 0x0F9F],
        'tongs' : [0x0FBB, 0x0FBC]
        }
    Props = {}
    CurVer = '1.0.0'
    ScriptName = 'Crafts Checker'

    def __init__(self):
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(300, 337)
        self.Text = '{0} - v{1}'.format(self.ScriptName, self.CurVer)
        
        self.btnStart = Button()
        self.btnStart.Text = 'Start'
        self.btnStart.BackColor = Color.FromArgb(50,50,50)
        self.btnStart.Location = Point(222, 257)
        self.btnStart.Size = Size(50, 30)
        self.btnStart.FlatStyle = FlatStyle.Flat
        self.btnStart.FlatAppearance.BorderSize = 1
        self.btnStart.Click += self.btnStartPressed
        
        self.ControlsSetup()
        self.ToolsSetup()
        
        self.Controls.Add(self.pnlControls)
        self.Controls.Add(self.pnlTools)
        self.Controls.Add(self.btnStart)        
    
    def ToolsSetup(self):
        self.pnlTools = Panel()
        self.pnlTools.BackColor = Color.FromArgb(25,25,25)
        self.pnlTools.Size = Size(200, 30)
        self.pnlTools.Location = Point(12, 257)
        
        self.rbNone = RadioButton()
        self.rbNone.Text = 'None'
        self.rbNone.Checked = True
        self.rbNone.Location = Point(0, 0)
        self.rbNone.BackColor = Color.FromArgb(25,25,25)
        self.rbNone.ForeColor = Color.FromArgb(231,231,231)
        self.rbNone.Size = Size(50, 30)
        
        self.rbScissors = RadioButton()
        self.rbScissors.Text = 'Scissors'
        self.rbScissors.Location = Point(60, 0)
        self.rbScissors.BackColor = Color.FromArgb(25,25,25)
        self.rbScissors.ForeColor = Color.FromArgb(231,231,231)
        self.rbScissors.Size = Size(70, 30)
        
        self.rbTongs = RadioButton()
        self.rbTongs.Text = 'Tongs'
        self.rbTongs.Location = Point(140, 0)
        self.rbTongs.BackColor = Color.FromArgb(25,25,25)
        self.rbTongs.ForeColor = Color.FromArgb(231,231,231)
        self.rbTongs.Size = Size(60, 30)
        
        self.pnlTools.Controls.Add(self.rbNone)
        self.pnlTools.Controls.Add(self.rbScissors)
        self.pnlTools.Controls.Add(self.rbTongs)

        
    def ControlsSetup(self):
        self.pnlControls = GroupBox()
        self.pnlControls.BackColor = Color.FromArgb(35,35,35)
        self.pnlControls.Size = Size(260, 235)
        self.pnlControls.Location = Point(12, 12)
        self.pnlControls.ForeColor = Color.FromArgb(231,231,231)
        self.pnlControls.Text = 'Props'
        
        self.cbProps = ComboBox()
        self.cbProps.BackColor = Color.FromArgb(25,25,25)
        self.cbProps.ForeColor = Color.FromArgb(231,231,231)
        self.cbProps.Location = Point(12, 21)
        self.cbProps.Size = Size(150, 30)
        
        self.txtProps = TextBox()
        self.txtProps.BackColor = Color.FromArgb(25,25,25)
        self.txtProps.ForeColor = Color.FromArgb(231,231,231)
        self.txtProps.BorderStyle = BorderStyle.FixedSingle
        self.txtProps.Location = Point(172, 21)
        self.txtProps.Text = '1'
        self.txtProps.Size = Size(30, 30)
        
        self.btnAddProp = Button()
        self.btnAddProp.Text = 'Add'
        self.btnAddProp.BackColor = Color.FromArgb(50,50,50)
        self.btnAddProp.Location = Point(212, 16)
        self.btnAddProp.Size = Size(35, 30)
        self.btnAddProp.FlatStyle = FlatStyle.Flat
        self.btnAddProp.FlatAppearance.BorderSize = 1
        self.btnAddProp.Click += self.btnAddPropPressed
        
        self.btnDelProp = Button()
        self.btnDelProp.Text = 'Del'
        self.btnDelProp.BackColor = Color.FromArgb(50,50,50)
        self.btnDelProp.Location = Point(212, 178)
        self.btnDelProp.Size = Size(35, 30)
        self.btnDelProp.FlatStyle = FlatStyle.Flat
        self.btnDelProp.FlatAppearance.BorderSize = 1
        self.btnDelProp.Click += self.btnDelPropPressed
        
        props = [
            'Balanced','Damage Increase', 'Enhance Potions', 
            'Exceptional', 'Faster Cast Recovery', 'Physical Damage',
            'Fire Damage', 'Cold Damage', 'Poison Damage', 'Energy Damage',
            'Faster Casting', 'Hit * Area', 'Hit Life Leech', 'Hit Mana Leech',
            'Hit Stamina Leech', 'Hit Fatigue', 'Hit Mana Drain','Super Slayer',
            'Slayer', 'Demon Slayer', 'Dragon Slayer', 'Fey Slayer', 'Repond Slayer',
            'Reptile Slayer', 'Undead Slayer', 'Vermin Slayer', 'Spellchanneling',
            'Swing Speed Increase','Velocity', 'Physical Resist',
            'Fire Resist', 'Cold Resist', 'Poison Resist', 'Energy Resist',
            'Hit Point Increase', 'Mana Increase', 'Stamina Increase',
            'Mana Regeneration', 'Hit Point Regeneration', 'Stamina Regeneration',
            'Lower Mana Cost', 'Lower Reagent Cost', 'Hit Chance Increase',
            'Defense Chance Increase', 'Hit * Spell', 'Hit Curse', 'Hit Dispel',
            'Hit Fireball', 'Hit Harm', 'Hit Lightning', 'Hit Magic Arrow',
            'Hit Lower Attack', 'Self Repair', 'Luck', 'Hit Lower Defense',
            'Reflect Physical Damage', 'Strength Bonus', 'Dexterity Bonus',
            'Intelligence Bonus'
            ]
            
        for p in props:
            self.cbProps.Items.Add(p)
        
        self.lbProps = ListBox()
        self.lbProps.BackColor = Color.FromArgb(25,25,25)
        self.lbProps.ForeColor = Color.FromArgb(231,231,231)
        self.lbProps.Location = Point(12, 61)
        self.lbProps.Size = Size(190, 150)
        
        self.pnlControls.Controls.Add(self.cbProps)
        self.pnlControls.Controls.Add(self.txtProps)
        self.pnlControls.Controls.Add(self.btnAddProp)
        self.pnlControls.Controls.Add(self.btnDelProp)
        self.pnlControls.Controls.Add(self.lbProps)
        
    def btnAddPropPressed(self, sender, args):
        if self.cbProps.Text != '':
        
            if self.txtProps.Text == '0' or self.txtProps.Text == '':
                num = 0
            else:
                num = int(self.txtProps.Text)
                
            self.lbProps.Items.Add('{0}, {1}'.format(self.cbProps.Text, num))
            
    def btnDelPropPressed(self, send, args):
        if self.lbProps.SelectedIndex > -1:
            i = self.lbProps.SelectedIndex
            self.lbProps.Items.Remove(self.lbProps.SelectedItem)
            
    def btnStartPressed(self, send, args):
        self.Props = {}
        for itm in self.lbProps.Items:
            prop = str(itm).split(',')
            self.Props[prop[0]] = int(prop[1].strip())
        
        if self.rbNone.Checked:
            checked = 0
        elif self.rbScissors.Checked:
            checked = 1
        else:
            checked = 2
            
        try:
            self.KeepSmelt(checked)
        except:
            Misc.SendMessage('{0}: There was an error.'.format(self.ScriptName), 33)
            pass
            
    def KeepSmelt(self, tool):
        bagid = Target.PromptTarget()
        tosmelt = []
        if bagid == -1:
            Misc.SendMessage('{0}: No container selected.'.format(self.ScriptName), 33)
            return
        
        bag = Items.FindBySerial(bagid)
        Items.WaitForContents(bag, 8000)
        
        starttime = time.time()

        for p in bag.Contains:            
            Items.WaitForProps(p, 8000)
            for k,v in self.Props.iteritems():
                if '*' in k:
                    if 'Area' in k:
                        hasarea = False
                        areas = ['Physical', 'Fire', 'Cold', 'Poison', 'Energy']
                        for area in areas:
                            if Items.GetPropValue(p, 'Hit {0} Area'.format(area)) >= v:
                                hasarea = True
                                break
                                
                        if not hasarea:
                            tosmelt.append(p.Serial)
                            break
                            
                    elif 'Spell' in k:
                        hasspell = False
                        spells = ['Lightning', 'Fireball', 'Harm', 'Magic Arrow', 'Curse']
                        for spell in spells:
                            if Items.GetPropValue(p, 'Hit {0}'.format(spell)) >= v:
                                hasspell = True
                                break
                                
                        if not hasspell:
                            tosmelt.append(p.Serial)
                            break
                            
                elif k == 'Super Slayer':
                    hassuper = False
                    supers = ['Demon', 'Fey', 'Repond', 'Reptile', 'Undead', 'Vermin']
                    for super in supers:
                        if Items.GetPropValue(p, '{0} Slayer'.format(super)) == 1:
                            hassuper = True
                            break
                            
                    if not hassuper:
                        tosmelt.append(p.Serial)
                        break
                        
                elif k == 'Slayer':
                    propstr = ''.join(s.lower() for s in Items.GetPropStringList(p))
                    if not 'slayer' in propstr:
                        tosmelt.append(p.Serial)
                        break
                        
                else:
                    if Items.GetPropValue(p, k) < v:
                        tosmelt.append(p.Serial)
                        break
                        
        if tool == 0: # none, it puts wanted items in backpack and leave unwanted ones in the bag
            wanted = [w for w in bag.Contains if not w.Serial in tosmelt]
            for w in wanted:
                Items.Move(w, Player.Backpack, 0)
                Misc.Pause(600)

        elif tool == 1: # scissors, it cuts unwanted items
            tool = next(t for t in Player.Backpack.Contains if t.ItemID in self.IDs['scissors'])
            
            if tool is None:
                Misc.SendMessage('{0}: No scissors found.'.format(self.ScriptName), 33)
            else:
                for ts in tosmelt:
                    Items.UseItem(tool)
                    Target.WaitForTarget(8000)
                    Target.TargetExecute(ts)
                    Misc.Pause(300)
                    
        else: # tongs, it smelts unwanted items
            tool = next(t for t in Player.Backpack.Contains if t.ItemID in self.IDs['tongs'])
            
            if tool is None:
                Misc.SendMessage('{0}: No tongs found.'.format(self.ScriptName), 33)
            else:
                Gumps.ResetGump()
                Items.UseItem(tool)
                for ts in tosmelt:
                    Gumps.WaitForGump(949095101, 8000)
                    Gumps.SendAction(949095101, 14)
                    Target.WaitForTarget(8000)
                    Target.TargetExecute(ts)
                    Misc.Pause(300)
                    
        m, s = divmod(time.time() - starttime, 60)
        Misc.SendMessage('{0}: Done in {1}m {2}s!'.format(self.ScriptName, int(m), s), 76)
        
                                
        
form = KeepForm()
Application.Run(form)
        