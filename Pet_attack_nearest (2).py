import time
import sys
import math
#
from System.Collections.Generic import List
from System import Byte, Int32
#
while True:
    enemy = None
    if not enemy:
        enemy_filter = Mobiles.Filter()
        enemy_filter.Enabled = True
        enemy_filter.RangeMin = -1
        enemy_filter.RangeMax = 8
        enemy_filter.CheckLineOfSite = True
        enemy_filter.Notorieties = List[Byte](bytes([3,4,5,6]))
        #
        enemies = Mobiles.ApplyFilter(enemy_filter)
        remove_mine = []
        for e in enemies:
            owner = Mobiles.GetPropValue(e.Serial, "Owner")
            #Misc.SendMessage("Owner: {}".format(owner))
            if owner == Player.Name:
                remove_mine.append(e)
        if len(remove_mine) != 0:        
            for e in remove_mine:
                enemies.Remove(e)
                Misc.SendMessage("Removed one")
        #Misc.SendMessage("Up CLose Enemies after is {}".format(len(up_close_enemies)))
        if len(enemies) > 0 :
            enemy = Mobiles.Select(enemies, 'Nearest')
            
    if enemy != None:
        Player.ChatSay(52, "All kill")
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(enemy)
        Mobiles.Message(enemy, 5, "Attacking 0x{:08x}".format(enemy.Serial))
    else:
        #Player.HeadMessage(5, "No Enemy") 
        pass   
    Misc.Pause(2000)