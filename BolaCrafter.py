#Bola Crafter by Frank Castle
#
#What you need:
#1 - Tinkering skill
#2 - Storage Container with Iron ingots and Leather
#3 - Tinker Tool



from System.Collections.Generic import List

global stoCont

stoCont = Target.PromptTarget('Target your resource chest')
Misc.Pause(100)
Items.UseItem(stoCont)
Misc.Pause(1100)

def checkTools():
    checkIngots()
    countOne = Items.BackpackCount(0x1EB9,-1)
    while countOne < 3:
        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
        Misc.Pause(1100)
        Items.UseItem(tinkerTool)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 11)
        Misc.Pause(1500)
        countOne = Items.BackpackCount(0x1EB9,-1)
        Misc.SendMessage('I have {} tinker tools in my bag'.format(countOne),48)
        
def checkIngots():
    if Items.BackpackCount(0x1BF2,0x0000) < 15:
        global stoCont
        Misc.SendMessage('Getting Ingots',48)
        Misc.Pause(1100)
        ingot = Items.FindByID(0x1BF2,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(ingot,Player.Backpack.Serial,50)
        Misc.Pause(1100)
        
def checkLeather():
    if Items.BackpackCount(0x1081,0x0000) < 4:
        global stoCont
        Misc.SendMessage('Getting Leather',48)
        Misc.Pause(1100)
        leather = Items.FindByID(0x1081,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(leather,Player.Backpack.Serial,20)
        Misc.Pause(1100) 

def makeBalls():
    countX = Items.BackpackCount(0x0E73,-1)
    while countX < 4:
        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
        checkTools()
        checkIngots()
        Items.UseItem(tinkerTool)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 38)
        Misc.Pause(1500)
        countX = Items.BackpackCount(0x0E73,-1)
        Misc.SendMessage('I have {} bola balls in my bag'.format(countX),48)
        
def assembleBola():
    tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
    checkTools()
    checkIngots()
    checkLeather()
    Items.UseItem(tinkerTool)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 207)
    Misc.Pause(1100)
    Bola = Items.FindByID(0x26AC,-1,Player.Backpack.Serial)
    if Bola:
        Items.Move(Bola,stoCont,0)
        Misc.Pause(1100)
    
while True:
    makeBalls()
    assembleBola()
    
    
    
    
    
    

    