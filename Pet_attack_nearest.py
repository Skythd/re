import time
import sys
import math
#
if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())
#
import common
#
from System.Collections.Generic import List
from System import Byte, Int32
#
#
def findRecursive(containerSerial, typeArray):
    ret_list = []
    container = Items.FindBySerial(containerSerial)
    if container != None:
        for item in container.Contains:
            if item.ItemID in typeArray:
                ret_list.append(item)
            if item.IsContainer:
                for tmp in findRecursive(item.Serial, typeArray):
                    ret_list.append(tmp)
    return ret_list
#
Misc.ClearIgnore( )
if Misc.CheckSharedValue("Pets"):
    for pet in Misc.ReadSharedValue("Pets"):
        Misc.IgnoreObject(pet)
#
while True:
    #enemy = Mobiles.FindBySerial(Target.GetLast())
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
        Player.HeadMessage(5, "No Enemy")    
    Misc.Pause(2000)