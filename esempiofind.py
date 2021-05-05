def CheckAndRun():
    # figure this out later
    return
    enemy_filter = Mobiles.Filter()
    enemy_filter.Enabled = True
    enemy_filter.RangeMin = -1
    enemy_filter.RangeMax = 10
    enemy_filter.Notorieties = List[Byte](bytes([4,5,6]))
    enemies = Mobiles.ApplyFilter(enemy_filter)
    
    if len(enemies) > 0:
        #Spells.CastMagery("Mark")
        #Target.WaitForTarget(2000, True)
        #Target.TargetExecute(SavePlaceRune)
        #Misc.Pause(3000)
        #Spells.CastMagery("Recall")
        #Target.WaitForTarget(2000, True)
        #Target.TargetExecute(StoreWoodRune)
        sys.exit(0)
        
		
		
		
def FindPackhorse():
    pack_horse = 0
    findPack = Mobiles.Filter()
    findPack.Enabled = True
    findPack.RangeMax = 2
    findPack.Bodies = List[int]([0x0123, 0x0319])
    listPack = Mobiles.ApplyFilter(findPack)
    if len(listPack) > 0:
        for i in listPack:
            pack_horse = listPack[0]
            Misc.SendMessage("Pack is 0x{:x}".format(pack_horse.Serial))
    else:
        Misc.SendMessage("NO PACK HORSE")
        pack_horse = Mobiles.FindBySerial(0x00B0C1E5)
    return pack_horse
PackHorse = FindPackhorse()   




LootListName = "chest"
PickableChests = List[int]([ 0x0E40, 0x0E41, 0x09AB, 0x0E42, 0x0E43, 0x0E77, 0x0E7C, 0x0E7E, 0x09A9, 0x0E7F, 0x0E3E, 0x0E3D, 0x0E3F, 0x0E3C])
# 
# You need an autoloot list with the name that matches whatever you specify in LootListName above
# PickableChests is probably everything, but if you find something it doesn't recognize as pickable
# add it to the list 
#
#
chest = Items.Filter()
chest.Enabled = True
chest.OnGround = True
chest.Movable = False
chest.Graphics = PickableChests
chest.RangeMax = 1
chestOnGround = Items.ApplyFilter(chest)

LootList = set()
for item in AutoLoot.GetList(LootListName):
    LootList.add(item.Graphics)
#    
    
    

#
sheep_filter = Mobiles.Filter()
    sheep_filter.Enabled = True
    sheep_filter.Bodies = List[int] ([ 0x00CF ])
    sheep_filter.RangeMax = 16
    sheep_filter.CheckIgnoreObject = True
    sheeps = Mobiles.ApplyFilter(sheep_filter)
    num_sheeps = len(sheeps)
    sheep = Mobiles.Select(sheeps, "Nearest")
    if sheep:
#

while True:
    enemy = Target.GetTargetFromList('filtername')
    Misc.Pause(200)
    Player.Attack(enemy)
    while enemy:
        Misc.Pause(300)
        
 #