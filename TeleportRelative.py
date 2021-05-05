class Coord:
    X = Y = Z = 0
    def __init__(self, x, y):
        self.X = x + Player.Position.X
        self.Y = y + Player.Position.Y
        self.Z = Player.Position.Z

Tiles = 9
Dir = {
    'North' : Coord(0, -Tiles),
    'South' : Coord(0, Tiles),
    'West' : Coord(-Tiles, 0),
    'East' : Coord(Tiles, 0),
    'Up' : Coord(-Tiles, -Tiles),
    'Down' : Coord(Tiles, Tiles),
    'Left' : Coord(-Tiles, Tiles),
    'Right' : Coord(Tiles, -Tiles)
    }
    

Rel = Dir[Player.Direction]
if Items.BackpackCount(0x1F42, 0) > 0: # TP Scrolls
    Items.UseItemByID(0x1F42, 0)
else:
    Spells.CastMagery("Teleport")

Target.WaitForTarget(9000, True)
Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)