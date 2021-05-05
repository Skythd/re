from System.Collections.Generic import List 
#auto cloth farmer by Mourn 8182 discord contact
# have single runic atlas in bag, first rune marked at house, runs north to loom and spinning wheels(6) with commodity deed box close
# find 3 sheep pens mark 2 runes in each pen
# rune 2 and 5 first pen
# rune 3 and 6 second pen
# rune 4 and 7 third pen
# rune numbers are references to the order u place them in your atlas

sheeple = Mobiles.Filter()
sheeple.RangeMax = 20
sheeple.Bodies = List[int]((0x00CF,0x00DF))

blade = Items.FindByID(0x13F6,-1,Player.Backpack.Serial)   # ID of the blade you use to shear

wheelfil = Items.Filter()
wheelfil.RangeMax = 3
wheelfil.OnGround = True
wheelfil.Movable = False
wheelfil.Graphics = List[int]((0x2DDA,0x2DDA)) #elven wheel south add your id to list

loomfil = Items.Filter()
loomfil.RangeMax = 3
loomfil.OnGround = True
loomfil.Movable = False
loomfil.Graphics = List[int]((0x1062,0x1062)) # loom south add your id to list

CFilter = Items.Filter()
CFilter.RangeMax = 3
CFilter.OnGround = True
CFilter.Movable = False
container = List[int]((0x09AA, 0x0E7D)) # commodity deed box both directions or add ur id to list 
CFilter.Graphics = container

def go(x1, y1):
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = 5
    PathFinding.Go(Coords)
    
def recall(runenumber):
    Misc.Pause(2000)
    newrunenumber = 49999 + runenumber   
    Items.UseItemByID(0x9C16)
    Misc.Pause(1000)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, newrunenumber)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, 4000)
    newrunenumber = 0
    Misc.Pause(4000)

def shear(): 
    ignore = []    
    sheeps = Mobiles.ApplyFilter(sheeple)
    while len(sheeps) > 0:
        if Player.Weight > Player.MaxWeight - 15:
            break
            gohome()
        sheep = Mobiles.Select(sheeps,'Nearest')
        if sheep.Serial in ignore:
            Player.Attack(sheep)
            Spells.CastMagery('Mind Blast')
            Target.WaitForTarget(3000)
            Target.TargetExecute(sheep)
        go(sheep.Position.X,sheep.Position.Y)
        if not Player.InRangeMobile(sheep,3):
            ignore.append(sheep.Serial)
        Spells.CastMagery('Harm')
        Items.UseItem(blade)
        Target.WaitForTarget(1000)
        Target.TargetExecute(sheep)
        Target.WaitForTarget(1000)
        Target.TargetExecute(sheep)
        sheeps = Mobiles.ApplyFilter(sheeple)
        Misc.Pause(200)
        
def gohome():
        recall(1)
        Misc.Resync()
        Player.Run('North')
        Player.Run('North')
        Player.Run('North')
        Misc.Resync()
        Player.Run('North')
        Player.Run('North')
        Player.Run('North')
        Player.Run('North')
        Misc.Resync()
        Player.Run('North')
        Player.Run('North')
        Misc.Pause(1000)
        Misc.Resync()
        
def spin():
    while Items.BackpackCount(0x0DF8,-1) > 0:
        wheels = Items.ApplyFilter(wheelfil)    
        for wheel in wheels:
            wool = Items.FindByID(0x0DF8,-1,Player.Backpack.Serial)
            Items.UseItem(wool)
            Target.WaitForTarget(1000)
            Target.TargetExecute(wheel)
            Misc.Pause(1100)
        Misc.Pause(100)
    Misc.Pause(4000)

def weave():
    bolts = Items.FindByID(0x0F95,-1,Player.Backpack.Serial)
    yarn = Items.FindByID(0x0E1D,-1,Player.Backpack.Serial)
    looms = Items.ApplyFilter(loomfil)
    Misc.Pause(300)
    loom = Items.Select(looms,'Nearest')
    Misc.Pause(100)
    boxs = Items.ApplyFilter(CFilter)
    Misc.Pause(300)
    box = Items.Select(boxs,'Nearest')
    Misc.Pause(100)
    Items.WaitForContents(box,2000)
    while Items.BackpackCount(0x0E1D,-1) > 0:
        if yarn:
            Items.UseItem(yarn)
            Target.WaitForTarget(2000)
            Target.TargetExecute(loom) 
            Misc.Pause(1000)
    bolts = Items.FindByID(0x0F95,-1,Player.Backpack.Serial)            
    Items.Move(bolts.Serial,box,0)
    Misc.Pause(1100)
    
def Main():
    while not Player.IsGhost: 
        runenum = 2   
        while runenum <= 7:            
            recall(runenum)
            shear()
            runenum +=1
            if runenum == 8:
                break
            if Player.Weight > Player.MaxWeight - 15:
                break                
        gohome()
        spin()
        weave()

Main()
