Misc.SendMessage("Taming Started", 33)
#Journal.Clear()
while True:
    Misc.Pause(50)
    tametarget = Target.GetTargetFromList("tames")
    Player.SetWarMode(True)
    Player.SetWarMode(False)
    if not tametarget and Timer.Check('attacker') == False:
        Target.AttackTargetFromList('greyclosest')
        Timer.Create('attacker', 1000)
        Player.SetWarMode(True)
        Player.SetWarMode(False)
    if tametarget:
        if Player.Poisoned and Timer.Check('skilltimer') == True:
            Spells.CastMagery("Cure")
            Target.WaitForTarget(1000)
            Target.Self()
        if Player.Hits < 81 and Timer.Check('skilltimer') == True:
            Player.HeadMessage(33, "**Healing Self**")
            Spells.CastMagery("Heal")
            Target.WaitForTarget(1000)
            Target.Self()
        if tametarget.WarMode:
            Player.SetWarMode(False)
            if Timer.Check('skilltimer') == False and Timer.Check('tametimer') == False:
                Target.ClearQueue()
                Misc.Pause(100)
                Target.Cancel()
                Misc.Pause(50)
                Player.UseSkill("Peacemaking")
                Target.WaitForTarget(1000)
                Target.TargetExecute(tametarget.Serial)
                Player.HeadMessage(77, "Peacemaking")
                Player.SetWarMode(False)
                Timer.Create('skilltimer', 5500)
            else:
                Misc.NoOperation()
        if not tametarget.WarMode:
            Player.SetWarMode(False)
            if Timer.Check('skilltimer') == False and Timer.Check('tametimer') == False:
            #while Timer.Check('tametimer') == False:
                Player.SetWarMode(False)
                Target.ClearQueue()
                Misc.Pause(100)
                Target.Cancel()
                Misc.Pause(50)
                Player.UseSkill("Animal Taming")
                Target.WaitForTarget(1000)
                Target.TargetExecute(tametarget.Serial)
                Mobiles.Message(tametarget.Serial, 77,"Taming")
                Timer.Create('tametimer', 13000)
                Misc.Pause(200)
            else:
                Misc.NoOperation()
        if Journal.Search("fail to tame"):
            Player.HeadMessage(33, "**FAILED***")
            Timer.Create('tametimer', 1)
            Journal.Clear()
        else:
            Misc.NoOperation()
        if Journal.Search("seems to accept you as master") or Journal.Search("looks tame already"):
            Timer.Create('tametimer', 5000)
            Player.ChatSay(55, "all stay")
            Misc.Beep()
            Journal.Clear()
            Spells.CastMagery("Explosion")
            Target.WaitForTarget(3000)
            Target.TargetExecute(tametarget.Serial)
            Misc.Pause(800)
            Spells.CastMagery("Energy Bolt")
            Target.WaitForTarget(3000)
            Target.TargetExecute(tametarget.Serial)
            Misc.Pause(800)
            if 'lizard' in tametarget.Name: 
                Spells.CastMagery("Lightning")
                Target.WaitForTarget(3000)
                Target.TargetExecute(tametarget.Serial)
            Misc.Pause(2000)
        else:
            Misc.NoOperation()
    elif Timer.Check('closer') == False:
        Player.HeadMessage(55, "NO TARGET GET CLOSER")
        Timer.Create('closer', 1500)
    else:
        Misc.NoOperation()
            
            
            
        
    