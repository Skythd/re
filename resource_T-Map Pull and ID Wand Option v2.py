# T-Map ID & Pull by MatsaMilla
# Last Edit 6/4/18
# Disable auto-open corpses to run smoother
# Uses wands if ID skill below 80.

#*********** SETUP SECTION*********************************

# Replace with beetle serial if you have one 
beetle = 0x0006EB2A

# False if you don not have beetle 
beetleBag = True

# True if you want to keep scrolls
sortScrolls = False

# turn to true if client has tool tips enabled
toolTipsOn = True

# Will use ID Wand if skill Item ID below 80
if Player.GetRealSkillValue('Item ID') < 80:
    idWand = True
else:
    idWand = False

#**********************************************************

Misc.SendMessage('Starting TMap Pull and ID', 33)
skillTimer = 0
dragTime = 800
msgColor = 68
self = Mobiles.FindBySerial(Player.Serial)
heavy = Player.MaxWeight - 10
rightHand = Player.CheckLayer('RightHand')
leftHand = Player.CheckLayer('LeftHand')

#loot includes gate, recall & lvl 8 summoning scrolls
loot = [0x2260,0x1f4c,0x1f60,0x1f66,0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c]
perk = [0x2dd5,0x1f18,0x2da3,0x166e,0x26BB,0x139B]
gold = [0xeed]
gems = [0xf16,0xf15,0xf19,0xf25,0xf21,0xf10,0xf26,0xf2d,0xf13]
wands = [0xdf5,0xdf3,0xdf4,0xdf2]
boneArmor = [0x1450,0x1f0b,0x1452,0x144f,0x1451,0x144e]
regs= [0xf7a,0xf7b,0xf86,0xf84,0xf85,0xf88,0xf8d,0xf8c]

scrolls = [0x1f2d,0x1f2e,0x1f2f,0x1f30,0x1f31,0x1f32,0x1f33,0x1f34,0x1f35,0x1f36,0x1f37,0x1f38,0x1f39,
0x1f3a,0x1f3b,0x1f3c,0x1f3d,0x1f3e,0x1f3f,0x1f40,0x1f41,0x1f42,0x1f43,0x1f44,0x1f45,0x1f46,0x1f47,0x1f48,
0x1f49,0x1f4a,0x1f4b,0x1f4d,0x1f4e,0x1f4f,0x1f50,0x1f51,0x1f52,0x1f53,0x1f54,0x1f55,0x1f56,0x1f57,0x1f58,
0x1f59,0x1f5a,0x1f5b,0x1f5c,0x1f5d,0x1f5e,0x1f5f,0x1f60,0x1f61,0x1f62,0x1f63,0x1f64,0x1f65,0x1f66,0x1f67,
0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c]

trash = [0x1717,0x1718,0x1544,0x1540,0x1713,0x1715,0x1714,0x1716,0x1717,0x1718,0x1719,0x171a,0x171b,
0x171c,0x2306,0x13f6,0xec4,0x1716,0xe81,0xe86,]

# Anything in keepProps will be kept after ID. Anything in slashprops & sub slash props will be kept if it matches both
slashProps = ['Invulnerability','Exceptional','Power']
subSlashProps = ['Indestructable', 'Fortified', 'Massive','Substantial','Supremely Accurate','Exceedingly Accurate','Eminently Accurate']
keepProps = ['Vanquishing','Silver','Undead','Snake','Lizardman','Dragon','Reptilian','Terathan','Scorpion',
'Spider','Orc Slaying','Ogre','Water','Earth','Elemental','Flame','Vacuum','Repond','Fey','Gargoyle',
'Daemon','Exorcism','Poison', 'Arachnid']

idItems = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,
0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,
0x13c6,0x13cd,0x13cc,0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a,0x1450,0xf62,
0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,0x143d,0x13b4,0xe81,0x13f8,0xf5c,
0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,0x13fb,
0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x13b2,]

# check / set bags. Idea from Wardoc (thanks!)
def GetBag ( sharedValue, promptString ):
    if Misc.CheckSharedValue( sharedValue ):
        bag = Misc.ReadSharedValue( sharedValue )
        if not Items.FindBySerial( bag ):
            bag = Target.PromptTarget( promptString )
            Misc.SetSharedValue( sharedValue, bag )
    else:
        bag = Target.PromptTarget( promptString )
        Misc.SetSharedValue( sharedValue, bag )
    return bag
    
regBag = GetBag( 'regBag', 'Select Bag for Regs' )
sellBag = GetBag( 'sellBag', 'Select Bag for BAD weps and armor' )
keepBag = GetBag( 'keepBag', 'Select Bag for GOOD weps and armor' )
gemBag = GetBag( 'gemBag', 'Select Bag for Gems' )
trashCan = GetBag( 'trashCan', 'Select corpse to dump on')
if sortScrolls:
    scrollBag = GetBag( 'scrollBag', 'Select Bag for Scrolls' )

chest = Target.PromptTarget('Select Treasure Chest')

mapChest = Items.FindBySerial(chest)
Items.UseItem(mapChest)
Misc.Pause(dragTime)

def checkWeight():
    if Player.Weight >= heavy:
        Player.ChatSay(msgColor, 'Overweight, stopping!')
        Stop

def checkDistance():
    Timer.Create('Distance', 5000)
    while mapChest.DistanceTo(self) > 2:
        if not Timer.Check('Distance'):
            Player.HeadMessage(msgColor, 'Too Far Away')
            Timer.Create('Distance', 2500)

def goldToBeetle():
    #moves gold to beetle
    if beetleBag:
        for s in mapChest.Contains:
            checkDistance()
            if s.ItemID in gold:
                if Player.Mount:
                    Mobiles.UseMobile(Player.Serial)
                    Misc.Pause(dragTime)
                Items.Move(s, beetle, 0)
                Misc.Pause(dragTime)
                if not Player.Mount:
                    Mobiles.UseMobile(beetle)
                    Misc.Pause(dragTime)
                    
def idStuffToolTips(container, type):
    idContainer = Items.FindBySerial(container)
    
    if type == 'weps':
        idItems = weps
        tier1 = keepWepDmgMods
        tier2 = keepWepAccuracyMods
        worthlessBag = sellBag
    elif type == 'armor':
        idItems = armor
        tier1 = keepArmorMods
        tier2 = keepArmorHPMods
        worthlessBag = sellBag
    elif type == 'bone':
        idItems = boneArmor
        tier1 = keepArmorMods
        tier2 = ['Indestructible']
        worthlessBag = trashCan
    
        
    for i in idContainer.Contains:
        worldSave()
        if i.ItemID in idItems:
            checkWeight()
            Journal.Clear()
            idTarget()
            Target.WaitForTarget(1500)
            Target.TargetExecute(i.Serial)
            Misc.Pause(dragTime)
            Items.WaitForProps(i,2000)
            props = Items.GetPropStringList(i)
            if any(elem in keepProps for elem in props):
                #** Good Stuff Move **
                Items.Move(i, keepBag, 0)
                Misc.Pause(dragTime)
            elif any(elem in tier1 for elem in props):
                #moves items if in sell ids
                if i.ItemID in sellItems:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
                elif any(elem in tier2 for elem in props):
                    #** Good Stuff Move **
                    Items.Move(i, keepBag, 0)
                    Misc.Pause(dragTime)
                else:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, worthlessBag, 0)
                Misc.Pause(dragTime)
            
def itemID():        
    for i in mapChest.Contains:
        if i.ItemID in idItems:
            checkWeight()
            checkDistance()
            Journal.Clear()
            idTarget()
            Target.WaitForTarget(1500)
            Target.TargetExecute(i.Serial)
            Misc.Pause(dragTime)
            Items.SingleClick(i)
            if Journal.Search('Unidentified'):
                idTarget()
                Target.WaitForTarget(1500)
                Target.TargetExecute(i.Serial)
                Misc.Pause(200)
                Items.SingleClick(i)
                Misc.Pause(dragTime)
            if any(Journal.Search(keep) for keep in keepProps):
                #** Good Stuff Move **
                Items.Move(i, keepBag, 0)
                Misc.Pause(dragTime)
            elif any(Journal.Search(slash) for slash in slashProps):
                if any(Journal.Search(sub) for sub in subSlashProps):
                    #** Good Stuff Move **
                    Items.Move(i, keepBag, 0)
                    Misc.Pause(dragTime)
                else:
                    #** Sell Stuff Move **
                    Items.Move(i, sellBag, 0)
                    Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, sellBag, 0)
                Misc.Pause(dragTime)
        elif i.ItemID in boneArmor:
            checkWeight()
            checkDistance()
            Journal.Clear()
            idTarget()
            Target.WaitForTarget(1500)
            Target.TargetExecute(i.Serial)
            Misc.Pause(200)
            Items.SingleClick(i)
            Misc.Pause(dragTime)
            if Journal.Search('Unidentified'):
                idTarget()
                Target.WaitForTarget(1500)
                Target.TargetExecute(i.Serial)
                Misc.Pause(200)
                Items.SingleClick(i)
                Misc.Pause(dragTime)
            if any(Journal.Search(keep) for keep in keepProps):
                #** Good Stuff Move **
                Items.Move(i, keepBag, 0)
                Misc.Pause(dragTime)
            elif any(Journal.Search(slash) for slash in slashProps):
                if any(Journal.Search(sub) for sub in subSlashProps):
                    #** Good Stuff Move **
                    Items.Move(i, keepBag, 0)
                    Misc.Pause(dragTime)
                else:
                    #** Sell Stuff Move **
                    Items.Move(i, trashCan, 0)
                    Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, trashCan, 0)
                Misc.Pause(dragTime)
                
def pullGems():
    for i in mapChest.Contains :
        checkDistance()
        checkWeight()
        if i.ItemID in gems:
            Items.Move(i, gemBag, 0)
            Misc.Pause(dragTime)
                
def pull():
    for i in mapChest.Contains :
        checkDistance()
        checkWeight()
        if i.ItemID in gold:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in loot:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in perk:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in regs:
            Items.Move(i, regBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in wands:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in scrolls:
            if sortScrolls:
                Items.Move(i, scrollBag, 0)
                Misc.Pause(dragTime)

def trashStuff():
    for i in mapChest.Contains :
        checkDistance()
        checkWeight()
        if i.ItemID in scrolls:
            Items.Move(i, trashCan, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in trash:
            Items.Move(i, trashCan, 0)
            Misc.Pause(dragTime)
            
def equipWand():
    global wandSerial
    player_bag = Items.FindBySerial(Player.Backpack.Serial)
    if leftHand:
        Player.UnEquipItemByLayer('LeftHand')
        
    if not rightHand:
        for i in player_bag.Contains:
            if i.ItemID in wands:
                Player.EquipItem(i.Serial)
                Misc.Pause(dragTime)
                wandSerial = Player.GetItemOnLayer('RightHand').Serial
    elif Player.GetItemOnLayer('RightHand').ItemID in wands:
        wandSerial = Player.GetItemOnLayer('RightHand').Serial
    else:
        Player.ChatSay(33, "No Wands Found, Stopping Script")
        Misc.ScriptStop('TMap Pull and ID.py')
        
def idTarget():
    if idWand:
        equipWand()
        Items.UseItem(wandSerial)
    else:
        Player.UseSkill('Item ID')
        Misc.Pause(100)
    if not Target.HasTarget():
        idTarget()
        

goldToBeetle()
pullGems()
pull()
itemID() 
trashStuff()           
Player.HeadMessage(msgColor, 'Chest Cleared, Thanks MatsaMilla!')