
if Items.BackpackCount(0x0FF6,0x0000)>=1:
    x=0
    xmax = Items.BackpackCount(0x0FF6,0x0000)
    while x < xmax:
        Items.UseItemByID(0x0FF6,0x0000)
        Target.WaitForTarget(500,False)
        Target.TargetExecute(0x402B95EE)
        Misc.Pause(100)
        x=x+1
else:
    Misc.ScriptStop("riempibrocca.py")