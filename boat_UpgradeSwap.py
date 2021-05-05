from System.Collections.Generic import List
from System import Byte
import math
import time

actionDelay = 700
upgradeDeed = 0x14F0

if Misc.CheckSharedValue('UpgradeDeedBag') == False:
    Misc.SetSharedValue('UpgradeDeedBag', Target.PromptTarget())
upgradeBag = Misc.ReadSharedValue('UpgradeDeedBag')

tillergalfil = Mobiles.Filter()
tillergalfil.Enabled = True
tillergalfil.RangeMax = 6
#tillergalfil.Serials = tillergalfilIDs
tillergalfil.Notorieties = List[Byte](bytes([7]))
tillergalfil.CheckIgnoreObject = False

tillergal = []
tillergal = Mobiles.ApplyFilter(tillergalfil)
tillergalman = Mobiles.Select(tillergal, "Nearest")


tillerFilter = Items.Filter()
tillerFilter.Enabled = True
tillerFilter.OnGround = True
tillerFilter.Movable = False
tillerFilter.RangeMax = 6
tillerFilter.Graphics = List[int]( [ 0x3E4E,0x3E4B,0x3E55,0x3E50 ] )

tiller = Items.ApplyFilter( tillerFilter )
tillerMan = Items.Select ( tiller , 'Nearest')


if Gumps.HasGump:
    Gumps.CloseGump(3821575966)
    Misc.Pause(150)
    Gumps.CloseGump(1611080882)
    Misc.Pause(150)
    Gumps.CloseGump(3884316545)
    Misc.Pause(150)
    
if Player.Mount:
    Mobiles.UseMobile(Player.Serial)
    Misc.Pause(actionDelay)    

if upgradeDeed:
    deed = Items.FindByID(upgradeDeed, 0x0a66 , upgradeBag)
    if tillerMan:
        Items.UseItem(tillerMan)
    elif tillergalman:
        Mobiles.UseMobile(tillergalman)
    if Gumps.HasGump():
        Gumps.CloseGump(Gumps.CurrentGump())
    Gumps.WaitForGump(3821575966, 1000)
    Gumps.SendAction(3821575966, 1)
    Gumps.WaitForGump(1611080882, 1000)
    Gumps.SendAction(1611080882, 5)
    Gumps.WaitForGump(3884316545, 1000)
    Gumps.SendAction(3884316545, 2)
    if Gumps.HasGump:
        Gumps.CloseGump(3821575966)
        Misc.Pause(150)
        Gumps.CloseGump(1611080882)
        Misc.Pause(150)
        Gumps.CloseGump(3884316545)
        Misc.Pause(150)
    Items.UseItem(deed)
    Target.WaitForTarget(600, False)
    if tillerMan:
        Target.TargetExecute(tillerMan)
    elif tillergalman:
        Target.TargetExecute(tillergalman)
    Misc.Pause(600)
    
for r in Player.Backpack.Contains:
    if r.ItemID == 0x14F0 and r.Hue == 0x0a66:
        Items.Move(r, upgradeBag, 1)    
        Misc.Pause(600)