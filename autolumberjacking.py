# Parametri
RaggioScansione = 15
TreeStaticID = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]
SerialAccetta = 0x4035C605
EquipAccettaDelay = 1000
TimeoutOnWaitAction = 4000
ChopDelay = 1000
RuneBookBanca = 0x400056E4
RuneBookAlberi = 0x40162DF1
RecallPause = 3000
DragDelay = 1200
LogID = 0x1BDD
OtherResourceID = [12687, 12697, 12127, 12688, 12689]
LogBag = 0x40191C19 #0x4002ED85
OtherResourceBag = 0x40191C19 #0x401CD4DB
WeightLimit = 500
BankX = 2051
BankY = 1343


# Variabili Sistema
from System.Collections.Generic import List
tileinfo = List[Statics.TileInfo]
treeposx = []
treeposy = []
treeposz = []
treegfx = []
treenumber = 0
blockcount = 0
lastrune = 5
onloop = True

def RecallNextSpot( ):
    global lastrune
    Gumps.ResetGump()
    Misc.SendMessage("--> Racall to Spot", 77) 
    Items.UseItem(RuneBookAlberi)
    Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
    Gumps.SendAction(1431013363, lastrune)
    Misc.Pause(RecallPause)
    lastrune = lastrune + 6
    if lastrune > 95:
        lastrune = 5
        
    EquipAxe()
        

def RecallBack( ):
    while Player.Position.X == BankX and Player.Position.Y == BankY:
        global lastrune
        Gumps.ResetGump()
        Misc.SendMessage("--> Torno a tagliare ", 77) 
        Misc.Pause(RecallPause)
        Items.UseItem(RuneBookAlberi)
        Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
        Gumps.SendAction(1431013363, (lastrune - 6))
        Misc.Pause(RecallPause)
        if lastrune < 6:
            Misc.SendMessage("--> Inizio Nuovo ciclo", 77) 
            lastrune = 5
        else:
            Misc.NoOperation()
        EquipAxe()
       

def Scarico( ):
    global BankX
    global BankY
    while Player.Weight >= WeightLimit:
        Gumps.ResetGump()
        Items.UseItem(RuneBookBanca)
        Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
        Gumps.SendAction(1431013363, 5)
        Misc.Pause(RecallPause)
        Player.ChatSay(33, "Bank")
        Misc.Pause(300)
        for item in Player.Backpack.Contains:
            if item.ItemID == LogID:
                Misc.SendMessage("--> Sposto Log", 77) 
                Items.Move(item, LogBag, 0)
                Misc.Pause(DragDelay)
            else:
                for otherid in OtherResourceID:
                    if item.ItemID == otherid:
                        Misc.SendMessage("--> Sposto Altro", 77) 
                        Items.Move(item, OtherResourceBag, 0)
                        Misc.Pause(DragDelay)
                    else:
                        Misc.NoOperation()

def RangeTree( spotnumber ):
    if (Player.Position.X - 1) == treeposx[spotnumber] and (Player.Position.Y + 1) == treeposy[spotnumber]:
        return True
    elif (Player.Position.X - 1) == treeposx[spotnumber] and (Player.Position.Y - 1) == treeposy[spotnumber]:
        return True
    elif (Player.Position.X + 1) == treeposx[spotnumber] and (Player.Position.Y + 1) == treeposy[spotnumber]:
        return True
    elif (Player.Position.X + 1) == treeposx[spotnumber] and (Player.Position.Y - 1) == treeposy[spotnumber]:
        return True
    elif Player.Position.X == treeposx[spotnumber] and (Player.Position.Y - 1) == treeposy[spotnumber]:
        return True    
    elif Player.Position.X == treeposx[spotnumber] and (Player.Position.Y + 1) == treeposy[spotnumber]:   
        return True     
    elif Player.Position.Y == treeposy[spotnumber] and (Player.Position.X - 1) == treeposx[spotnumber]:
        return True    
    elif Player.Position.Y == treeposy[spotnumber] and (Player.Position.X + 1) == treeposx[spotnumber]:   
        return True    
    else:
        return False
    
def ScanStatic( ): 
    global treenumber
    Misc.SendMessage("--> Inizio Scansione Tile", 77)
    minx = Player.Position.X - RaggioScansione
    maxx = Player.Position.X + RaggioScansione
    miny = Player.Position.Y - RaggioScansione
    maxy = Player.Position.Y + RaggioScansione

    while miny <= maxy:
        while minx <= maxx:
            tileinfo = Statics.GetStaticsTileInfo(minx, miny, Player.Map)
            if tileinfo.Count > 0:
                for tile in tileinfo:
                    for staticid in TreeStaticID:
                        if staticid == tile.StaticID:
                            Misc.SendMessage('--> Albero X: %i - Y: %i - Z: %i' % (minx, miny, tile.StaticZ), 66)
                            treeposx.Add(minx)
                            treeposy.Add(miny)
                            treeposz.Add(tile.StaticZ)
                            treegfx.Add(tile.StaticID)
            else:
                Misc.NoOperation()
            minx = minx + 1
        minx = Player.Position.X - RaggioScansione            
        miny = miny + 1
    treenumber = treeposx.Count    
    Misc.SendMessage('--> Totale Alberi: %i' % (treenumber), 77)
    
def MoveToTree( spotnumber ):
    pathlock = 0
    Misc.SendMessage('--> Moving to TreeSpot: %i' % (spotnumber), 77)
    Player.PathFindTo(treeposx[spotnumber], treeposy[spotnumber], treeposz[spotnumber])
    while not RangeTree(spotnumber):
        CheckEnemy()  
        Misc.Pause(10)
        pathlock = pathlock + 1
        if pathlock > 350:
            Player.PathFindTo(treeposx[spotnumber], treeposy[spotnumber], treeposz[spotnumber])  
            pathlock = 0
        else:
            Misc.NoOperation()
        
    Misc.SendMessage('--> Raggiunto TreeSpot: %i' % (spotnumber), 77)

def EquipAxe( ):
    if not Player.CheckLayer("RightHand"):
        Player.EquipItem(SerialAccetta)
        Misc.Pause(EquipAccettaDelay)      
    else:
        Misc.NoOperation()
    
def CutTree( spotnumber ):
    global blockcount
    if Target.HasTarget():
        Misc.SendMessage("--> Blocco rilevato target residuo, cancello!", 77)
        Target.Cancel()
        Misc.Pause(500)
    else:
        Misc.NoOperation()    
    
    if (Player.Weight >= WeightLimit):
        Misc.Pause(1500)
        Scarico( )
        RecallBack()
        MoveToTree(spotnumber)
    else:
        Misc.NoOperation()
    CheckEnemy()    
    Journal.Clear()
    accetta = Items.FindBySerial(SerialAccetta)
    Items.UseItem(accetta)
    Target.WaitForTarget(TimeoutOnWaitAction)
    Target.TargetExecute(treeposx[spotnumber], treeposy[spotnumber], treeposz[spotnumber], treegfx[spotnumber])
    Misc.Pause(ChopDelay)
    if Journal.Search("There's not enough"):
        Misc.SendMessage("--> Cambio albero", 77)
    elif Journal.Search("That is too far away"):
        blockcount = blockcount + 1
        Journal.Clear()
        if (blockcount > 15):
            blockcount = 0
            Misc.SendMessage("--> Possibile blocco rilevato cambio albero", 77)
        else:
            CutTree(spotnumber)
    else:
        CutTree(spotnumber)
        
def CheckEnemy( ):
    if (Player.Hits < Player.HitsMax):
        Misc.SendMessage("--> WARNING: Enemy Around!",33)
        Misc.Beep()
        
        fil = Mobiles.Filter()
        fil.Enabled = True
        fil.RangeMax = 2
        enemyfound = 0
        enemys = Mobiles.ApplyFilter(fil)
        
        for enemy in enemys:
            if enemy.Notoriety == 3:
                enemyfound = enemy.Serial
            else:
                Misc.NoOperation()
                
        if enemyfound != 0:
            enemymobile = Mobiles.FindBySerial(enemyfound)
            Misc.SendMessage("--> WARNING: Enemy Detected!",33) 
            Spells.CastMagery("Poison")
            Target.WaitForTarget(1000)
            Target.TargetExecute(enemymobile)
            Misc.Pause(900)
            while enemymobile:
                Spells.CastMagery("Harm")
                Target.WaitForTarget(1000)
                Target.TargetExecute(enemymobile)
                Misc.Pause(900)
                enemymobile = Mobiles.FindBySerial(enemyfound)
                
        while Player.Hits < Player.HitsMax:
            Spells.CastMagery("Heal")
            Target.WaitForTarget(1000)
            Target.Self()
            Misc.Pause(900)    

        EquipAxe()     
        
    else:
        return;

Misc.SendMessage("--> Avvio Tagliaboschi", 77)     
while onloop:
    RecallNextSpot()
    ScanStatic()
    i = 0
    while i < treenumber:
        MoveToTree(i)
        CutTree(i)
        i = i + 1
    treeposx = []
    treeposy = []
    treeposz = []
    treegfx = []
    treenumber = 0