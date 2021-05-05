from System.Collections.Generic import List
bodylist = List[int]([0x0190,0x0191,0x02EC,0x02EB,0x025D,0x025E,0x019,0x079,0x029B,0x029A])
ghostlist = List[int]([0x0192,0x0193,0x0260,0x025f])

#sparalla#
#for var in bodylist
#find var in groun 0 10 
#if in friend list e parall 
#cast clumsy, target, warmode off,on,off

def CheckAndRun():
    enemy_filter = Mobiles.Filter()
    enemy_filter.Enabled = True
    enemy_filter.RangeMin = -1
    enemy_filter.RangeMax = 10
    enemy_filter.Bodies = bodylist
    enemies = Mobiles.ApplyFilter(enemy_filter)

#smortalla#
for var in bodylist:
     