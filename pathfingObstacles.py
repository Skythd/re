from System import Random
from System.Collections.Generic import List
chests =List[int]((0x0E42,0x0E43,0x0E40,0x09AB,0x0E41,0x0E7C))

fil = Items.Filter()
fil.Enabled = True
fil.RangeMax = 25 
fil.OnGround = True
fil.Movable = False
fil.Graphics = chests

def go(x1, y1):
    x = x1
    y = y1
    chests = Items.ApplyFilter(fil)
    for chest in chests:
        if chest.Position.X == x1 and chest.Position.Y == y1:
            Player.HeadMessage(43,'Chest Blocking')
            rnd = Random()
            rndRange = List[int]([-1,1])            
            xmod = rnd.Next(len(rndRange))
            x1 += rndRange[xmod]        
            ymod = rnd.Next(len(rndRange))
            y1 += rndRange[ymod]

    land = Statics.GetLandID(x1, y1, Player.Map)
    if Statics.GetLandFlag(land, 'Impassable'):
        Player.HeadMessage(43,'Impassable Land')
        Misc.Pause(1000)
        go(x,y)
          
    statics = Statics.GetStaticsTileInfo(x1, y1, Player.Map)
    if statics:
        for static in statics:
            if static.StaticID:                
                if Statics.GetTileFlag(static.StaticID, 'Impassable'):
                    Player.HeadMessage(43,'Static Blocking')
                    Misc.Pause(1000)
                    
                    go(x,y)
                    
                    
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = 5
    PathFinding.Go(Coords)
    
go(5611, 802)
