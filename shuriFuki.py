#########  shuriken and fukiya reloader and distance checker by Mourn #8182 discord contact



if Items.BackpackCount(0x2790,-1) > 0:
    belt = Items.FindByID(0x2790,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Ninja Belt',38)
if Items.BackpackCount(0x27AA,-1) > 0:    
    fuk = Items.FindByID(0x27AA,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Fukiya',38) 
if Items.BackpackCount(0x2806,-1) > 0:    
    fukdart = Items.FindByID(0x2806,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Fukiya Darts in bag',38) 
if Items.BackpackCount(0x27AC,-1) > 0:
    shur = Items.FindByID(0x27AC,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Shuriken in bag',38) 
    

def uses():
    beltprops = Items.GetPropStringList(belt)
    for beltprop in beltprops:
        if beltprop.split(' ')[0] == 'uses':
            sUses = beltprop.split(' ')[2]
            Misc.SendMessage(sUses + ' Shuriken in belt',82)
            if int(sUses) == 0:
                Misc.WaitForContext(belt.Serial, 3000)
                Misc.ContextReply(belt.Serial, 701)
                Target.WaitForTarget(2000,False)
                Target.TargetExecute(shur.Serial)
                Misc.SendMessage('Loading Shuriken',82)
            
    fukprops = Items.GetPropStringList(fuk)
    for fukprop in fukprops:
        if fukprop.split(' ')[0] == 'uses':
            fUses = fukprop.split(' ')[2]
            Misc.SendMessage(fUses + ' Darks in fukiya',82)    
            if int(fUses) == 0:
                Misc.WaitForContext(fuk.Serial, 3000)
                Misc.ContextReply(fuk.Serial, 703)
                Target.WaitForTarget(2000,False)
                Target.TargetExecute(fukdart.Serial)
                Misc.SendMessage('Loading Fukiya',82)
                
                
def attack():
    
    target = Target.GetLast()
    enemy = Mobiles.FindBySerial(target)
    if enemy == None:
        target = Target.PromptTarget('Need Target')
        enemy = Mobiles.FindBySerial(target)
        Mobiles.Message(enemy,46,'Target')
    if Player.DistanceTo(enemy) < 5:
        Items.UseItem(fuk)
        Target.WaitForTarget(2000,False)
        Target.TargetExecute(enemy)
    if Player.DistanceTo(enemy) >= 5 and Player.DistanceTo(enemy) <= 10:
        Items.UseItem(belt)
        Target.WaitForTarget(2000,False)
        Target.TargetExecute(enemy)
    
                        
uses()
attack()
