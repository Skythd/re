#Imbuing Trainer by Frank Castle with special guest Mourn
#
#What you need:
# 1 - 30.0+ Tinkering Skill. If you do not have it buy it up. 
# 1 - 40.0+ Imbuing. If you do not have it buy it up.
# 2 - a player made Tinker Tools
# 3 - a chest with plenty of iron ingots, leather, citrine, amber, emerald, and magical residue 
# 4 - GM Tailoring and at least GM Smithing.  Script will not check for crafting fails.
# Written and tested on OSI. 



from System.Collections.Generic import List

global stoCont
global timesImbued

stoCont = Target.PromptTarget('Target your resource chest')
Misc.Pause(100)
Items.UseItem(stoCont)
Misc.Pause(1100)

residue = 0x2DB1
amber = 0x0F25
citrine = 0x0F15
emerald = 0x0F10

def checkIngots():
    if Items.BackpackCount(0x1BF2,0x0000) < 20:
        global stoCont
        Misc.SendMessage('Getting Ingots',48)
        Misc.Pause(1100)
        ingot = Items.FindByID(0x1BF2,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(ingot,Player.Backpack.Serial,40)
        Misc.Pause(1100)
        
def checkLeather():
    if Items.BackpackCount(0x1081,0x0000) < 4:
        global stoCont
        Misc.SendMessage('Getting Leather',48)
        Misc.Pause(1100)
        leather = Items.FindByID(0x1081,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(leather,Player.Backpack.Serial,40)
        Misc.Pause(1100)        
        
def checkTools():
    checkIngots()
    countOne = Items.BackpackCount(0x1EB9,-1)
    while countOne < 3:
        Misc.Pause(1100)
        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
        Misc.Pause(1100)
        Items.UseItem(tinkerTool)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 11)
        Misc.Pause(1500)
        countOne = Items.BackpackCount(0x1EB9,-1)
        Misc.SendMessage('I have {} tinker tools in my bag'.format(countOne),48)
        
    countTwo = Items.BackpackCount(0x0F9D,-1)
    while countTwo < 3:
        Misc.Pause(1100)
        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(tinkerTool)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 14)
        Misc.Pause(1500)
        countTwo = Items.BackpackCount(0x0F9D,-1)
        Misc.SendMessage('I have {} sewing kits in my bag'.format(countTwo),48)
        
    countThree = Items.BackpackCount(0x0FBC,-1)
    while countThree < 3:
        Misc.Pause(1100)
        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(tinkerTool)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 20)
        Misc.Pause(1500)
        countThree = Items.BackpackCount(0x0FBC,-1)
        Misc.SendMessage('I have {} tongs in my bag'.format(countThree),48)

def checkImbuingMats(mat,gem):
    if Items.BackpackCount(mat,-1) < 10:
        global stoCont
        Misc.SendMessage('Getting Materials',90)
        Misc.Pause(1100)
        material = Items.FindByID(mat,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(material,Player.Backpack.Serial,100)
        Misc.Pause(1100)
        
    if Items.BackpackCount(gem,-1) < 10:
        global stoCont
        Misc.SendMessage('Getting Gems',90)
        Misc.Pause(1100)
        jewels = Items.FindByID(gem,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(jewels,Player.Backpack.Serial,100)
        Misc.Pause(1100)  

def imbueThrice(item):
    timesImbued = 0
    theTarget = Items.FindByID(item,-1,Player.Backpack.Serial)
    def firstImbue(item,timesImbued):
        checkImbuingMats(residue,amber)
        Player.UseSkill('Imbuing')
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 202)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 313)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        if timesImbued < 1:
            firstImbue(item,timesImbued)
        return timesImbued
    timesImbued = firstImbue(item,timesImbued)
    Misc.Pause(300)
    def secondImbue(item,timesImbued):
        checkImbuingMats(residue,citrine)
        Misc.Pause(500)
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 1114252)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 203)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 313)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        if timesImbued < 2:
            secondImbue(item,timesImbued)
        return timesImbued
    timesImbued = secondImbue(item,timesImbued)
    checkImbuingMats(residue,emerald)
    Misc.Pause(500)
    Gumps.WaitForGump(999059, 10000)
    Gumps.SendAction(999059, 1)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(theTarget)
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 1114254)
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 205)
    difficulty()
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 302)
    Misc.Pause(500)
    if Journal.Search('successfully imbue') == True:
        Journal.Clear()
        timesImbued = timesImbued + 1
    imbueLast(timesImbued,residue,emerald)    
    destroy(item)
        
def imbueTwice(item):
    timesImbued = 0
    theTarget = Items.FindByID(item,-1,Player.Backpack.Serial)
    def firstImbue(item,timesImbued):
        checkImbuingMats(residue,amber)
        Player.UseSkill('Imbuing')
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 202)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 313)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 311)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        if timesImbued < 1:
            firstImbue(item,timesImbued)
        return timesImbued
    timesImbued = firstImbue(item,timesImbued)        
    checkImbuingMats(residue,citrine)
    Misc.Pause(500)
    Player.UseSkill('Imbuing')
    Gumps.WaitForGump(999059, 10000)
    Gumps.SendAction(999059, 1)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(theTarget)
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 1114252)
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 203)
    difficulty()
    Gumps.WaitForGump(999056, 10000)
    Gumps.SendAction(999056, 302)
    Misc.Pause(500)
    if Journal.Search('successfully imbue') == True:
        Journal.Clear()
        timesImbued = timesImbued + 1
    imbueLast(timesImbued,residue,citrine)    
    destroy(item)    

def imbueOnce(item):
    timesImbued = 0
    theTarget = Items.FindByID(item,-1,Player.Backpack.Serial)
    if item == 0x1DB9:
        checkImbuingMats(residue,amber)
        Misc.Pause(500)
        Player.UseSkill('Imbuing')
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 202)
        difficulty()
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        imbueLast(timesImbued,residue,amber)
    elif item == 0x0F51:
        checkImbuingMats(residue,amber)
        Misc.Pause(500)
        Player.UseSkill('Imbuing')
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 1114251)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 202)
        difficulty()
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        imbueLast(timesImbued,residue,amber)
    elif item == 0x2777:
        checkImbuingMats(residue,citrine)
        Misc.Pause(500)
        Player.UseSkill('Imbuing')
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 1)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(theTarget)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 1114252)
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 203)
        difficulty()
        Gumps.WaitForGump(999056, 10000)
        Gumps.SendAction(999056, 302)
        Misc.Pause(500)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1
        imbueLast(timesImbued,residue,citrine)    
    destroy(item)

def imbueLast(timesImbued,mat,gem):
    while timesImbued < 20:
        checkImbuingMats(mat,gem)
        Gumps.WaitForGump(999059, 10000)
        Gumps.SendAction(999059, 4)
        Misc.Pause(200)
        if Journal.Search('successfully imbue') == True:
            Journal.Clear()
            timesImbued = timesImbued + 1    
            
def destroy(item):
    unravel = Items.FindByID(item,-1,Player.Backpack.Serial)
    Player.UseSkill('Imbuing')
    Gumps.WaitForGump(999059, 10000)
    Gumps.SendAction(999059, 2)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(unravel)
    
def makeLeatherCap():
    sewingKit = Items.FindByID(0x0F9D,-1,Player.Backpack.Serial)
    Misc.Pause(100)
    checkTools()
    checkLeather()
    Items.UseItem(sewingKit)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 609)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    imbueOnce(0x1DB9)
    
def makeDagger():
    tongs = Items.FindByID(0x0FBC,-1,Player.Backpack.Serial)
    Misc.Pause(100)
    checkTools()
    checkIngots()
    Items.UseItem(tongs)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 45)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    imbueOnce(0x0F51) 
    
def makeJingasa():
    tongs = Items.FindByID(0x0FBC,-1,Player.Backpack.Serial)
    Misc.Pause(100)
    checkTools()
    checkIngots()
    Items.UseItem(tongs)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 27)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    Imbuing = Player.GetSkillValue('Imbuing')
    if Imbuing < 90.1:
        imbueOnce(0x2777)
    elif Imbuing < 112.1:
        imbueTwice(0x2777)
    else:
        imbueThrice(0x2777)
    
    
def difficulty():
    Gumps.WaitForGump(999056, 10000)
    text = Gumps.LastGumpGetLineList()
    Misc.Pause(100)
    number = len(text)-1
    x = (text[number].split('.'))[0]
    Misc.SendMessage('{}% Success Chance'.format(x),44)
    Misc.Pause(500)
      
    if int(x) > 50:
        Gumps.SendAction(999056, 312)
        Misc.Pause(500)
        difficulty()    
    
    
def setFunction():
    Imbuing = Player.GetSkillValue('Imbuing')
    while Imbuing < 50.0:
        Imbuing = Player.GetSkillValue('Imbuing')
        makeLeatherCap()
    while Imbuing > 49.9 and Imbuing < 70.0:
        Imbuing = Player.GetSkillValue('Imbuing')
        makeDagger()
    while Imbuing > 69.9 and Player.GetSkillValue('Imbuing') != Player.GetSkillCap('Imbuing'):
        Imbuing = Player.GetSkillValue('Imbuing')
        makeJingasa()
    
    
    
setFunction()    

