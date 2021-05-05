#Mysticism Spellbook Crafter by Frank Castle
#
# Instructions:
#
# Have plenty of Exceptional Scribes Pens with makers mark on them
# Have GM Inscription.  It just makes it easier.
# Have a resource container with plenty of scrolls and regs
# Have at least 100 mana
# Have a trash can within reach
# Have your Mysticism spellbook in your hand.  Do not have any other Mysticism spellbooks in your backpack.
# Having Meditation and a Mana Regen suit is recommended, but not necessary. 


from System.Collections.Generic import List

mandrakeroot = 0x0F86
bloodmoss = 0x0F7B
sulphurousash = 0x0F8C
nightshade = 0x0F88
blackpearl = 0x0F7A
spidersilk = 0x0F86
ginseng = 0x0F85
garlic = 0x0F84
stoCont = Target.PromptTarget('Target your Storage Container')
Items.UseItem(stoCont)
Misc.Pause(2000)

bookBag = Target.PromptTarget('Target your BookBag')
Items.UseItem(stoCont)
Misc.Pause(2000)

regsList = [0x0F86,0x0F7B,0x0F8C,0x0F88,0x0F7A,0x0F8D,0x0F85,0x0F84,0x0EF3,0x0F80,0x0F81,0x0F7E,0x4077]
mystScrollList = [0x2D9E,0x2D9F,0x2DA0,0x2DA1,0x2DA2,0x2DA3,0x2DA4,0x2DA5,0x2DA6,0x2DA7,0x2DA8,0x2DA9,0x2DAA,0x2DAB,0x2DAC,0x2DAD]
global pen
pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

GFilter = Items.Filter()
GFilter.RangeMax = 5
GFilter.OnGround = True
GFilter.Enabled = True
GFilter.Movable = True
garbagecan = List[int]((0x0E77, 0x0E77))  
GFilter.Graphics = garbagecan

def getSupplies():
    for i in regsList:
        if Items.BackpackCount(i,-1) < 30:
            reg = Items.FindByID(i,-1,stoCont)
            Misc.Pause(500)
            Items.Move(reg,Player.Backpack.Serial,100)
            Misc.Pause(1100)
            
def makeSpellbook():
    getSupplies()
    Items.UseItem(pen)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 206)
    Misc.Pause(3000)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    if not spellbook:
        makeSpellbook()
        
def checkPen():
    curCharges = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
    Items.WaitForProps(curCharges,2000)
    props = Items.GetPropStringList(curCharges.Serial)
    Misc.Pause(500)
    prop = props[3].split(' ')[2]
    Misc.SendMessage(prop)
    Misc.Pause(500)
    if int(prop) < 20:
        global pen
        garbagecans = Items.ApplyFilter(GFilter)
        Misc.Pause(500)
        garbagecan = Items.Select(garbagecans, 'Nearest')
        Misc.Pause(500)
        Items.Move(pen,garbagecan,0)
        Misc.Pause(1100)
        checkPen()
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
      
mystScrollList = [0x2D9E,0x2D9F,0x2DA0,0x2DA1,0x2DA2,0x2DA3,0x2DA4,0x2DA5,0x2DA6,0x2DA7,0x2DA8,0x2DA9,0x2DAA,0x2DAB,0x2DAC,0x2DAD]
    
def makeNetherBolt():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 678)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2D9E,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeNetherBolt()
        
def makeHealingStone():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 679)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2D9F,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeHealingStone()
        
def makePurgeMagic():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 680)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA0,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makePurgeMagic()
        
def makeEnchant():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 681)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA1,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeEnchant()            

def makeSleep():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 682)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA2,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeSleep()        
        
def makeEagleStrike():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 683)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA3,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeEagleStrike()
        
def makeAnimatedWeapon():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 684)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA4,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeAnimatedWeapon()

def makeStoneForm():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 685)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA5,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeStoneForm() 
 
def makeSpellTrigger():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 686)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA6,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeSpellTrigger()

def makeMassSleep():
    getSupplies()
    checkPen()
    checkMana(14)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 687)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA7,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeMassSleep()
        
def makeCleansingWinds():
    getSupplies()
    checkPen()
    checkMana(20)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 688)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA8,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeCleansingWinds()

def makeBombard():
    getSupplies()
    checkPen()
    checkMana(20)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 689)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DA9,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeBombard()        

def makeSpellPlague():
    getSupplies()
    checkPen()
    checkMana(40)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 690)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DAA,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeSpellPlague()

def makeHailStorm():
    getSupplies()
    checkPen()
    checkMana(50)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 691)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DAB,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeHailStorm()

def makeNetherCyclone():
    getSupplies()
    checkPen()
    checkMana(50)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 692)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DAC,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeNetherCyclone()

def makeRisingColossus():
    getSupplies()
    checkPen()
    checkMana(50)
    Items.UseItem(pen)
    Misc.Pause(1100)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 693)
    Misc.Pause(2000)
    scroll = Items.FindByID(0x2DAD,-1,Player.Backpack.Serial)
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    if scroll:
        Items.Move(scroll,spellbook,1)
        Misc.Pause(1100)
    else:
        makeRisingColossus()

        
def checkMana(mana):
    while Player.Mana < mana:
        Player.UseSkill('Meditation')
        Misc.Pause(11500)
            

        
def makeBook():
    while Player.Mana < Player.ManaMax :
        Player.UseSkill('Meditation')
        Misc.Pause(10000)
    makeSpellbook()
    makeNetherBolt()
    makeRisingColossus()
    makeHealingStone()
    makeNetherCyclone()
    makePurgeMagic()
    makeHailStorm()
    makeEnchant()
    makeSpellPlague()
    makeSleep()
    makeBombard()
    makeEagleStrike()
    makeCleansingWinds()
    makeAnimatedWeapon()
    makeMassSleep()
    makeStoneForm()
    makeSpellTrigger()
    spellbook = Items.FindByID(0x2D9D,-1,Player.Backpack.Serial)
    Misc.Pause(200)
    Items.Move(spellbook,bookBag,0)

while True:
    makeBook()    
            



    
    
