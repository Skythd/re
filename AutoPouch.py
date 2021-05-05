"""
================= Auto Pouch =================
=               by Cookie Lover              =
=           Latest Release: 06/14/2017       =
=                                            =            
=   What you need:                           =
=   - magically trapped pouches              =
=   - greater heal pots, otherwise, set      =
=     DrinkPot to False                      =
==============================================
"""
class AutoPouch:
    Trapped = []
    DrinkPot = True
    def __init__(self):
        self.Trapped = [i.Serial for i in Player.Backpack.Contains if i.ItemID == 0x0E79]

    def Main(self):
        while Player.Hits > 0:
            if Player.Paralized:
                if Player.Hits < 80 and self.DrinkPot:
                    pots = Items.BackpackCount(0x0F0C, 0)
                    pot = next(i for i in Player.Backpack.Contains if i.ItemID == 0x0F0C)
                    if not pot:
                        Player.HeadMessage(33, "You used up all your GHeals.")
                        self.DrinkPot = False
                    else:
                        if pots < 5:
                            Player.HeadMessage(33, "GHeal: {0} left.".format(pots))
                        Items.UseItem(pot)
                        Misc.Pause(500)
                if Player.Hits >= 80:
                    if self.Trapped != []:
                        Items.UseItem(self.Trapped[0])
                        del(self.Trapped[0])
                        Misc.Pause(500)
                    else:
                        Player.HeadMessage(33, "You used up all your pouches!")
                        break

            Misc.Pause(500)
    

ap = AutoPouch()
ap.Main()
