from Scripts.utilities.items import MoveItem
from Scripts import config
from Scripts.glossary.colors import colors
from Scripts.glossary.items.moongates import FindMoongates
from Scripts.utilities.items import FindNumberOfItems
from Scripts.glossary.items.spellScrolls import spellScrolls


### GLOBALS
bankbalance = 0
bankregbalance = 0
regbalance = 0
supplybalance=0
vendorbalance = 0
totalgold = 0
arrowtimer = 0



####VENDORS
flutevendor = 0x00238962
flutevendorbag = 0x4449D087
bottlevendor = 0x002431A3
bottlevendorbag = 0x445A6400
arrowvendor = 0x00248DCE
arrowvendorbag = 0x44632678
slayervendor= 0x0024E426
slayervendorbag=0x446D32FD
spiderslayerbag = 0x446CE2BC
elementalslayerbag = 0x446CE2B8
exoslayerbag = 0x446CE2B9
feyslayerbag = 0x446CE2BB
repondslayerbag =0x446CE2BA
reptslayerbag =  0x446CE2B7
silverslayerbag =0x403FB48B
armorvendor = 0x0024ED8F
armorvendorbag = 0x446E9B89
trappedboxvendor=0x00259949
trappedboxvendorbag=0x4481A341
kegvendor=0x000AFAE1
kegvendorbag=0x41473081 
regvendor= 0x0012FEED
regvendorbag= 0x424A9332
kegcolors = [0x012A, 0x03DF ,0x002B, 0x0035, 0x0085, 0x0012,0x0040] #blue, grey, orng, yellow,red ,purple,gree
scribevendor = 0x000D46F2
weaponvendor = 0x0013013E
ingotvendor= 0x001DCF58
ingotvendorbag=0x437EA764
woodvendor = 0x001DE42C
woodvendorbag = 0x43811640

####TOOLS
tinktool=0x1EB8
sawmodel=0x1034
tongs = 0x13BB
sewingkit=0x0F9D

###CONSTANTS

flute = 0x2805
kegmodel = 0x1940
arrows = 0x0F3F
bottles = 0x0F0E
deeds= 0x14F0
slayerdeeds = [0x14F0,0x07AC]
traps = 0x0E7E #trapped boxes 
scalearmor = [0x2645,0x2657,0x2B69, 0x2643, 0x2641,0x2647]
leatherarmor = [0x1DB9,0x13C7,0x13CD,0x13C6,0x13CC,0x13CB]


#materials
ingotmodel = 0x1BF2
ingotcolor = 0x0000
dullcolor = 0x0415 
shadowcolor = 0x0455
coppercolor = 0x045F
bronzecolor = 0x06D8
goldcolor = 0x06B7
aggycolor = 0x097E
vercolor = 0x07D2
valcolor = 0x0544

wood = 0x1BDD
regwoodcolor = 0x0000
frostwoodcolor = 0x047F
bloodwoodcolor = 0x04AA
heartwoodcolor = 0x04A9




###CHESTS
bankbox = 0x41006888
flutetrash = 0x442CCB42
woodchest = 0x4083A7E1
ingotchest = 0x448B879A
regchest = 0x4079777D

emptykegchest = 0x4557B998
expkegchest = 0x453435AC
strengthkegchest = 0x453435AA
refreshkegchest = 0x453435AD
agilitykegchest = 0x453435A8
healkegchest = 0x453435AF
curekegchest = 0x453435AB
poisonkegchest = 0x4557B99C

arachniddeedchest = 0x40D34D30
elementaldeedchest = 0x40D34D2E
exorcismdeedchest = 0x40D34D2D
feydeedchest = 0x40D34D32
reponddeedchest =0x411837F6
reptiliandeedchest = 0x40D34D31
silverdeedchest = 0x40D34D2C

scalearmorchest = [0x43FF3581,0x456F0458, 0x40FB7C82, 0x4474AD24, 0x4589A0F6, 0x444C6744]
leatherarmorchest = [0x4058CC07, 0x4058CC29, 0x4058A30C, 0x4058A317, 0x4058A321,0x4058A326]




 






###Prices
fluteprice = 500
bottleprice = 6



gumppause = 1000
arrowtimer = 0
crafterbodtimer = 0
balance = 0

unload = 0x41B89F04 #commpdity deed box at home to dump shit in

mountID = 0x001BF818#beetle ID

regs = [0x0F7A, 0x0F86, 0x0F7B, 0x0F8C, 0x0F84, 0x0F85, 0x0F8D, 0x0F88]

rune = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96] #only works with gate

book = [0,1,2,3,4,5]

book[0] = 0x463D089E # 0 home
book[1] = 0x40B36704  # 1 bods
book[3] = 0x41BE5981 #mageshops
book[4] =  0x41BE561B #provo

# TOKEN = "NjUzNjg5OTUxMjc5MzgyNTQ5.Xe6qlA.NfKouSl1uliWCF98dkveblTStT0"


def fetchsmithstation(fetchbag, fetchitem, fetchqty):
    webhook('grabbing supplies')
    recall(book[0],14)
    Misc.Pause(750)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Misc.Pause(2000)
    Items.UseItem(fetchbag)
    Misc.Pause(750)
    countqty= Items.ContainerCount(fetchbag, fetchitem, -1)
    if countqty >= fetchqty:
        x = 0
        while x < fetchqty:
            currentmove = Items.FindByID(fetchitem, -1, fetchbag)
            Items.Move(currentmove, Player.Backpack.Serial, -1)
            Misc.Pause(1000)
            x =x +1     
    else:
        webhook('not enough supplies to complete order')
    if str(Player.Position) != '(691, 799, 47)':
        recall(book[0],1)
        Player.Walk("North")
        Player.Walk("North")
        webhook('Moving back to vendor house')
        Misc.Pause(1500)
        hide()
    
def loadvendors(thing2move, vendor, vendorbag, price):
    Mobiles.UseMobile(vendor)
    Misc.Pause(1000)
    while Items.FindByID(thing2move, -1, Player.Backpack.Serial): 
        currentmove = Items.FindByID(thing2move, -1, Player.Backpack.Serial)
        Items.Move(currentmove, vendorbag, -1) 
        Misc.Pause(1000)
        Misc.ResponsePrompt(price)

def stockslayerdeeds():
    stockqty = 5
    if str(Player.Position) != '(691, 799, 47)':
        recall(book[0],1)
        Player.Walk("North")
        Player.Walk("North")
    webhook('Stocking Slayer Deeds')
    Misc.Pause(1500)
    idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
    hide()
    Misc.Pause(1500)
    arachslayercheck = vendorcount(slayervendor, spiderslayerbag , deeds, True)
    if arachslayercheck[1] < stockqty:
        fetchsmithstation(arachniddeedchest , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, spiderslayerbag  , "5000")

    elementalslayercheck = vendorcount(slayervendor, elementalslayerbag , deeds, True)
    if elementalslayercheck[1] < stockqty:
        fetchsmithstation(elementaldeedchest, deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, elementalslayerbag , "5000")
        
    exoslayercheck = vendorcount(slayervendor, exoslayerbag , deeds, True)
    if exoslayercheck[1] < stockqty:
        fetchsmithstation(exorcismdeedchest , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, exoslayerbag  , "5000")
    
    feyslayercheck = vendorcount(slayervendor, feyslayerbag , deeds, True)
    if feyslayercheck[1] < stockqty:
        fetchsmithstation(feydeedchest  , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, feyslayerbag  , "5000")
    
    repondslayercheck = vendorcount(slayervendor, repondslayerbag , deeds, True)
    if repondslayercheck[1] < stockqty:
        fetchsmithstation(reponddeedchest   , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, repondslayerbag   , "5000")    
  
    reptslayercheck = vendorcount(slayervendor, reptslayerbag  , deeds, True)
    if reptslayercheck[1] < stockqty:
        fetchsmithstation(reptiliandeedchest    , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, reptslayerbag    , "5000")
        
    silverslayercheck = vendorcount(slayervendor, silverslayerbag, deeds, True)   
    if silverslayercheck[1] < stockqty:
        fetchsmithstation(silverdeedchest , deeds, stockqty)
        idontknowwhyineedtodothis = vendorcount(slayervendor, spiderslayerbag , deeds, True)
        loadvendors(deeds, slayervendor, silverslayerbag    , "5000")
        
        
        
        
def checkvendors():
    global vendorbalance
    if str(Player.Position) != '(691, 799, 47)':
        recall(book[0],1)
        Player.Walk("North")
        Player.Walk("North")
    webhook('Checking Vendor Status')
    Misc.Pause(1500)
    hide()
    flutecheck = vendorcount(flutevendor, flutevendorbag, flute, False)
    webhook('FLUTES: There is ' + str(flutecheck[0]) + ' gold on the vendor and he has ' + str(flutecheck[1]) + ' flutes in stock')
    bottlecheck = vendorcount(bottlevendor, bottlevendorbag, deeds, False)
    webhook('BOTTLES: There is ' + str(bottlecheck[0]) + ' gold on the vendor and he has ' + str(bottlecheck[1]) + ' deeds' )
    arrowcheck = vendorcount(arrowvendor, arrowvendorbag, deeds, False)
    webhook('ARROWS: There is ' + str(arrowcheck[0]) + ' gold on the vendor and he has ' + str(arrowcheck[1]) + ' deeds' )
    armorcheck = vendorcount(armorvendor, armorvendorbag, 0x0E79, False) #0x0E79 = pouches
    webhook('Armor: There is ' + str(armorcheck[0]) + ' gold on the vendor and he has ' + str(armorcheck[1]) + ' sets of armor' )
    trapcheck = vendorcount(trappedboxvendor, trappedboxvendorbag, traps, False) 
    webhook('Trapped Boxes: There is ' + str(trapcheck[0]) + ' gold on the vendor and he has ' + str(trapcheck[1]) + ' trapped boxes' )
    
    #### KEG VENDOR #####

    bluecount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[0])  
    greycount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[1])
    orgncount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[2])
    yellowcount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[3])
    redcount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[4])
    purplecount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[5])
    greencount = vendorcountkeg(kegvendor, kegvendorbag, kegmodel, kegcolors[6])
    webhook('Kegs: There is ' + str(bluecount[0]) + ' gold on the vendor')
    webhook('Exp: ' + str(purplecount[1]) + ' // Str: ' + str(greycount[1]) + ' // Refresh: ' + str(redcount[1]) + ' // Agility: ' + str(bluecount[1]) + ' // Heal: ' + str(yellowcount[1]) + ' // Cure: ' + str(orgncount[1]) + ' // Poison: '+ str(greencount[1]))
    
    
    
    ##### SLAYER VENDOR #######
    Misc.Pause(1000)
    spiderslayercheck = vendorcount(slayervendor, spiderslayerbag, deeds, True)
        
    elementalslayercheck = vendorcount(slayervendor, elementalslayerbag , deeds, True)
    exoslayercheck = vendorcount(slayervendor, exoslayerbag , deeds, True)
    feyslayercheck = vendorcount(slayervendor, feyslayerbag , deeds, True)
    repondslayercheck = vendorcount(slayervendor, repondslayerbag , deeds, True)
    reptslayercheck = vendorcount(slayervendor, reptslayerbag , deeds, True)
    silverslayercheck = vendorcount(slayervendor, silverslayerbag, deeds, True)    
    webhook('THE SLAYER VENDOR: There is ' + str(silverslayercheck[0]) + ' gold on the vendor')
    webhook('Spider Deeds: ' + str(spiderslayercheck[1])+ '\n' + 'Elemental Deeds: '+ str(elementalslayercheck[1])+ '\n' + 'Exo Deeds: '+ str(exoslayercheck[1])+ '\n' + 'Fay Deeds: '+ str(feyslayercheck[1])+ '\n' + 'Repond Deeds: '+ str(repondslayercheck[1])+ '\n' + 'Reptile Deeds: '+ str(reptslayercheck[1])+'\n' + 'Silver Deeds: '+ str(silverslayercheck[1]))
  
    #### REG VENDOR ######
    Misc.Pause(1000)
    regvendorcheck = vendorcount(regvendor, regvendorbag, 0x14F0, False)  
    webhook('REGS: There is ' + str(regvendorcheck[0]) + ' gold on the vendor and he has ' + str(regvendorcheck[1]) + ' out of 8 deeds' )
    
    #### INGOT VENDOR ######
    Misc.Pause(1000)
    ingotvendorcheck = vendorcount(ingotvendor, ingotvendorbag, 0x14F0, False)  
    webhook('Ingots: There is ' + str(ingotvendorcheck[0]) + ' gold on the vendor and he has ' + str(ingotvendorcheck[1]) + ' out of 9 deeds' )
    
    ### WEAP VENDOR ######
    Misc.Pause(1000)
    weaponvendorcheck = vendorcount(weaponvendor, regvendorbag, 0x14F0, False)  
    webhook('Weapons: There is ' + str(weaponvendorcheck[0]) + ' gold on the vendor')
  
    #### WOOD VENDOR ######
    Misc.Pause(1000)
    woodvendorcheck = vendorcount(woodvendor, woodvendorbag, 0x14F0, False)  
    webhook('Wood: There is ' + str(woodvendorcheck[0]) + ' gold on the vendor and he has ' + str(woodvendorcheck[1]) + ' out of 7 deeds' )
      
    
    
    ### Scribe VENDOR ######
    Misc.Pause(1000)
    scribevendorcheck = vendorcount(scribevendor, regvendorbag, 0x14F0, False)  
    webhook('Scribe: There is ' + str(scribevendorcheck[0]) + ' gold on the vendor')
  
    
    totalgold = 0
    
    temp = flutecheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = bottlecheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = arrowcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = armorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = trapcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = spiderslayercheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = bluecount[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = regvendorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
        
    temp = weaponvendorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    temp = scribevendorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    
    temp = woodvendorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    
    temp = ingotvendorcheck[0].replace(',',"")
    temp = int(temp)
    totalgold = totalgold + temp
    
    
    vendorbalance = totalgold
    totalgoldinthousands = totalgold/1000
    webhook('Gold On Vendors: ' + str(totalgoldinthousands) + 'k')
    


def vendorcount(vendor, bag, item, subbag):
    data = [0,0]
    Mobiles.UseMobile(vendor)
    Misc.Pause(2500)
    if subbag == True:
        Items.UseItem(bag)
        Misc.Pause(1250)        
    data[0] = Gumps.LastGumpGetLine(12)
    Gumps.WaitForGump(797007452, 1000)
    Gumps.SendAction(797007452, 1)
    Misc.Pause(1000)
    data[1] = Items.ContainerCount(bag, item, -1)
    return data
    Misc.Pause(1500)

def vendorcountkeg(vendor, bag, item, color):
    data = [0,0]
    Mobiles.UseMobile(vendor)
    Misc.Pause(2000)
    data[0] = Gumps.LastGumpGetLine(12)
    Gumps.WaitForGump(797007452, 1000)
    Gumps.SendAction(797007452, 1)
    Misc.Pause(1000)
    data[1] = Items.ContainerCount(bag, item, color)
    return data
    Misc.Pause(1500)

    
def buybottles():
    webhook('Buying bottles please stand by')
    checkregs()
    bottleqty = 0
    cost = 0
    VendorFilter = Mobiles.Filter()
    VendorFilter.RangeMax = 12
    
    rune = 0
    while rune < 15:
        castincog()
        caststr()
        recall(book[3], rune)
        rune=rune+1
        VendorFilters = Mobiles.ApplyFilter( VendorFilter )
        for vendor in VendorFilters:
            Mobiles.SingleClick( vendor.Serial )
            Misc.WaitForContext( vendor.Serial, 10000 )
            Misc.Pause( 200 )
            Misc.ContextReply( vendor.Serial, 1 )
            Misc.Pause( 500 )
    recall(book[0], 15) #Recall to bank  
    movetobank(bottles)
    bottleqty = Items.ContainerCount(Player.Bank.Serial, bottles, -1) 
    webhook('I Purchased ' + str(bottleqty)+' bottles')
    cost = bottleqty * bottleprice
    webhook('Total price: ' + str(cost)+' gold')      
    #deedstack(bottles, 5000)
    #Misc.Pause(1000)
    #recall(book[0],1)
    #Mobiles.UseMobile(0x002431A3)
    #Gumps.WaitForGump(797007452, 10000)
    #Gumps.SendAction(797007452, 1)
    #Misc.Pause(500)
    #while Items.FindByID(0x14F0, 0x0A66, Player.Backpack.Serial):
        #   targetitem = Items.FindByID(0x14F0, 0x0A66, Player.Backpack.Serial)
        #Items.Move(targetitem, bottlevendorbag , -1)
        #Misc.Pause(1000)  
        #Misc.ResponsePrompt(str(cost))
    Misc.Pause(5000)
    gohome()
    
        
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
    recall(0x463D089E, 15) #Recall to bank  
    movetobank(arrows)
    arrowqty = Items.ContainerCount(Player.Bank.Serial, arrows, -1) 
    webhook('I Purchased ' + str(arrowqty)+' arrows')
    cost = arrowqty *3
    webhook('Total price: ' + str(cost)+' gold')      
    deedstack(arrows, 1000)
    gohome()
    homeunload(0x14F0, 0x0A66) #pink commodity deed

def checktools():
    if Items.BackpackCount(tinktool , -1) < 3:
        Misc.SendMessage('Out of Tink Tools',33)
        craftTink()
    Misc.Pause(1000)    
    if Items.BackpackCount(sawmodel , -1) < 3:
        Misc.SendMessage('Out of sawz',33)
        craftsaws()
        
def craftTink():    
    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 23)
    Misc.Pause(2000)
    
def craftsaws():

    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 51)



def getwood(qty):
        if str(Player.Position) != '(6927, 2484, 75)':
            recall(book[0],14)
            Player.Walk("North")
            Player.Walk("North")
            Player.Walk("North")
        Misc.Pause(1500)
        Items.UseItem(woodchest)
        Misc.Pause(1000)
        while Items.FindByID(wood, -1, Player.Backpack.Serial): 
            currentwood = Items.FindByID(wood, -1, Player.Backpack.Serial)
            Items.Move(currentwood, woodchest, -1) 
            Misc.Pause(1000)
        itemmove = Items.FindByID(wood, 0x0000, woodchest)
        Items.Move(itemmove, Player.Backpack.Serial, qty)
        
def getingots(qty):
        if str(Player.Position) != '(6927, 2484, 75)':
            recall(book[0],14)
            Player.Walk("North")
            Player.Walk("North")
            Player.Walk("North")
        Misc.Pause(1000)
        Items.UseItem(ingotchest)
        Misc.Pause(1000)
        while Items.FindByID(ingotmodel, -1, Player.Backpack.Serial): 
            currentingot = Items.FindByID(ingotmodel, -1, Player.Backpack.Serial)
            Items.Move(currentingot, ingotchest, -1) 
            Misc.Pause(1000)
        itemmove = Items.FindByID(ingotmodel, 0x0000, ingotchest)
        Items.Move(itemmove, Player.Backpack.Serial, qty)
        
def craftflute():
    if Items.BackpackCount(wood,-1)<20 or Items.BackpackCount(ingotmodel,-1)<20:
        webhook('Need mats - going home to restock!')
        getwood(1000)
        getingots(50)
    
    checktools()
    if str(Player.Position) != '(691, 799, 47)':
        recall(book[0],1)
        Player.Walk("North")
        Player.Walk("North")
    webhook('Crafting Flutes!')
    while Items.ContainerCount(flutevendor, flute, -1) < 75:
        if Items.BackpackCount(wood,-1)<20 or Items.BackpackCount(ingotmodel,-1)<20:
            craftflutes()
        Mobiles.UseMobile(0x00238962)
        Gumps.WaitForGump(797007452, 10000)
        Gumps.SendAction(797007452, 1)
        Misc.Pause(500)
        UseTinkTool = Items.FindByID(sawmodel, -1, Player.Backpack.Serial)
        Items.UseItem(UseTinkTool.Serial)
        #CRAFT FLUTE
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 44)
        Misc.Pause(3000)
        #CHECK EXP
        Journal.Clear()
        while Items.FindByID(flute, -1, Player.Backpack.Serial): 
            currentflute = Items.FindByID(flute, -1, Player.Backpack.Serial)
            Items.SingleClick(currentflute.Serial)
            Misc.Pause(1000)
            if Journal.Search("Exceptional"):
                Items.Move(currentflute, flutevendor, -1) 
                Misc.Pause(1000)
                Misc.ResponsePrompt(str(fluteprice))
            else: 
                Items.Move(currentflute, flutetrash, -1)
                Misc.Pause(1000)
                Journal.Clear()
    webhook('Done Flutes')
            
def hopgate():
    moongates = FindMoongates( Items )
    if len( moongates ) > 0:
      moongate = Items.Select( moongates, 'Nearest' )
      Items.UseItem( moongate )

      Gumps.WaitForGump( 3716879466, 2000 )
      Gumps.SendAction( 3716879466, 1 )
      
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
            
def gohome():
    if str(Player.Position) == '(6939, 2486, 75)':
        webhook('home already')
        return  
    recall(book[0],0)
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
        


def smithbods():
    abortcounter = 0
    webhook('Getting smith Bod')   
    castincog()
    Misc.Pause(1000)
    recall(book[1],0)
    while not Gumps.HasGump():
        abortcounter = abortcounter +1
        if abortcounter > 30:
            webhook('aborting on count')
            gohome()
        if Items.FindByID(0x13BB, -1, Player.Backpack.Serial): #chainmail
            Misc.WaitForContext(0x00029397, 10000) #sell 
            Misc.ContextReply(0x00029397, 3)
        else:
            Misc.WaitForContext(0x00029397, 10000)
            Misc.ContextReply(0x00029397, 2)
            Misc.Pause(1000)
    while Items.FindByID(0x13BB, -1, Player.Backpack.Serial): #chainmail
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
    recall(book[1],1)
    while not Gumps.HasGump():
        abordcounter = abortcounter + 1
        if abortcounter > 25:
            gohome()
        if Items.FindByID(sewingkit, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x0024A965, 10000)
            Misc.ContextReply(0x0024A965, 3)
            Misc.Pause(1000)
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

def homeunload(item, color): #unload athome
    while Items.FindByID(item, color, Player.Backpack.Serial): #looks passed item in mag
        currenttarget = Items.FindByID(item, color, Player.Backpack.Serial)
        Items.Move(currenttarget, unload, -1) 
        Misc.Pause(1000)

def castincog():
    if Player.BuffsExist('Incognito'):
        Player.HeadMessage(54,'incog already on')
    else:
        Spells.CastMagery( 'Incognito' )
        Misc.Pause(2000)

def webhook(msg):
    URI = 'https://discordapp.com/api/webhooks/658375319899602944/EDZ5qMDtgsGnoy6WBGiDKfbJQ90OgfSrOB218WWfbGZMDDmRkyWzLzLgEVbtKo-2gsY8'
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
    
def recall(book, rune):
    mana(30)
    rune = 5+6*rune
    currentlocation = Player.Position
    while currentlocation == Player.Position:
        Misc.Pause( 100 )
        Items.UseItem(book)
        Misc.Pause( 500)
        Gumps.WaitForGump( 1431013363, 5000 )
        Misc.Pause( 250 )
        Gumps.SendAction( 1431013363, rune )
        caststr()
        Misc.Pause( 500 )

def mana(mana_req):
    if Player.Mana < mana_req:
        Player.UseSkill( 'Meditation' )
        while Player.Mana < ( Player.ManaMax ):
            Misc.Pause( 50 )
def caststr():
    if Player.Weight > 375 and not Player.BuffsExist( 'Strength' ):
            Spells.CastMagery( 'Strength' )
            Target.WaitForTarget( 10000, False )
            Target.Self()
            Misc.Pause( 1000 )
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
  
def movefrombank(item, color): 
    Player.ChatSay(57,'Bank')
    Misc.Pause(500)   
    bank = Player.Bank.Serial
    while Items.FindByID(item, color, Player.Bank.Serial):
        targetitem = Items.FindByID(item, color, Player.Bank.Serial)
        Items.Move(targetitem, Player.Backpack.Serial , -1)
        Misc.Pause(1000)    
  
  
  
                    
def movetobank(item): 
    Player.ChatSay(57,'Bank')
    Misc.Pause(500)   
    bank = Player.Bank.Serial
    while Items.FindByID(item, -1, Player.Backpack.Serial):
        targetitem = Items.FindByID(item, -1, Player.Backpack.Serial)
        Items.Move(targetitem, bank , -1)
        Misc.Pause(1000)                    

def checkregs():
    #if Items.BackpackCount(0x0F7A,0) <50 or Items.BackpackCount(0x0F86,0) <50 or Items.BackpackCount(0x0F7B,0) < 50 orItems.BackpackCount(0x0F8C,0) < 50 or Items.BackpackCount(0x0F84,0) <50 or Items.BackpackCount(0x0F85,0)<50 or Items.BackpackCount(0x0F8D,0) <50 orItems.BackpackCount(0x0F88,0):
     for reg in regs:
         if Items.BackpackCount(reg,0)<50:
            restock()                    

def restock():
    webhook('Need Regs')
    gate(book[0], rune[0]) 
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

    
def regcount():
    webhook('Pearl: ' + str(Items.BackpackCount(0x0F7A,0)) +'/Root: ' + str(Items.BackpackCount(0x0F86,0)) + '/Moss: ' + str(Items.BackpackCount(0x0F7B,0)) + '/Sulf: ' + str(Items.BackpackCount(0x0F8C,0)) + '/Gar: ' + str(Items.BackpackCount(0x0F84,0)) + '/Gin: ' + str(Items.BackpackCount(0x0F85
    ,0))+'/Silk: ' + str(Items.BackpackCount(0x0F8D,0)) + '/Shade: ' + str(Items.BackpackCount(0x0F88,0))            )

    
def hide():

    if not Player.BuffsExist('Hiding'):

        Player.UseSkill('Hiding')


        
        
        
        
        
        
def checkallsupplies():
    global bankbalance
    global bankregbalance
    global regbalance
    global supplybalance
    global vendorbalance 
    global globalgold

    checksupplies()
    Misc.Pause(2000)
    regsupplies()
    Misc.Pause(2000)    
    getbalance()
    Misc.Pause(2000)  
    #checkvendors()
    #Misc.Pause(2000) 
    globalgold = bankbalance + regbalance + supplybalance + vendorbalance + bankregbalance
    temptotalgold = globalgold /1000
    webhook('TOTAL GOLD: ' + str(temptotalgold) + 'k')

    
def checksupplies():
        global supplybalance
        webhook('checking smith supply station')
        recall(book[0],14)
        Misc.Pause(750)
        Player.Walk("North")
        Player.Walk("North")
        Player.Walk("North")
        Player.Walk("North")
        Misc.Pause(2000)
        
                
        Items.UseItem(ingotchest)
        webhook(':::::::::Ingot Supply:::::::::')
        Misc.Pause(750)
        ironingotqty = Items.ContainerCount(ingotchest, ingotmodel, ingotcolor)
        dullcolorqty = Items.ContainerCount(ingotchest, ingotmodel, dullcolor)
        shadowcolorqty = Items.ContainerCount(ingotchest, ingotmodel, shadowcolor)
        coppercolorqty = Items.ContainerCount(ingotchest, ingotmodel, coppercolor)
        bronzecolorqty = Items.ContainerCount(ingotchest, ingotmodel, bronzecolor)
        goldcolorqty = Items.ContainerCount(ingotchest, ingotmodel, goldcolor)
        aggycolorqty = Items.ContainerCount(ingotchest, ingotmodel, aggycolor)
        vercolorqty = Items.ContainerCount(ingotchest, ingotmodel, vercolor)
        valcolorqty = Items.ContainerCount(ingotchest, ingotmodel, valcolor)
        
        webhook('Iron qty: ' + str(ironingotqty) + ' // Dull Qty: ' + str(dullcolorqty) +  ' // Shadow Qty: ' + str(shadowcolorqty) + ' // Copper Qty: ' + str(coppercolorqty) + ' // Bronze Qty: ' + str(bronzecolorqty) + ' // Gold Qty: ' + str(goldcolorqty) + ' // Aggy Qty: ' + str(aggycolorqty) + ' // Ver Qty '+ str(vercolorqty) + ' // Val Qty: ' + str(valcolorqty) )
        ingotgold = (ironingotqty * 8 + dullcolorqty * 15 + shadowcolorqty * 20 + coppercolorqty * 25 + bronzecolorqty * 35 + goldcolorqty * 40 +  aggycolorqty * 45 + vercolorqty * 50 + valcolorqty * 60)/1000
        webhook(str(ingotgold) + 'k Gold worth of ingots')
        
        
        Items.UseItem(woodchest)
        webhook(':::::::::Wood Supply:::::::::')
        Misc.Pause(750)
        regwoodqty = Items.ContainerCount(woodchest, wood, regwoodcolor)
        frostwoodqty = Items.ContainerCount(woodchest, wood, frostwoodcolor)
        bloodwoodqty = Items.ContainerCount(woodchest, wood, bloodwoodcolor)
        heartwoodqty = Items.ContainerCount(woodchest, wood, heartwoodcolor)
        webhook('Regular Wood Qty: ' + str(regwoodqty) + ' // Heart Qty: ' + str(heartwoodqty) +  ' // Blood Qty: ' + str(bloodwoodqty) + ' // Frost Qty: ' + str(frostwoodqty))
        woodgold = (regwoodqty * 0.5 + frostwoodqty * 200 + bloodwoodqty * 200 + heartwoodqty * 100)/1000
        webhook(str(woodgold) + 'k Gold worth of wood')
        
        Misc.Pause(2000)
        webhook(':::::::::Slayer Deed Supply:::::::::')
        Items.UseItem(arachniddeedchest)
        Misc.Pause(750)
        arachniddeedqty = Items.ContainerCount(arachniddeedchest, slayerdeeds[0], -1)
        webhook('Arachnid Slayer Deeds: ' +str(arachniddeedqty))
    
        Items.UseItem(elementaldeedchest)
        Misc.Pause(750)
        elementaldeedqty = Items.ContainerCount(elementaldeedchest, slayerdeeds[0], -1)
        webhook('Elemental Slayer Deeds: ' +str(elementaldeedqty))
        
        Items.UseItem(exorcismdeedchest)
        Misc.Pause(750)
        exorcismdeedqty = Items.ContainerCount(exorcismdeedchest, slayerdeeds[0], -1)
        webhook('Exorcism Slayer Deeds: '+ str(exorcismdeedqty))

        Items.UseItem(feydeedchest)
        Misc.Pause(750)
        feydeedqty = Items.ContainerCount(feydeedchest, slayerdeeds[0], -1)
        webhook('Fey Slayer Deeds: '+ str(feydeedqty))
        
        Items.UseItem(reponddeedchest)
        Misc.Pause(750)
        reponddeedqty = Items.ContainerCount(reponddeedchest, slayerdeeds[0], -1)
        webhook('Repond Slayer Deeds: '+ str(reponddeedqty))
        
        Items.UseItem(reptiliandeedchest)
        Misc.Pause(750)
        reptiliandeedqty = Items.ContainerCount(reptiliandeedchest, slayerdeeds[0], -1)
        webhook('Reptilian Slayer Deeds: '+ str(reptiliandeedqty))
        
        Items.UseItem(silverdeedchest)
        Misc.Pause(750)
        silverdeedqty = Items.ContainerCount(silverdeedchest, slayerdeeds[0], -1)
        webhook('Silver Slayer Deeds: ' +str(silverdeedqty))
        Misc.Pause(1000)
        totalgoldslayer = ( silverdeedqty + reptiliandeedqty + reponddeedqty + feydeedqty + exorcismdeedqty + elementaldeedqty + elementaldeedqty) * 5
        webhook('Total Gold in Slayers: ' + str(totalgoldslayer) + 'k')

        webhook(':::::::::Scale Armor:::::::::')
        scalearmorqty = [0,0,0,0,0,0]
        Items.UseItem(scalearmorchest[0])
        Misc.Pause(750)
        scalearmorqty[0] = Items.ContainerCount(scalearmorchest[0], scalearmor[0], -1)

        Items.UseItem(scalearmorchest[1])
        Misc.Pause(750)
        scalearmorqty[1] = Items.ContainerCount(scalearmorchest[1], scalearmor[1], -1)

        Items.UseItem(scalearmorchest[2])
        Misc.Pause(750)
        scalearmorqty[2] = Items.ContainerCount(scalearmorchest[2], scalearmor[2], -1)

        Items.UseItem(scalearmorchest[3])
        Misc.Pause(750)
        scalearmorqty[3] = Items.ContainerCount(scalearmorchest[3], scalearmor[3], -1)
 
        Items.UseItem(scalearmorchest[4])
        Misc.Pause(750)
        scalearmorqty[4] = Items.ContainerCount(scalearmorchest[4], scalearmor[4], -1)

        Items.UseItem(scalearmorchest[5])
        Misc.Pause(750)
        scalearmorqty[5] = Items.ContainerCount(scalearmorchest[5], scalearmor[5], -1)
    
        fullscalesets = min(scalearmorqty)
        scalegold =    fullscalesets * 10     
        webhook('Full scale sets: ' + str(fullscalesets) + ' worth ' + str(scalegold) + 'k gold')
        Misc.Pause(2000)
        
        webhook(':::::::::Leather Armor:::::::::')
        leatherarmorqty = [0,0,0,0,0,0]
        Items.UseItem(leatherarmorchest[0])
        Misc.Pause(750)
        leatherarmorqty[0] = Items.ContainerCount(leatherarmorchest[0], leatherarmor[0], -1)

        
        Items.UseItem(leatherarmorchest[1])
        Misc.Pause(750)
        leatherarmorqty[1] = Items.ContainerCount(leatherarmorchest[1], leatherarmor[1], -1)

        
        Items.UseItem(leatherarmorchest[2])
        Misc.Pause(750)
        leatherarmorqty[2] = Items.ContainerCount(leatherarmorchest[2], leatherarmor[2], -1)


        Items.UseItem(leatherarmorchest[3])
        Misc.Pause(750)
        leatherarmorqty[3] = Items.ContainerCount(leatherarmorchest[3], leatherarmor[3], -1)

        
        Items.UseItem(leatherarmorchest[4])
        Misc.Pause(750)
        leatherarmorqty[4] = Items.ContainerCount(leatherarmorchest[4], leatherarmor[4], -1)

        
        Items.UseItem(leatherarmorchest[5])
        Misc.Pause(750)
        leatherarmorqty[5] = Items.ContainerCount(leatherarmorchest[5], leatherarmor[5], -1)
        
        fullleathersets = min(leatherarmorqty)
        leathgold = fullleathersets * 3
        webhook('Full Leather sets: ' + str(fullleathersets) + ' worth ' + str(leathgold) + 'k gold')
        Misc.Pause(2000)
        
        tempgold = (leathgold + scalegold + totalgoldslayer+ woodgold + ingotgold)         
        supplybalance = tempgold * 1000
        webhook('TOTAL SUPPLY GOLD: ' + str(tempgold)+ 'k')
               
def regsupplies():
    global regbalance
    webhook('checking Regs& Kegs station supplies')
    recall(book[1],2)
    Misc.Pause(750)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")
    Misc.Pause(2000)
        
    Items.UseItem(regchest)
    webhook(':::::::::Keg Crafting Reg Supply:::::::::') 
    Misc.Pause(750)
    pearlqty =(Items.ContainerCount(regchest,0x0F7A,0) / 1000)
    rootqty = Items.ContainerCount(regchest,0x0F86,0) / 1000
    mossqty = Items.ContainerCount(regchest,0x0F7B,0) / 1000
    sulfqty = Items.ContainerCount(regchest,0x0F8C,0) / 1000
    garlicqty = Items.ContainerCount(regchest,0x0F84,0) / 1000
    ginsingqty = Items.ContainerCount(regchest,0x0F85,0) / 1000
    silkqty = Items.ContainerCount(regchest,0x0F8D,0) / 1000
    shadeqty=Items.ContainerCount(regchest,0x0F88,0) / 1000
    bottleqty = Items.ContainerCount(regchest,0x0F0E,0) / 1000 #bottles
    scrollqty = Items.ContainerCount(regchest,0x0EF3,0) / 1000 #scrolls
    arrowqty = Items.ContainerCount(regchest,0x0F3F,0) / 1000 #arrows
    
    reggold = (pearlqty * 5500 +  rootqty * 3500 + mossqty * 5500 + sulfqty * 3500 + garlicqty * 3500 + ginsingqty *3500 + silkqty * 3500 + shadeqty*3500+bottleqty*6000+scrollqty*6000 + arrowqty*3000)/1000
    webhook('Pearl: ' + str(pearlqty) +'k / Root: ' + str(rootqty) + 'k / Moss: ' + str(mossqty) + 'k / Sulf: ' + str(sulfqty) + 'k / Gar: ' + str(garlicqty) + 'k / Gin: ' + str(ginsingqty)+'k / Silk: ' + str(silkqty) + 'k / Shade: ' + str(shadeqty)  + 'k / Bottles: ' + str(bottleqty) + 'k / Scrolls: ' + str(scrollqty)  + 'k' +' / arrows: ' + str(arrowqty)  + 'k'           ) 
    webhook(str(reggold) + ' k worth of gold in regs for kegs')  
    
    
    webhook(':::::::::Keg Supply:::::::::')
    Misc.Pause(2000)
    Items.UseItem(emptykegchest)
    Misc.Pause(750) 
    emptykegqty = Items.ContainerCount(emptykegchest,kegmodel,-1)    
    Items.UseItem(expkegchest)
    Misc.Pause(750)    
    explosionkegqty=Items.ContainerCount(expkegchest,kegmodel,-1)
    Items.UseItem(strengthkegchest)
    Misc.Pause(750)  
    strengthkegqty= Items.ContainerCount(strengthkegchest,kegmodel,-1)
    Items.UseItem(refreshkegchest)
    Misc.Pause(750) 
    refreshkegqty=Items.ContainerCount(refreshkegchest,kegmodel,-1)
    Items.UseItem(agilitykegchest)
    Misc.Pause(750)
    agilitykegqty=Items.ContainerCount(agilitykegchest,kegmodel,-1)
    Items.UseItem(healkegchest)
    Misc.Pause(750)
    healkegqty=Items.ContainerCount(healkegchest,kegmodel,-1)
    Items.UseItem(curekegchest)
    Misc.Pause(750)        
    curekegqty=Items.ContainerCount(curekegchest,kegmodel,-1)
    Items.UseItem(poisonkegchest)
    Misc.Pause(750  )
    poisonkegqty= Items.ContainerCount(poisonkegchest,kegmodel,-1)
    
    webhook('We got ' + str(emptykegqty) + ' empty kegs ready to go')
    webhook('Exp: ' + str(explosionkegqty) + ' // Str: ' + str(strengthkegqty) + ' // Refresh: ' + str(refreshkegqty) + ' // Agility: ' + str(agilitykegqty) + ' // Heal: ' + str(healkegqty) + ' // Cure: ' + str(curekegqty) + ' // Poison: '+ str(poisonkegqty))
    totalkeggold = explosionkegqty*5 + strengthkegqty * 3 + refreshkegqty * 3.8 + agilitykegqty * 3 + healkegqty * 3.5 + curekegqty  * 3.5 + poisonkegqty * 3.5 
    webhook(str(totalkeggold) + ' k worth of gold in kegs')  
    
    temp = totalkeggold + reggold
    regbalance = temp * 1000
    webhook('TOTAL REG AND KEG BALANCE: ' + str(temp) + 'k')

def getbalance():
    global bankbalance
    webhook(':::::::::Bank Supply:::::::::')
    regamounts= [0,0,0,0,0,0,0,0]
    recall(book[0],15)
    Player.ChatSay( 58, 'Balance and bank' )
    Misc.Pause(2000)
    bankbox = Items.FindBySerial(0x41006888)
    if Journal.Search("balance")== True: 
        a = Journal.GetLineText("balance is")
        balance = a.replace('Thy current bank balance is ', '')
        balance = balance.replace(' Gold.',"")
        balance = balance.replace(',',"")
        balance= int(balance)
    webhook('There is ' + str(balance/1000) + 'k gold in the bank')
    Misc.Pause(750)
    pearlqtybank =(Items.ContainerCount(bankbox,0x0F7A,0) / 1000)
    rootqtybank = Items.ContainerCount(bankbox,0x0F86,0) / 1000
    mossqtybank = Items.ContainerCount(bankbox,0x0F7B,0) / 1000
    sulfqtybank = Items.ContainerCount(bankbox,0x0F8C,0) / 1000
    garlicqtybank = Items.ContainerCount(bankbox,0x0F84,0) / 1000
    ginsingqtybank = Items.ContainerCount(bankbox,0x0F85,0) / 1000
    silkqtybank = Items.ContainerCount(bankbox,0x0F8D,0) / 1000
    shadeqtybank=Items.ContainerCount(bankbox,0x0F88,0) / 1000
    bottleqtybank = Items.ContainerCount(bankbox,0x0F0E,0) / 1000 #bottles
    scrollqtybank = Items.ContainerCount(bankbox,0x0EF3,0) / 1000 #scrolls
    arrowqtybank = Items.ContainerCount(bankbox,0x0F3F,0) / 1000 #arrows
    
    reggoldbank = (pearlqtybank * 5500 +  rootqtybank * 3500 + mossqtybank * 5500 + sulfqtybank * 3500 + garlicqtybank * 3500 + ginsingqtybank *3500 + silkqtybank * 3500 + shadeqtybank*3500+bottleqtybank*6000+scrollqtybank*6000 + arrowqtybank*3000)/1000
    webhook('Pearl: ' + str(pearlqtybank) +'k / Root: ' + str(rootqtybank) + 'k / Moss: ' + str(mossqtybank) + 'k / Sulf: ' + str(sulfqtybank) + 'k / Gar: ' + str(garlicqtybank) + 'k / Gin: ' + str(ginsingqtybank)+'k / Silk: ' + str(silkqtybank) + 'k / Shade: ' + str(shadeqtybank)  + 'k / Bottles: ' + str(bottleqtybank) + 'k / Scrolls: ' + str(scrollqtybank)  + 'k' +' / arrows: ' + str(arrowqtybank)  + 'k'           ) 
    webhook(str(reggoldbank) + ' k worth of gold in regs in teh bank')      

    
    
    
    bankbalance = balance    
    
    
    
x = 2

lastcomment = "start"
while x > 1:
    
    f = open('C:/Users/Jason/Desktop/craftbot.txt', 'r')
    crafterbodtimer = crafterbodtimer +1
    arrowtimer = arrowtimer +1
    if crafterbodtimer > 18000:
        webhook('Bod Timer hit 18000')
        crafterbodtimer=0
        smithbods()
        #if arrowtimer == 3600:
            #webhook('arrow timer hit 3600')
            #arrowtimer=0
            #buyarrows()
    for line in f:    
        #Player.ChatSay( 58,line )
        Misc.Pause(1)     
    if line != lastcomment:        
        if line == '.getbods\n':
            smithbods()        
        if line == '.stockflute\n':
            craftflute()    
        if line == '.buyarrows\n':
            buyarrows()
        if line == '.buybottles\n':
            buybottles()
        if line == '.checkvendors\n':
            checkvendors()
        if line == '.checksupplies\n':
            checksupplies()   
        if line == '.getbalance\n':
            getbalance()
        if line == '.checkallsupplies\n':
            checkallsupplies()
        if line == '.checkregsupplies\n':
            regsupplies()   
        if line == '.stockslayerdeeds\n':
            stockslayerdeeds()    
        if line == '.gohome\n':
            gohome()   
     
          
           
    Misc.Pause(1000)
    lastcomment = line