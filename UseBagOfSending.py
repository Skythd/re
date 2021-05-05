import time
import sys
#
#
# This script only sends Gold piles that are above the threshold specified
# However it could be modified to send other things without too much change
#
#
GoldAmountToSend = 55000
BagOfSendingID = 0x0E76
ItemsIDsToSend = [ 0xeed ]
#
if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())
#
from System.Collections.Generic import List
from System import Byte
#
#    
def findRecursive(containerSerial, typeArray):
    ret_list = []    
    container = Items.FindBySerial(containerSerial)
    if container.ItemID in typeArray:
        ret_list.append(container)
        return ret_list
    if container != None:
        if "sending" in Items.GetPropStringByIndex(container, 0).lower():
            return ret_list
        if "spellbook" in Items.GetPropStringByIndex(container, 0).lower():
            return ret_list
        Items.WaitForContents(container, 2000)
        for item in container.Contains:
            if item.ItemID in typeArray:
                ret_list.append(item)
            if item.IsContainer:                                        
                for tmp in findRecursive(item.Serial, typeArray):
                    ret_list.append(tmp)
    return ret_list
#
def FindSendingBag():
    allBags = findRecursive(Player.Backpack.Serial, [ BagOfSendingID ])
    for bag in allBags:
        if "sending" in Items.GetPropStringByIndex(bag, 0).lower():
            return bag
    return None
    
def UseSendingBag(item):
    bag = FindSendingBag()
    if bag:
        Items.UseItem(bag)
        Target.WaitForTarget(2000)
        if Target.HasTarget():
            Target.TargetExecute(item)
            return
    Player.HeadMessage(5, "Unable to send gold")                    
#
import re
golds = findRecursive(Player.Backpack.Serial, ItemsIDsToSend)
for gold in golds:
    goldCount = re.match("(\d+)\s+gold coin", str(gold.Properties[0]))
    if goldCount:        
        amount = int(goldCount.group(1))
        if amount > GoldAmountToSend:
            UseSendingBag(gold)
    