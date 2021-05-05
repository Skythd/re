if Player.Mana > 40:
    Items.UseItem(0x40087CC6)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 13)
Misc.Pause(800)