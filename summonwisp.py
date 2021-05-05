fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 2
followers = Mobiles.ApplyFilter(fil)
dispelled = False
for f in followers:
    if f.Body == 0x00A5:
        Misc.WaitForContext(f.Serial, 9000)
        Misc.ContextReply(f.Serial, 0)
        dispelled = True
        Misc.Pause(500)
        break
        
if not dispelled:
    Gumps.ResetGump()
    Spells.CastNecro("Summon Familiar")
    Gumps.WaitForGump(545409390, 9000)
    Gumps.SendAction(545409390, 2)