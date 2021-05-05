"""
================ Expiring SOPs ================
=               by Cookie Lover               =
=           Latest Release: 06/14/2017        =
===============================================
"""
sopchest = []
# for i in xrange(ContainerCount): in case you want to use more containers
chest = Target.PromptTarget()
sopchest.append(chest)   
for c in sopchest:
    Items.WaitForContents(Items.FindBySerial(c), 5000)
    sops = [i for i in Items.FindBySerial(c).Contains if i.ItemID == 0x14F0]
    if not sops: continue
    for sop in sops:
        Items.WaitForProps(sop, 5000)
        days = int(list(i for i in Items.GetPropStringList(sop))[-1].replace(" days until deletion", ""))
        if days < 20:
            Items.Move(sop, Player.Backpack, 0)
            Misc.Pause(700)