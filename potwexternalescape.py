#Explode pot tosser
msgcolor = 53
serial = Target.GetLast()
#serial = Target.GetLastAttack()
boomtarget = Mobiles.FindBySerial(serial)
self = Player.Serial

Target.Cancel()
Journal.Clear()


def potThrow():
    if Items.BackpackCount(0x0F0D, -1) == 0:
        Player.HeadMessage(msgcolor, 'Out of Exp pots')
        return False

    else:
        bomb = Items.FindByID(0x0F0D, -1 , Player.Backpack.Serial)
        #Items.UseItemByID(0x0F0D, -1)
        Items.UseItem(bomb)
        while not Target.HasTarget( ):
            Misc.Pause( 1 )
        Misc.ScriptRun('pressescape.py')

    Player.HeadMessage(msgcolor, 'Charging')
    while not Journal.SearchByName( '2', Player.Name ):
        Misc.Pause( 50 )
    Misc.Pause(200)
    Player.HeadMessage(msgcolor, 'Tossing!')
    
    Items.UseItem(bomb)
    while not Target.HasTarget( ):
            Misc.Pause( 1 )
    while Target.HasTarget( ):
        pottarget = Target.GetLast()
        z = Mobiles.FindBySerial( pottarget )
        if Player.DistanceTo(z) >= 12:
            Player.HeadMessage(msgcolor, 'Out of range, dumping!')
            Target.TargetExecuteRelative(Player.Serial, -5)
        else:
            Misc.Pause(100)
            pottarget = Target.GetLast()
            Target.TargetExecute(pottarget)
        if Journal.Search('cannot be seen.'):
            Player.HeadMessage(msgcolor, 'Target not seen, dumping!')
            Target.TargetExecuteRelative(Player.Serial, -5)
            
            
potThrow()