##########   Enchanted Apple Crafter by Frank Castle   ########## 
#
#You need a secure container with plenty of apples, greater heal potions, and iron ingots
#You also need one player made tinker tool in your backpack
#You must have GM Cooking and Tinkering
#
#WARNING! This will make Enchanted Apples until you run out of one of the supplies.

from System.Collections.Generic import List

supplyChest = Target.PromptTarget('Target your Secure Storage Now')

def checkSupplies():
    if Items.BackpackCount(0x09D0,0x0000) < 1: #apples
        getApples()
    if Items.BackpackCount(0x0F0C,0x0000) < 1: #gheals
        getGheals()
    Misc.Pause(200)    

def checkTools():        
    if Items.BackpackCount(0x1EB9,-1) < 2: #tinker tools
        makeTinker()
    if Items.BackpackCount(0x097F,-1) < 1: #skillets
        makeSkillet()
    Misc.Pause(200)
    
def makeTinker():
    if Items.BackpackCount(0x1BF2,-1) < 10:
        sIngot = Items.FindByID(0x1BF2,-1,supplyChest)
        Misc.Pause(200)
        Items.Move(sIngot,Player.Backpack.Serial,10)
        Misc.Pause(1200)
    Items.UseItemByID(0x1EB9,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 11)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    Misc.Pause(1100)
        
def makeSkillet():
    if Items.BackpackCount(0x1BF2,-1) < 10:
        sIngot = Items.FindByID(0x1BF2,-1,supplyChest)
        Misc.Pause(200)
        Items.Move(sIngot,Player.Backpack.Serial,10)
        Misc.Pause(1200)
    Items.UseItemByID(0x1EB9,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 26)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    Misc.Pause(200)
        
def getApples():
    sApple = Items.FindByID(0x09D0,0x0000,supplyChest)
    Misc.Pause(200)
    Items.Move(sApple,Player.Backpack.Serial,50)
    Misc.Pause(1200)
    
def getGheals():
    sGheal = Items.FindByID(0x0F0C,0x0000,supplyChest)
    Misc.Pause(200)
    Items.Move(sGheal,Player.Backpack.Serial,50)
    Misc.Pause(1200)
    
def makeApples():
    Items.UseItemByID(0x097F,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 43)
    Misc.Pause(200)
    
    
def makeLast():
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 1999)
    if Journal.Search('You have worn out your tool!') == True:
        Journal.Clear()
        checkTools()
        Misc.Pause(300)
        Items.UseItemByID(0x097F,-1)
    Journal.Clear()
    Misc.Pause(200)
    
def moveEncApp():
    EncApp = Items.FindByID(0x2FD8,0x0488,Player.Backpack.Serial)
    Items.Move(EncApp,supplyChest,0)
    Misc.Pause(1200)
    
def appleLoop():
    makeApples()
    while Items.BackpackCount(0x2FD8,0x0488) < 50:
        checkSupplies()
        makeLast()
    moveEncApp()    
    
def main():
    Items.UseItem(supplyChest)
    Misc.Pause(1200)
    checkSupplies()
    checkTools()
    appleLoop()

    
while True:
    main()    
    
    
        






