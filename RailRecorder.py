# UI rail recorder by Mourn 8182 discord
# must figure out how to import os
# Creates RAIL.txt in your DOCUMENTS FOLDER, you can cut and paste into scripts

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Drawing import Point
from System.Windows.Forms import Application, Button, Form, Label, TextBox
from System.Text import Encoding
from System.Threading import ThreadStart, Thread
import sys
sys.path.append(r'C:\Program Files (x86)\IronPython.StdLib.2.7.9')  # D/L and adjust path for your library sorry 
import os

list = []

def go(x1, y1):
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = -1
    PathFinding.Go(Coords)
    
class SimpleTextBoxForm(Form):
    def __init__(self):
        self.Text = "Fast Rails"
        self.Width = 250
        self.Height = 180
        self.TopMost = True
       
        self.button = Button()
        self.button.Text = 'Add Coord'
        self.button.Width = 100
        self.button.Height = 40
        self.button.Location = Point(10, 10)
        self.button.Click += self.add
        
        self.button1 = Button()
        self.button1.Text = 'Del last Coord'
        self.button1.Width = 100
        self.button1.Height = 40
        self.button1.Location = Point(125, 10)
        self.button1.Click += self.delLast

        self.button2 = Button()
        self.button2.Text = 'Clear All'
        self.button2.Width = 100
        self.button2.Height = 40
        self.button2.Location = Point(125, 50)
        self.button2.Click += self.clear
        
        self.button3 = Button()
        self.button3.Text = 'Test Rail'
        self.button3.Width = 100
        self.button3.Height = 40
        self.button3.Location = Point(10, 50)
        self.button3.Click += self.test
        
        self.button4 = Button()
        self.button4.Text = 'INFO'
        self.button4.Width = 100
        self.button4.Height = 40
        self.button4.Location = Point(10, 90)
        self.button4.Click += self.info
        
        self.button5 = Button()
        self.button5.Text = 'Make.TXT'
        self.button5.Width = 100
        self.button5.Height = 40
        self.button5.Location = Point(125, 90)
        self.button5.Click += self.makefile
      
        self.Controls.Add(self.button)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.button2)
        self.Controls.Add(self.button3)
        self.Controls.Add(self.button4)
        self.Controls.Add(self.button5)

    def add(self, sender, event):
        list.append([(Player.Position.X),(Player.Position.Y)])
        
        Misc.SendMessage('{} Total Coords'.format(len(list)))
        
           
    def test(self, sender, event):
        if len(list) > 0:
            for l in list:
                go(l[0],l[1])
        else:
            Misc.SendMessage('You didnt set any Coords!',33)
            
    def delLast(self, sender, event):
        if len(list) > 0:
            del list[-1]
            Misc.SendMessage('{} Total Coords'.format(len(list)))
        else:
            Misc.SendMessage('The Coord list is Empty!',33)
            
    def clear(self, sender, event):
        list.Clear()
        Misc.SendMessage('Coord list Cleared',180)
        
    def info(self, sender, event):
        if len(list) > 0:
            Misc.SendMessage('{} Total Coords'.format(len(list)),75)
            Misc.SendMessage('Last Coords were {}'.format(list[-1]),180)
            Misc.SendMessage('Current Coords are {}'.format(str(Player.Position.X)) + ',' + (str(Player.Position.Y)),285)
        else:
            Misc.SendMessage('You didnt set any Coords!',33)
            Misc.SendMessage('Current Coords are {}'.format(str(Player.Position.X)) + ',' + (str(Player.Position.Y)),285)
            
    def makefile(self, sender, event):
        rail_file = os.path.join(os.environ.get('userprofile', 'c:'), 'Documents', 'RAIL.txt')

        if not os.path.exists(rail_file):
            file = open(rail_file, 'w+')
            file.write(str(list))
            file.close()
        else:
            Misc.SendMessage('Over Writing Last Saved Rail',33)
            file = open(rail_file, 'w+')
            file.write(str(list))
            file.close()

    
form = SimpleTextBoxForm()
Application.Run(form)

