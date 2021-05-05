horse = Target.PromptTarget()
while True:    
    bottles = Items.FindByID(0x0F0E,-1,Player.Backpack.Serial)
    if bottles:
        Items.Move(bottles,horse,0)
    Player.UseSkill("Stealing")
    Target.WaitForTarget(1000)
    Target.TargetExecute(horse)
    Misc.Pause(10600)