import sys
from System.Collections.Generic import List
from System import Byte

straightNS = 0x9BE7
straightEW = 0x9BF4
bottomcorner = 0x9BEB
rightcorner = 0x9BF8
leftcorner = 0x9BEF
topcorner = 0x9BFC

ignore = []
pieces = List[int]((straightNS, straightEW, bottomcorner, rightcorner, leftcorner, topcorner))

pieceFilter = Items.Filter()
pieceFilter.Enabled = True
pieceFilter.OnGround = True
pieceFilter.Movable = True
pieceFilter.Graphics = pieces
pieceFilter.RangeMax = 2

organizerBag = Items.FindByID(0x0E75,-1,Player.Backpack.Serial)
if not organizerBag:
    organizerBag = Player.Backpack
while True:
    items = Items.ApplyFilter(pieceFilter)
    Misc.Pause(200)
    if Timer.Check('move') == False:
        for item in items:
            if item.Serial in ignore:
                continue
            if item.ItemID == straightNS:
                Items.Move(item,organizerBag,1,90,100)
                Timer.Create('move',1800)
                Misc.Pause(300)                
            elif item.ItemID == straightEW:
                Items.Move(item,organizerBag,1,90,40)
                Timer.Create('move',1800)
                Misc.Pause(300)
            elif item.ItemID == bottomcorner:
                Items.Move(item,organizerBag,1,40,100)
                Timer.Create('move',1800)
                Misc.Pause(300)
            elif item.ItemID == rightcorner:
                Items.Move(item,organizerBag,1,140,100)
                Timer.Create('move',1800)
                Misc.Pause(300)
            elif item.ItemID == leftcorner:
                Items.Move(item,organizerBag,1,40,40)
                Timer.Create('move',1800)
                Misc.Pause(300)
            elif item.ItemID == topcorner:
                Items.Move(item,organizerBag,1,140,40)
                Timer.Create('move',1800)
                Misc.Pause(300)
            else:
                Misc.NoOperation()
                    
        for piece in organizerBag.Contains:
            if not piece.Serial in ignore:
                ignore.append(piece.Serial)
                Misc.Pause(100)
            
            
    