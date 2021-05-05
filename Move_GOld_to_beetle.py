beetle = 0x0017A5E9
bag = 0x41001F8C
gold = Items.FindByID(0x0EED, -1, bag)
dragtime = 600
self = Player.Serial

if Player.Mount: 
    Mobiles.UseMobile(self)
    Misc.Pause(600)
    Items.Move(gold, beetle, 0)
    Misc.Pause(600)
    Mobiles.UseMobile(beetle)
    Misc.Pause(100)

    
 