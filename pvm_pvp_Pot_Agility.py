leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 800
msgColor = 66
noBow = True
bows = [0x13B2,0x26C2,0x0F50,0x13FD]
basedex = 101

if not leftHand:
    noBow = True
elif leftHand.ItemID in bows:
    noBow = False
elif leftHand:
    noBow = True
    
Journal.Clear()
if Player.Dex < basedex:
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(650)
        Player.ChatSay( 1 , '[drink greaterAgilityPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Agility pots!")
        Misc.Pause(chugtime)
        Player.EquipItem(leftHand)
        Misc.Pause(50)
    else:
        Player.ChatSay( 1 , '[drink greaterAgilityPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Agility pots!")
        else:
            Misc.NoOperation()
else:
    Player.HeadMessage(msgColor, "Full Dex Buff")