
from System.Collections.Generic import List 
gem = Items.FindByID(0x193F,-1,Player.Backpack.Serial)

hueNone = 0x0838
hueRed = 0x0021
huePink = 0x0021
hueWhite = 0x047E
hueBlue = 0x0480
hueLtOj = 0x05E5
hueLtGrn = 0x0041
hueDkGrn = 0X0593


dFilter = Items.Filter()
dFilter.RangeMax = 5
dFilter.OnGround = True
dFilter.Enabled = True
dFilter.Movable = True
door = List[int]((0x0677, 0x0677))  
dFilter.Graphics = door

def gotoLocation(x1, y1):
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = -1
    PathFinding.Go(Coords)

def roomOne(item): 
    Journal.Clear()
    gotoLocation(985, 1117) 
    doors = Items.ApplyFilter(dFilter)
    Misc.Pause(500)
    thedoor = Items.Select(doors,'Nearest')
    Misc.Pause(500)
    Items.UseItem(thedoor)
    Misc.Pause(3000) 
    gotoLocation(984,1109)    
    while not Journal.Search('Hurry') == True:
        if Target.HasTarget() == False:
            if Target.HasTarget() == False:
                Spells.CastMagery('Teleport')
                Misc.Pause(1200)
        elif item.Hue == hueRed:            
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(987,1109,-42)
            Misc.Pause(500) 
        elif item.Hue == hueWhite:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(987,1108,-42)
            Misc.Pause(500) 
        elif item.Hue == hueBlue:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(981,1109,-42)
            Misc.Pause(500) 
        elif item.Hue == huePink:
            Misc.Pause(500) 
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(981,1108,-42)
        Misc.Pause(300)
    gotoLocation(985,1104)
    Misc.Pause(1000)
    doors = Items.ApplyFilter(dFilter)
    Misc.Pause(500)
    thedoor = Items.Select(doors,'Nearest')
    Misc.Pause(500)
    Items.UseItem(thedoor)
    Misc.Pause(3000)
    
def roomTwo(item): 
    Journal.Clear()
    Misc.Pause(500)  
    while not Journal.Search('Hurry') == True:
        if Target.HasTarget() == False:
            Spells.CastMagery('Teleport')
            Misc.Pause(1200)
        elif item.Hue == hueRed:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(982,1096,-42)
            Misc.Pause(500) 
        elif item.Hue == hueWhite:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(986,1098,-42)
            Misc.Pause(500) 
        elif item.Hue == hueBlue:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(986,1094,-42)
            Misc.Pause(500)
        elif item.Hue == huePink:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(982,1094,-42)
            Misc.Pause(500) 
        elif item.Hue == hueLtGrn:             
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(982,1098,-42)
            Misc.Pause(500)
        elif item.Hue == hueLtOj:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(986,1096,-42)
            Misc.Pause(500)    
        Misc.Pause(300)    
    gotoLocation(985,1092)
    Misc.Pause(500)
    Misc.Pause(500)
    doors = Items.ApplyFilter(dFilter)
    Misc.Pause(500)
    thedoor = Items.Select(doors,'Nearest')
    Items.UseItem(thedoor)
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    Player.Walk('North')
    
def roomThree(item): 
    Journal.Clear()
    Misc.Pause(500)  
    while not Journal.Search('Hurry') == True:
        if Target.HasTarget() == False:
            Spells.CastMagery('Teleport')
            Misc.Pause(1200)
        elif item.Hue == hueRed:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(988,1079,-42)
            Misc.Pause(500) 
        elif item.Hue == hueWhite:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(989,1079,-42)
            Misc.Pause(500) 
        elif item.Hue == hueBlue:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(979,1078,-42)
            Misc.Pause(500)
        elif item.Hue == huePink:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(980,1078,-42)
            Misc.Pause(500) 
        elif item.Hue == hueLtGrn:             
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(980,1079,-42)
            Misc.Pause(500)
        elif item.Hue == hueLtOj:
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(989,1078,-42)
            Misc.Pause(500)
        elif item.Hue == hueDkGrn:             
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(988,1078,-42)
            Misc.Pause(500) 
            
        Misc.Pause(300)    

        # drkojtiles = (988,1078)
        # lt grn  989 1078
        # blue   988 1079
        #pink  989  1079
        #lt oj  980 1079
        #dk grn 979 1079
        # white  980 1078
        # red 979 1078
        
        
            
roomOne(gem)
roomTwo(gem)
roomThree(gem)



