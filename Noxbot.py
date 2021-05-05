from Scripts.utilities.items import MoveItem
from Scripts import config
from Scripts.glossary.colors import colors
from Scripts.glossary.items.moongates import FindMoongates
from Scripts.utilities.items import FindNumberOfItems
from Scripts.glossary.items.spellScrolls import spellScrolls

gumppause = 1000
arrowtimer = 0
bodtimer = 0
arrows = 0x0F3F
balance = 0
tongs = 0x0FBB
sewingkit=0x0F9D
unload = 0x41B89F04 #commpdity deed box at home to dump shit in








mountID = 0x001BF818#beetle ID

regs = [0x0F7A, 0x0F86, 0x0F7B, 0x0F8C, 0x0F84, 0x0F85, 0x0F8D, 0x0F88]

rune = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96] #only works with gate

book = [0,1,2,3,4,5,6]

book[0] = 0x4244D5C6 # 0 dungeons 
book[1] = 0x41206A84  # 1 champ spawns
book[3] = 0x463FCD14 #2 bro's houses
book[2] = 0x444E0FEA #Banks
book[4] =  0x41BE561B #provo
book[5] = 0x41BE58BC #Bods
book[6] = 0x463FAD08

itemQualityToKeep = [
    # Strength
    'Vanquishing', 'Invulnerability', 
    # Property Combos
    #'Indestructable/Invulnerability', 'Exceptional/Indestructible', 'Exceptional/Fortified',

    ### Slayer Types ###
    # Slayer Group: Humanoid
    'Repond', 'Goblin', 'Orc', 'Ogre', 'Troll',
    # Slayer Group: Undead
    'Undead', 'Silver',
    # Slayer Group: Fey
    'Fey',
    # Slayer Group: Elemental
    'Elemental', 'Air', 'Vacuum', 'Blood', 'Earth', 'Fire', 'Flame', 'Poison', 'Snow', 'Summer', 'Water',
    # Slayer Group: Abyss
    'Demon', 'Exorcism', 'Daemon', 'Gargoyle', 'Balron',
    # Slayer Group: Arachnid
    'Arachnid', 'Scorpion', 'Spider', 'Terathan',
    # Slayer Group: Reptilian
    'Reptile', 'Reptilian', 'Dragon', 'Lizardman', 'Ophidian', 'Snake'
]

scrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]  
gems = [0x0F25,0x0F15 ,0x0F26,0x0F16,  0x0F10,0x0F13,0x0F19,0x0F21,0x0F2D]


def tailorsell():
    webhook('heading to tailor shop')
    recall(book[5], 4)
    Misc.WaitForContext(0x00026014, 10000)
    Misc.ContextReply(0x00026014, 2)

def gemsell():
    webhook('heading to gem shop')
    recall(book[5], 5)
    Misc.WaitForContext(0x00243825, 10000)
    Misc.ContextReply(0x00243825, 2)    


def sellshit():
    castincog()
    smithsell()
    grabgold()
    tailorsell()
    grabgold()
    gemsell()
    grabgold()
 
    
    
    ##########################################################################################################

def baseloot(chest,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll):
     
    for reg in regs:
        Player.HeadMessage(54, 'Doing Regs')
        while Items.FindByID(reg, -1, chest):
            moveitem = Items.FindByID(reg, -1, chest) 
            Items.Move(moveitem, regchest, -1)
            Misc.Pause(750)
    Misc.Pause(750)
    for gem in gems:
        Player.HeadMessage(54, 'Doing gems')
        if Player.Weight > 400:
            return
        while Items.FindByID(gem, -1, chest):
            moveitem = Items.FindByID(gem, -1, chest) 
            Items.Move(moveitem, Player.Backpack.Serial, -1)
            Misc.Pause(750)
    Misc.Pause(750)
    while Items.FindByID(0x0EED, -1, chest):
        Player.HeadMessage(54, 'Doing gold')
        moveitem = Items.FindByID(0x0EED, -1, chest) 
        Items.Move(moveitem, goldchest, -1)
        Misc.Pause(750)
    while Items.FindByID(0x14EC, -1, chest):
        Player.HeadMessage(54, 'Maps')
        moveitem = Items.FindByID(0x14EC, -1, chest) 
        Items.Move(moveitem, mapchest, -1)
        Misc.Pause(750)
    for scrolls in scrollIDs:
            Player.HeadMessage(54, 'scrolls')
            while Items.FindByID(scrolls, -1, chest):
                moveitem = Items.FindByID(scrolls, -1, chest) 
                Items.Move(moveitem, trash, -1)
                Misc.Pause(750) 
    Misc.Pause(750)
    while Items.FindByID(0x2260, -1, chest):
        moveitem = Items.FindByID(0x2260, -1, chest) 
        Items.Move(moveitem, skillscroll, -1)
        Misc.Pause(500)
    while Items.FindByID(0x1452, -1, chest): #bone legs
        moveitem = Items.FindByID(0x1452, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)           
    while Items.FindByID(0x144F, -1, chest): #bone chest
        moveitem = Items.FindByID(0x144F, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)                 
    while Items.FindByID(0x1451, -1, chest): #bone helm
        moveitem = Items.FindByID(0x1451, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)                 
    while Items.FindByID(0x1714, -1, chest): #wide brim hat
        moveitem = Items.FindByID(0x1714, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)                 
    while Items.FindByID(0x1544, -1, chest): #scull cap
        moveitem = Items.FindByID(0x1544, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)
    while Items.FindByID(0x1719, -1, chest): #bonnet
        moveitem = Items.FindByID(0x1719, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)
    while Items.FindByID(0x171B, -1, chest): #tricorn
        moveitem = Items.FindByID(0x171B, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)  
    while Items.FindByID(0x144E, -1, chest): #bone arms
        moveitem = Items.FindByID(0x144E, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)       
    while Items.FindByID(0x1540, -1, chest): #bone arms
        moveitem = Items.FindByID(0x1540, -1, chest) 
        Items.Move(moveitem, trash, -1)
        Misc.Pause(750)             
                
def lockpickchest(chest):
    lockpicks = Items.FindByID(0x14FC, -1, Player.Backpack.Serial)
    Items.UseItem(lockpicks)
    if lockpicks == None:
        Player.HeadMessage( colors[ 'red' ], 'You don\'t have any lockpicks!' )
        return

    lockedChestSerial = chest.Serial
    lockedChest = Items.FindBySerial( lockedChestSerial )
                
    Player.HeadMessage( colors[ 'cyan' ], 'Starting chest unlock!' )
    
    Journal.Clear()
    while not ( Journal.SearchByName( 'The lock quickly yields to your skill.', '' ) or
            Journal.SearchByType( 'This does not appear to be locked.', 'Regular' ) ):
        Items.UseItem( lockpicks )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( lockedChest )
        Misc.Pause( 4000 )
        Misc.Pause( config.journalEntryDelayMilliseconds )

        lockpicks = Items.FindByID(0x14FC, -1, Player.Backpack.Serial)
        if lockpicks == None:
            Player.HeadMessage( colors[ 'red' ], 'Ran out of lockpicks!' )
            return

def itemid(item):
    Player.UseSkill( 'Item ID' )
    Target.WaitForTarget( 2000, True )
    Target.TargetExecute( item )

    # Wait for skill cooldown
    Misc.Pause( 1200 )

    while Journal.SearchByType( 'You are not certain...', 'Regular' ):
    # Failed to ID the item, keep trying until we succeed
        Journal.Clear()
        Player.UseSkill( 'Item ID' )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( item )
        # Wait for the skill cooldown
        Misc.Pause( 1200 )
    #textInSystem = Journal.GetTextByType( 'System' )
    keepItem = False
    textInSystem = Journal.GetTextByType( 'System' )
    for itemQuality in itemQualityToKeep:
        if itemQuality in textInSystem:
            return True
    return False


def complexloot(chest,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll):   
    Player.HeadMessage(54, 'test')
    sourceBoxItem = Items.FindBySerial( chest ) 
    
    for item in sourceBoxItem.Contains:
        Journal.Clear( )
        if item.IsContainer:
            Items.UseItem( item )
            Misc.Pause(1000)
            if Journal.Search("locked")== True:
                lockpickchest(item)
                Misc.Pause(3000)
                Items.UseItem( item )
                while Player.Hits < Player.HitsMax:
                    Spells.CastMagery('Greater Heal', True)
                    Target.WaitForTarget(1500)
                    Target.Self()
            if ischestempty(item.Serial) == True:
                Player.HeadMessage(54, 'empty')
                MoveItem( Items, Misc, item, trash )
            else:
                Player.HeadMessage(54, "got a container")
                baseloot(item.Serial,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll )
                complexloot(item.Serial,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll)        
        else:
            if itemid(item):
                MoveItem( Items, Misc, item, savechest )
            else:
                MoveItem( Items, Misc, item, Player.Backpack.Serial )
                caststr()
                if Player.Weight > 400:
                    return

def processloot(person):
    checkregs()
    if havemount() == None:
        stablebeetle()
    if person == 'nox':
        sortchest = 0x4301B201
        regchest = 0x41B89F04
        goldchest = 0x446A206D
        dropchest = 0x41D5D5E7 
        savechest = 0x41DECA82
        trash = 0x4390AC6A
        mapchest = 0x4128E921
        skillscroll= 0x42AF801F
        gohome()
    if person == 'dark':
        sortchest = 0x423C6C84
        regchest = 0x421B8131
        goldchest = 0x421B8131
        dropchest = 0x421B8131 
        savechest = 0x421B8131
        trash = 0x4033EAD2
        mapchest = 0x421B8131
        skillscroll= 0x421B8131        
        setdark()
    if person == 'tmap':
        sortchest = 0x42215FC3
        regchest = 0x4038C235
        goldchest = 0x408E9598
        dropchest = 0x41A1D393 
        savechest = 0x41018DD5
        trash = 0x40DA7B22
        mapchest = 0x4051491E
        skillscroll= 0x4051491E        
        settmap()   
        
    webhook('Process Loot')
    Items.UseItem( sortchest )
    Misc.Pause(1000)
    if ischestempty(sortchest):
        Player.HeadMessage(54, 'chest empty')
        return
    else:
        baseloot(sortchest,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll)
        complexloot(sortchest,regchest,goldchest,dropchest,savechest,trash,mapchest,skillscroll)
    sellshit()
    if person == 'nox':    
        gohome()
    if person == 'dark':    
        setdark()
    if person == 'tmap':
        Player.HeadMessage(54, 'tmap')
        settmap()     
    mountdismountbeetle()
    Misc.Pause(1000)
    beetle = Mobiles.FindBySerial( mountID )
    itemcount = Items.ContainerCount(beetle.Backpack.Serial, 0x0EED, -1) 
    webhook('I deposited ' + str(itemcount) + ' gold')
    while Items.FindByID(0x0EED,-1, beetle.Backpack.Serial):
        moveitem = Items.FindByID(0x0EED,-1, beetle.Backpack.Serial)
        Items.Move(moveitem, goldchest, 0)
        Misc.Pause(750)        
    mountdismountbeetle()
    Items.UseItem( sortchest )
    Misc.Pause(1000)
    if ischestempty(sortchest) == True:
        webhook('done sorting chest is empty')    
    else:
        processloot(person)

def settmap(): 
    if str(Player.Position) != '(6925, 2490, 28)':    
        recall(book[6],15)
    Misc.Pause(1000)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Misc.Pause(2000)
    Player.Walk("North")
    Misc.Pause(2000)
    if str(Player.Position) != '(6925, 2490, 28)':
        settmap()
        webhook("failed to get to tmaps")
    else:
        webhook("I am ready at tmaps")
    

    
        
def worldSave():
    if Journal.SearchByType('The world will save in 1 minute.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(500)
        Misc.Pause(2500)
        Misc.SendMessage('Continuing run', 33)
        Journal.Clear()

def checkforgate():
    moongates = FindMoongates( Items )
    if len( moongates ) >0 :        
        return True
    else:
        return False
        
def healbot():
    deadfilter = Mobiles.Filter()
    deadfilter.Enabled = True
    deadfilter.RangeMax = 2
    deadfilter.IsHuman = True 
    deadfilter.IsGhost = True
    deadppl = Mobiles.ApplyFilter(deadfilter )
    for ghost in deadppl:
        Spells.CastMagery( 'Resurrect' )
        Misc.Pause(1500)
        Target.TargetExecute(ghost)
        



def mountdismountbeetle(): #mounts or dismounts and opens beetle bag    
    if Player.Mount:
        Mobiles.UseMobile(Player.Serial)
        Misc.Pause(500)
        #Mobiles.SingleClick(mountID)
        if mountID != None:
            Misc.WaitForContext(mountID, 1500)
            Misc.ContextReply(mountID, "Open Backpack")
    elif mountID != None:
        Mobiles.UseMobile(mountID)

def grabgold():
    goldfilter = Items.Filter()
    goldfilter.OnGround = True
    goldfilter.Movable = True
    goldfilter.RangeMax = 2
    goldpiles = Items.ApplyFilter(goldfilter)
    mountdismountbeetle()
    for gold in goldpiles: # Look for items in filter
        if gold.ItemID == 0x0EED: # Return true if found a gold pile
            Misc.Pause(500)
            Items.Move(gold, mountID, 0) # dragtobeetle
            Misc.Pause(750)
    Misc.Pause(750)
    
    while Items.FindByID(0x0EED,-1, Player.Backpack.Serial):
        moveitem = Items.FindByID(0x0EED,-1, Player.Backpack.Serial)
        Items.Move(moveitem, mountID, -1)
        Misc.Pause(750)    
    mountdismountbeetle()
    
    
    
    
def stablebeetle(): #stables or unstables beetle
    recall(book[5],3)
    if Player.Mount:
        mountdismountbeetle()
        Misc.Pause(500)  
        Player.ChatSay(52, "stable")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(mountID)    
    else:
        Player.ChatSay(52, "claim asd")
        Gumps.WaitForGump(4108390903, 10000)
        Gumps.SendAction(4108390903, 1)
        Gumps.WaitForGump(2808389811, 10000)
        Gumps.SendAction(2808389811, 0)
        Misc.Pause(200)
        mountdismountbeetle()
        
def havemount():
    if Player.Mount == None:
        if Mobiles.FindBySerial(mountID)== None:
            return False
        else:
            Mobiles.UseMobile(mountID)
            return True
    else:
        return True

    
    
        
def smithsell(): #context sells whats in the agent to moonglow smiths
    webhook('heading to smith shop')
    Misc.Pause(1000)
    recall(book[5],2)
    Misc.WaitForContext(0x0021EE36, 10000)
    Misc.ContextReply(0x0021EE36, 2)
    Misc.Pause(750)
    Misc.WaitForContext(0x0021F01C, 10000)
    Misc.ContextReply(0x0021F01C, 2)
    Misc.Pause(750)
    Misc.WaitForContext(0x0021EE82, 10000)
    Misc.ContextReply(0x0021EE82, 2)
    Misc.Pause(750)
    Misc.WaitForContext(0x0021EE36, 10000)
    Misc.ContextReply(0x0021EE36, 2)
    Misc.Pause(750)
    Misc.WaitForContext(0x0021F01C, 10000)
    Misc.ContextReply(0x0021F01C, 2)
    Misc.Pause(750)
    Misc.WaitForContext(0x0021EE82, 10000)
    Misc.ContextReply(0x0021EE82, 2)
    Misc.Pause(750)


def ischestempty(sourceBox):
    sourceBox = sourceBox
    sourceBoxItem = Items.FindBySerial( sourceBox )

    Items.UseItem( sourceBox )
    Misc.Pause( config.dragDelayMilliseconds )   
    x = 0        
    for item in sourceBoxItem.Contains:
        x=x+1
    if x == 0:
        return True
    else:
        return False
            
    
def loaditems(sourceBox, targetBox): #loads ALL items in a chest into backpack
    sourceBoxItem = Items.FindBySerial( sourceBox )
    if sourceBoxItem == None:
        sourceBox = Mobiles.FindBySerial( sourceBox ).Backpack
    else:
        sourceBox = sourceBoxItem

        targetBoxItem = Items.FindBySerial( targetBox.Serial )
    if targetBoxItem == None:
        targetBox = Mobiles.FindBySerial( targetBox ).Backpack
    else:
        targetBox = targetBoxItem


    Items.UseItem( sourceBox )
    Misc.Pause( config.dragDelayMilliseconds )
    Items.UseItem( targetBox )
    Misc.Pause( config.dragDelayMilliseconds )
            
    for item in sourceBoxItem.Contains:
        if item.IsContainer:
            if ischestempty(item.Serial) == True:
                MoveItem( Items, Misc, item, targetBox )
            else:
                Player.HeadMessage(54, "got a container")
                loaditems(item.Serial,Player.Backpack)        
        else:
            MoveItem( Items, Misc, item, targetBox )
            caststr()
            if Player.Weight > 400:
                return
        
        
def amidead():
    if Player.IsGhost == True:
        webhook('Im dead - Help')

def smithbods():
    abortcounter = 0
    webhook('Getting smith Bod')   
    castincog()
    recall(book[5],0)
    while not Gumps.HasGump():
        abordcounter = abortcounter +1
        if abortcounter > 25:
            gohome()
        if Items.FindByID(tongs, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x00029397, 10000) #sell 
            Misc.ContextReply(0x00029397, 3)
        else:
            Misc.WaitForContext(0x00029397, 10000)
            Misc.ContextReply(0x00029397, 2)
            Misc.Pause(1000)
    while Items.FindByID(tongs, -1, Player.Backpack.Serial):
        Misc.WaitForContext(0x00029397, 10000) #sell 
        Misc.ContextReply(0x00029397, 3)
            
    
    Gumps.WaitForGump(3188567326, 2000)
    Gumps.SendAction(3188567326, 1)
    Gumps.WaitForGump(2611865322, 2000)
    Gumps.SendAction(2611865322, 1)
    tailorbods()
   

def tailorbods():
    webhook('Getting Tailor Bod')
    abortcounter = 0    
    recall(book[5],1)
    while not Gumps.HasGump():
        abordcounter = abortcounter + 1
        if abortcounter > 25:
            gohome()
        if Items.FindByID(sewingkit, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x0024A965, 10000)
            Misc.ContextReply(0x0024A965, 3)
            Misc.Pause(750)
        else:
            Misc.WaitForContext(0x0024A965, 10000)
            Misc.ContextReply(0x0024A965, 2)
            Misc.Pause(1000)
    while Items.FindByID(sewingkit, -1, Player.Backpack.Serial):
        Misc.WaitForContext(0x0024A965, 10000)
        Misc.ContextReply(0x0024A965, 3)
        Misc.Pause(750)   
        
    Gumps.WaitForGump(3188567326, 2000)
    Gumps.SendAction(3188567326, 1)
    Gumps.WaitForGump(2611865322, 2000)
    Gumps.SendAction(2611865322, 1)
    Misc.Pause(2000)
    gohome()
    x = Items.FindByID(0x14EF, 0x0483, Player.Backpack.Serial)
    Items.UseItem(x)
    Misc.Pause(1000)
    webhook('XXXXXXXXXXXX TAILOR BODS XXXXXXXXXXXXXXXX')
    XX = Gumps.LastGumpGetLine(6)+'\n' + Gumps.LastGumpGetLine(4)+'\n' +Gumps.LastGumpGetLine(9)
    webhook(XX)
    Gumps.SendAction(1526454082, 0)
    Misc.Pause(1000)
    
    y = Items.FindByID(0x14EF, 0x044E, Player.Backpack.Serial)
    Items.UseItem(y)
    Misc.Pause(1000)
    webhook('XXXXXXXXXXXX SMITH BODS XXXXXXXXXXXXXXXX')
    YY = Gumps.LastGumpGetLine(6)+'\n' + Gumps.LastGumpGetLine(4)+'\n'+Gumps.LastGumpGetLine(7)+'\n'+Gumps.LastGumpGetLine(10)
    webhook(YY)
    Misc.Pause(500)
    Gumps.SendAction(1526454082, 0)
    Misc.Pause(500)

    
    
    homeunload(0x14EF, 0x0483) #tailor bods
    homeunload(0x14EF, 0x044E) #smith bods
        
        
def recall(book, rune):
    mana(30)
    rune = 5+6*rune
    currentlocation = Player.Position
    while currentlocation == Player.Position:
        Misc.Pause( 250 )
        Items.UseItem(book)
        Gumps.WaitForGump( 1431013363, 5000 )
        Misc.Pause( 250 )
        Gumps.SendAction( 1431013363, rune )
        caststr()
        Misc.Pause( 500 )
    
def buyarrows():
    webhook('Buying arrows please stand by')
    checkregs()
    arrowqty = 0
    cost = 0
    VendorFilter = Mobiles.Filter()
    VendorFilter.RangeMax = 12
    VendorFilter.Name = 'Provisioner'
    rune = 0
    while rune < 15:
        castincog()
        caststr()
        recall(book[4], rune)
        rune=rune+1
        VendorFilters = Mobiles.ApplyFilter( VendorFilter )
        for vendor in VendorFilters:
            Mobiles.SingleClick( vendor.Serial )
            Misc.WaitForContext( vendor.Serial, 10000 )
            Misc.Pause( 200 )
            Misc.ContextReply( vendor.Serial, 1 )
            Misc.Pause( 500 )
    recall(0x463FCD14, 14) #Recall to bank  
    movetobank(arrows)
    arrowqty = Items.ContainerCount(Player.Bank.Serial, arrows, -1) 
    webhook('I Purchased ' + str(arrowqty)+' arrows')
    cost = arrowqty *3
    webhook('Total price: ' + str(cost)+' gold')      
    deedstack(arrows, 1000)
    gohome()
    homeunload(0x14F0, 0x0A66) #pink commodity deed
    
    
def homeunload(item, color): #unload athome
    while Items.FindByID(item, color, Player.Backpack.Serial): #looks passed item in mag
        currenttarget = Items.FindByID(item, color, Player.Backpack.Serial)
        Items.Move(currenttarget, unload, -1) 
        Misc.Pause(1000)

def movetobank(item): 
    Player.ChatSay(57,'Bank')
    Misc.Pause(500)   
    bank = Player.Bank.Serial
    while Items.FindByID(item, -1, Player.Backpack.Serial):
        targetitem = Items.FindByID(item, -1, Player.Backpack.Serial)
        Items.Move(targetitem, bank , -1)
        Misc.Pause(1000)
        
def movefrombank(item, color): 
    Player.ChatSay(57,'Bank')
    Misc.Pause(500)   
    bank = Player.Bank.Serial
    while Items.FindByID(item, color, Player.Bank.Serial):
        targetitem = Items.FindByID(item, color, Player.Bank.Serial)
        Items.Move(targetitem, Player.Backpack.Serial , -1)
        Misc.Pause(1000)    
        
def deedstack(item, count): #item type and minimum qty to deed
    targetitem =  Items.FindByID(item, -1, Player.Bank.Serial)       
    itemcount = Items.ContainerCount(Player.Bank.Serial, item, -1) 
    if itemcount >= count: #if qty in bank is more than min qty proceed with deeding
            Player.HeadMessage(54,"marker1")
            VendorFilter = Mobiles.Filter()
            VendorFilter.RangeMax = 12
            VendorFilter.Name = 'Banker'
            VendorFilters = Mobiles.ApplyFilter( VendorFilter )
            for vendor in VendorFilters: #buy deeds
                if Items.BackpackCount(0x14F0,0x0047)==0 and Items.ContainerCount(Player.Bank.Serial, 0x14F0, 0x0047) == 0: #if no deeds in bag continue
                    Mobiles.SingleClick( vendor.Serial )
                    Misc.WaitForContext( vendor.Serial, 10000 )
                    Misc.ContextReply( vendor.Serial, 3 )
                    Misc.Pause( 1000 )
    movetobank(0x14F0) #move deed to bank
    Misc.Pause(750)    
    deed = Items.FindByID(0x14F0, 0x0047, Player.Bank.Serial) #find serial for deed in bank         
    Items.UseItem(deed)
    Target.WaitForTarget(5000)
    Target.TargetExecute(targetitem)
    Misc.Pause(1000)
    movefrombank(0x14F0, 0x0A66) #move pink full commodity deeds from bank to bag
    Misc.Pause(1000)

    
def webhook(msg):
    URI = 'https://discordapp.com/api/webhooks/654131394854781018/KySfeUnLjoFmqfmf154_1V22nxkzGnDmOP6-j8Kj__Ei8boMeHwzir6irC57rIY65_6q'
    alert = msg
    report = "content="+ alert
    PARAMETERS=report
    from System.Net import WebRequest
    request = WebRequest.Create(URI)
    request.ContentType = "application/x-www-form-urlencoded"
    request.Method = "POST"
    from System.Text import Encoding
    bytes = Encoding.ASCII.GetBytes(PARAMETERS)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()
    response = request.GetResponse()
    from System.IO import StreamReader
    result = StreamReader(response.GetResponseStream()).ReadToEnd().replace('\r', '\n')

def mana(mana_req):
    if Player.Mana < mana_req:
        Player.UseSkill( 'Meditation' )
        while Player.Mana < ( Player.ManaMax ):
            Misc.Pause( 50 )

def castincog():
    if Player.BuffsExist('Incognito'):
        Player.HeadMessage(54,'incog already on')
    else:
        Spells.CastMagery( 'Incognito' )
        Misc.Pause(1500)
def setnox():
    recall(book[3],0)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Misc.Pause(1000)
    if str(Player.Position) != '(6939, 2486, 75)':
        gohome()
        webhook("failed to go home")
    else:
        webhook("I am at Nox's")

def setdark():
    recall(book[3],15)
    Player.Run("North")
    Misc.Pause( 100) 
    Player.Run("North")
    Misc.Pause( 100) 
    Player.Run("North")
    Misc.Pause( 100) 
    Player.Run("North")
    Misc.Pause( 100) 
    Player.Run("North")
    Misc.Pause( 100) 
    Player.Run("North")
    if str(Player.Position) != '(1883, 438, 27)':
        setdark() 
        webhook("failed to get to dark's")
    else:
        webhook("I am setup at dark's")
        
    
def gohome():
    if str(Player.Position) == '(6939, 2486, 75)':
        webhook('home already')
        return  
    recall(book[3],0)
    Misc.Pause(500)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Misc.Pause(2000)
    if str(Player.Position) != '(6939, 2486, 75)':
        webhook("failed to go home")    
        gohome()        
    else:
        webhook("I am at home")
        
def caststr():
    if Player.Weight > 375 and not Player.BuffsExist( 'Strength' ):
            Spells.CastMagery( 'Strength' )
            Target.WaitForTarget( 10000, False )
            Target.Self()
            Misc.Pause( 1000 )
            
def getbalance():
    Player.ChatSay( 58, 'Balance' )
    Misc.Pause(1000)
    if Journal.Search("balance")== True: 
        a = Journal.GetLineText("balance is")
        balance = a.replace('Thy current bank balance is ', '')
        balance = balance.replace(' Gold.',"")
        balance = balance.replace(',',"")
        balance= int(balance)


def regcount():
    webhook('Pearl: ' + str(Items.BackpackCount(0x0F7A,0)) +'/Root: ' + str(Items.BackpackCount(0x0F86,0)) + '/Moss: ' + str(Items.BackpackCount(0x0F7B,0)) + '/Sulf: ' + str(Items.BackpackCount(0x0F8C,0)) + '/Gar: ' + str(Items.BackpackCount(0x0F84,0)) + '/Gin: ' + str(Items.BackpackCount(0x0F85
    ,0))+'/Silk: ' + str(Items.BackpackCount(0x0F8D,0)) + '/Shade: ' + str(Items.BackpackCount(0x0F88,0))            )

    
def checkregs():
    #if Items.BackpackCount(0x0F7A,0) <50 or Items.BackpackCount(0x0F86,0) <50 or Items.BackpackCount(0x0F7B,0) < 50 orItems.BackpackCount(0x0F8C,0) < 50 or Items.BackpackCount(0x0F84,0) <50 or Items.BackpackCount(0x0F85,0)<50 or Items.BackpackCount(0x0F8D,0) <50 orItems.BackpackCount(0x0F88,0):
     for reg in regs:
         if Items.BackpackCount(reg,0)<50:
            restock()
    
    
def hopgate():
    moongates = FindMoongates( Items )
    if len( moongates ) > 0:
      moongate = Items.Select( moongates, 'Nearest' )
      Items.UseItem( moongate )

      Gumps.WaitForGump( 3716879466, 2000 )
      Gumps.SendAction( 3716879466, 1 )

def restock():
    webhook('Need Regs')
    gate(book[3], rune[0]) 
    hopgate()
    Misc.Pause(1500)
    Mobiles.UseMobile(0x000E0470)
    Gumps.WaitForGump(989312372, 10000)
    Gumps.SendAction(989312372, 8)
    Misc.Pause(500)
    hopgate()
    Misc.Pause(1000)
    regcount()
    Misc.Pause(1000)
    
    
def gate(book, rune):
        gatefilter = Items.Filter()
        gatefilter.Enabled = True
        gatefilter.OnGround = True
        gatefilter.Movable = False
        gatefilter.RangeMax = 1.5
        mana(60)
        Items.UseItem(book)
        Gumps.WaitForGump(1431013363, 10000)
        Gumps.SendAction(1431013363, rune)
        Misc.Pause(2750)
        moongate = Items.ApplyFilter(gatefilter)
        z=0
        for m in moongate:
            if m.ItemID == 0x0F6C:
                z=z+1
        if z ==1:
            webhook("Gate is up")
        else:
            webhook("Fizzle")
            Misc.Pause(1500)
            gate(book, rune)
            
    
lastcomment = "start"

x = 2

while x > 1:
    
    amidead()
    f = open('C:/Users/Jason/Desktop/bottest.txt', 'r')

    bodtimer = bodtimer +1

    if bodtimer == 18000:
        webhook('Bod Timer hit 18000')
        bodtimer=0
        smithbods()
    for line in f:    
        #Player.ChatSay( 58,line )
        Misc.Pause(1)
    if line != lastcomment:
        if line == '!gate abyss e\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[0])
        if line == '!gate abyss w\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[1])    
        if line == '!gate cove\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[2])
        if line == '!gate deciet n\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[3])
        if line == '!gate deciet s\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[4])
        if line == '!gate despise w\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[5])
        if line == '!gate despise e\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[6])        
        if line == '!gate destard n\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[7])
        if line == '!gate shame n\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[8])    
        if line == '!gate shame s\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[9])
        if line == '!gate terra n\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[10])
        if line == '!gate terra s\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[11])
        if line == '!gate oaks\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[12])   
        if line == '!gate water\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[13])
        if line == '!gate double\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[14])
        if line == '!gate orc\n':
            Player.ChatSay( 58,line )
            gate(book[1], rune[15])
#=============================================================
        if line == '!gate bucs\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[0])
        if line == '!gate cove\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[1])    
        if line == '!gate cursed fortress\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[2])
        if line == '!gate deciet\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[3])
        if line == '!gate despise\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[4])
        if line == '!gate destard\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[5])
        if line == '!gate fire\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[6])        
        if line == '!gate hyloth\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[7])
        if line == '!gate ice\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[8])    
        if line == '!gate khaldun\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[9])
        if line == '!gate orc cave\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[10])
        if line == '!gate shame\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[11])
        if line == '!gate spider cave\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[12])   
        if line == '!gate terra\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[13])
        if line == '!gate wind\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[14])
        if line == '!gate wrong\n':
            Player.ChatSay( 58,line )
            gate(book[0], rune[15])             
#==================================================
        if line == '!gate dark\n':
            Player.ChatSay( 58,line )
            gate(book[3], rune[15]) 
        if line == '!gate jer\n':
            Player.ChatSay( 58,line )
            gate(book[3], rune[7]) 
        if line == '!gate nox\n':
            Player.ChatSay( 58,line )
            gate(book[3], rune[0]) 
#==================================================
        if line == '!gate brit\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[0])
        if line == '!gate brit e\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[1])    
        if line == '!gate bucs den\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[2])
        if line == '!gate cove bank\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[3])
        if line == '!gate jhelom\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[4])
        if line == '!gate minoc\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[5])
        if line == '!gate moonglow\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[6])        
        if line == '!gate new magencia\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[7])
        if line == '!gate nujelm\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[8])    
        if line == '!gate ocllo\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[9])
        if line == '!gate serp\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[10])
        if line == '!gate trin e\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[11])
        if line == '!vesper\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[12])   
        if line == '!gate wind\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[13])
        if line == '!gate yew\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[14])
        if line == '!gate skara\n':
            Player.ChatSay( 58,line )
            gate(book[2], rune[15])
       #======================= REG COUNT ================
        if line == '!regcount\n':
            regcount()
        if line == '!restock\n':
            restock()
        #======================
        if line == '!buyarrows\n':
            buyarrows()
        if line == '!getbods\n':    
            smithbods()
        if line == '!setnox\n':
            setnox()
        if line == '!setdark\n':
            setdark()
        if line == '!timearrows\n':
            webhook(str(arrowtimer)+' seconds since last run' )
        if line == '!timebods\n':
            webhook(str(bodtimer)+' seconds since last run' )
        if line == '!darkloot\n':
            processloot('dark')
        if line == '!noxloot\n':
            processloot('nox')
        if line == '!tmaploot\n':
            processloot('tmap')
            
            
     
    lastcomment = line
    Misc.Pause(1000)

        
    #Mobiles.UseMobile(0x0019544B)