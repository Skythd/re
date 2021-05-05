#=================================================#
#                   Sop Manager                   #
#=================================================#
#                                                 #
#   Author: CookieLover                           #
#   Release Date: 10/11/2017                      #
#                                                 #
#=================================================#
#                                                 #
#   What you need:                                #
#   - a container to ransack                      #
#                                                 #
#   Info:                                         #
#   - you can move the selected item into your    #
#     backpack by pressing Get                    #
#   - upon creating the list a file will be saved #
#     in your Razor Enhanced main folder named    #
#     sopchest_*.txt with * being the current     #
#     date and time to avoid overwriting          #
#                                                 #
#=================================================#

import clr, time, thread

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')

import System
from System.Collections.Generic import List
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, BorderStyle, 
    Label, FlatStyle, DataGridView, DataGridViewAutoSizeColumnsMode,
    DataGridViewSelectionMode, DataGridViewEditMode, CheckBox)
from System.Data import DataTable

class SingleSop(System.IComparable, System.IConvertible):
    ID = value = days = 0
    skill = ''

    SkillList = [
        "Anatomy", "Animal Lore", "Animal Taming", "Archery", "Blacksmithy", 
        "Bushido", "Chivalry", "Discordance", "Evaluating Intelligence", "Fencing", "Fishing", 
        "Focus", "Healing", "Imbuing", "Mace Fighting", "Magery", "Meditation", "Musicianship", 
        "Mysticism", "Necromancy", "Ninjitsu", "Parrying", "Peacemaking", "Provocation", 
        "Resisting Spells", "Spellweaving", "Spirit Speak", "Stealing", "Stealth", "Swordsmanship", 
        "Tactics", "Tailoring", "Throwing", "Veterinary", "Wrestling", "Eval Intelligence"
        ]

    ValueList = [105,110,115,120]

    def __init__(self, serial, title, last):
        self.ID = serial
        self.value, self.skill, self.days = self.GetSop(title, last)

    def GetSop(self, t, l):
        sk = next(s for s in self.SkillList if s.lower() in t.lower())
        va = next(v for v in self.ValueList if str(v) in t)
        da = int(l.lower().replace(' days until deletion', '').strip())
        return va, sk, da
        
class SOPChestForm(Form):
    CurVer = '1.0.0'
    ScriptName = 'Sop Manager'
    Contents = []
    
    def __init__(self, contents):
        self.Contents = contents
        
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(334, 400)
        self.Text = '{0} - v{1}'.format(self.ScriptName, self.CurVer)
                
        self.DataGridSetup()
        
        self.btnGet = Button()
        self.btnGet.Text = 'Get'
        self.btnGet.BackColor = Color.FromArgb(50,50,50)
        self.btnGet.Location = Point(254, 324)
        self.btnGet.Size = Size(50, 30)
        self.btnGet.FlatStyle = FlatStyle.Flat
        self.btnGet.FlatAppearance.BorderSize = 1
        self.btnGet.Click += self.btnGetPressed
        
        self.Controls.Add(self.DataGrid)
        self.Controls.Add(self.btnGet)
        
        #self.DataGrid.Columns(0).Visible = False
           
    def DataGridSetup(self):
        self.DataGrid = DataGridView()
        self.DataGrid.RowHeadersVisible = False
        self.DataGrid.MultiSelect = False
        self.DataGrid.SelectionMode = DataGridViewSelectionMode.FullRowSelect
        self.DataGrid.BackgroundColor = Color.FromArgb(25,25,25)
        self.DataGrid.RowsDefaultCellStyle.BackColor = Color.Silver
        self.DataGrid.AlternatingRowsDefaultCellStyle.BackColor = Color.Gainsboro
        self.DataGrid.ForeColor = Color.FromArgb(25,25,25)
        self.DataGrid.Location = Point(12, 12)
        self.DataGrid.Size = Size(292, 306)
        self.DataGrid.DataSource = self.Data()
        self.DataGrid.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells
        self.DataGrid.EditMode = DataGridViewEditMode.EditProgrammatically
        self.DataGrid.BorderStyle = BorderStyle.None
        
    def btnGetPressed(self, sender, args):
        row = self.DataGrid.SelectedCells[0].RowIndex
        
        if row == -1:
            Misc.SendMessage('{0}: No row selected.'.format(self.ScriptName), 33)
            return
            
        col = self.DataGrid.SelectedCells[3].ColumnIndex
        serial = self.DataGrid.Rows[row].Cells[col].Value
        self.DeleteRow(serial)
        Items.Move(int(serial, 0), Player.Backpack, 0)
            

    def DeleteRow(self, serial):
        for r in xrange(self.DataGrid.DataSource.Rows.Count):
            row = self.DataGrid.DataSource.Rows[r]
            if row['ID'] == serial:
                self.DataGrid.DataSource.Rows.Remove(row)
                return        
            
    def Data(self):
        data = DataTable()        
        data.Columns.Add('Value', clr.GetClrType(int))
        data.Columns.Add('Skill', clr.GetClrType(str))
        data.Columns.Add('Days', clr.GetClrType(int))
        data.Columns.Add('ID', clr.GetClrType(str))
        
        for content in self.Contents:
            data.Rows.Add(content.value, content.skill, content.days, hex(content.ID))
           
        return data

contents = []
filetext = []

filename = 'sopchest_{0}.txt'.format(time.strftime('%y%m%d%H%M'))

Misc.SendMessage('Target a container to manage power scrolls.', 76)       
contid = Target.PromptTarget()
if contid > -1:
    cont = Items.FindBySerial(contid)
    Items.WaitForContents(cont, 8000)
    Misc.Pause(500)
    
    sops = [i for i in cont.Contains if (i.ItemID == 0x14F0 and i.Hue == 0x0481)]
    
    for s in sops:
        Items.WaitForProps(s, 8000)
        plist = list(Items.GetPropStringList(s))
        sop = SingleSop(s.Serial, plist[0], plist[-1])
        contents.append(sop)
        filetext.append('{1} {2} {3} days ({0})'.format(hex(s.Serial), sop.value, sop.skill, sop.days))

    if contents == []:
        Misc.SendMessage('It is either empty or not a container at all.', 33)
    else:
        with open(filename, 'w') as f:
            f.write('\n'.join(t for t in filetext))
        form = SOPChestForm(contents)
        Application.Run(form)
    
else:
    Misc.SendMessage('No container was targeted.', 33)
    

