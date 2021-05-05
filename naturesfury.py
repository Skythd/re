if Player.Mana > 18 and Player.Followers < Player.FollowersMax :
    Spells.CastSpellweaving("Natures Fury")
    Target.WaitForTarget(800, False)
    Target.TargetExecuteRelative(Player.Serial,1)
    if Player.Followers > 2:
       Misc.Pause(500)
