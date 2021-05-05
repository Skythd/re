"""
================ Inscription Trainer ================
=                   by Cookie Lover                 = 
=           Latest Release: 06/17/2017              =
=                                                   =
=   What you need:                                  =
=   - a chest with ingots, reagents and blank       =
=     scrolls                                       =
=   - at least 30.0 inscription                     =
=====================================================
"""

class Scroll:
    ID = Cat = Sub = MP = 0
    Reag = []    
    def __init__(self, typ, reag, mana, cat, sub):
        self.ID = typ
        self.Reag = reag
        self.Cat = cat
        self.Sub = sub
        self.MP = mana
        
class InscriptionTrainer:
    Scrolls = {
        'lightning' : Scroll(0x1F4A, [0x0F86, 0x0F8C], 11, 22, 37),
        'magic reflection' : Scroll(0x1F50, [0x0F84, 0x0F86, 0x0F8D], 14, 29, 23),
        'invisibility' : Scroll(0x1F58, [0x0F7B, 0x0F88], 20, 36, 23),
        'flamestrike' : Scroll(0x1F5F, [0x0F8D, 0x0F8C], 40, 43, 16),
        'resurrection' : Scroll(0x1F67, [0x0F7B, 0x0F84, 0x0F85], 50, 50, 16)
        }
    
    CHEST = 0
    OnGoing = True
    SCROLL = 0
    
    def SetChest(self):
        Misc.SendMessage("Target the container you wish to restock with.", 50)
        c = Target.PromptTarget()
        Items.WaitForContents(Items.FindBySerial(c), 5000)
        self.CHEST = c
        
    def KitCraft(self):
        Gumps.ResetGump()
        while Items.BackpackCount(0x1eb8, 0) < 2:
            Items.UseItemByID(0x1eb8, 0)
            Gumps.WaitForGump(949095101, 5000)
            if not Gumps.LastGumpTextExist("scissors"):
                Gumps.SendAction(949095101, 8)
                Gumps.WaitForGump(949095101, 5000)
            Gumps.SendAction(949095101, 23)
            Gumps.WaitForGump(949095101, 5000)
    
    def SPCraft(self):
        Gumps.ResetGump()
        while Items.BackpackCount(0x0FBF, 0) == 0:
            Items.UseItemByID(0x1eb8, 0)
            Gumps.WaitForGump(949095101, 5000)
            if not Gumps.LastGumpTextExist("scissors"):
                Gumps.SendAction(949095101, 8)
                Gumps.WaitForGump(949095101, 5000)
            Gumps.SendAction(949095101, 156)
            Gumps.WaitForGump(949095101, 5000)
            
    def CheckResources(self):
        if Items.BackpackCount(0x1BF2, 0) < 10:
            return False
        if Items.BackpackCount(0x0EF3, 0) == 0:
            return False
        for ingr in self.SCROLL.Reag:
            if Items.BackpackCount(ingr, 0) == 0:
                return False
        return True
        
    def CheckChest(self):
        if Items.ContainerCount(self.CHEST, 0x1BF2, 0) < 10:
            return False
        if Items.ContainerCount(self.CHEST, 0x0EF3, 0) == 0:
            return False
        for ingr in self.SCROLL.Reag:
            if Items.ContainerCount(self.CHEST, ingr, 0) == 0:
                return False
        return True
        
    def Restocka(self):        
        for ingr in self.SCROLL.Reag:
            for itm in Items.FindBySerial(self.CHEST).Contains:
                ingots = Items.BackpackCount(0x1BF2, 0) 
                reag = Items.BackpackCount(ingr, 0)
                scrolls = Items.BackpackCount(0x0EF3, 0)
                if ingots < 100 and itm.ItemID == 0x1BF2:
                    if itm.Amount >= 100 - ingots:
                        Items.Move(itm, Player.Backpack, 100 - ingots)
                    else:
                        Items.Move(itm, Player.Backpack, 0)
                    Misc.Pause(700)
                    continue
                if reag < 100 and itm.ItemID == ingr:
                    if itm.Amount >= 100 - reag:
                        Items.Move(itm, Player.Backpack, 100 - reag)
                    else:
                        Items.Move(itm, Player.Backpack, 0)
                    Misc.Pause(700)
                    continue
                if scrolls < 100 and itm.ItemID == 0x0EF3:
                    if itm.Amount >= 100 - scrolls:
                        Items.Move(itm, Player.Backpack, 100 - scrolls)
                    else:
                        Items.Move(itm, Player.Backpack, 0)
                    Misc.Pause(700)
                    
    def Destocka(self, num = 10):
        scrolls = [v.ID for k,v in self.Scrolls.iteritems()]
        for scroll in scrolls:
            if Items.BackpackCount(scroll, 0) >= num:
                itm = next(i for i in Player.Backpack.Contains if i.ItemID == scroll)
                if not itm is None:
                    Items.Move(itm, self.CHEST, 0)
                    Misc.Pause(700)
                
    def ScrollCraft(self):
        try:
            if not self.CheckChest():
                self.OnGoing = False
                return
            if not self.CheckResources():
                self.Restocka()
            self.KitCraft()
            self.SPCraft()
            while Player.Mana < self.SCROLL.MP:
                Misc.Pause(500)
            Gumps.ResetGump()
            Items.UseItemByID(0x0FBF, 0)
            Gumps.WaitForGump(949095101, 5000)
            Gumps.SendAction(949095101, self.SCROLL.Cat)
            Gumps.WaitForGump(949095101, 5000)
            Gumps.SendAction(949095101, self.SCROLL.Sub)
            Gumps.WaitForGump(949095101, 5000)

        except KeyError:
            Player.HeadMessage(33, "Error: no scroll with that key")
            return False
            
    def Main(self):
        while Player.GetSkillValue("Inscribe") < 100.0 and self.OnGoing == True:
            scribe = Player.GetSkillValue("Inscribe")
            if 30.0 <= scribe < 55.0:
                self.SCROLL = self.Scrolls['lightning']
            elif 55.0 <= scribe < 65.0:
                self.SCROLL = self.Scrolls['magic reflection']
            elif 65.0 <= scribe < 85.0:
                self.SCROLL = self.Scrolls['invisibility']
            elif 85.0 <= scribe < 94.0:
                self.SCROLL = self.Scrolls['flamestrike']
            elif 94.0 <= scribe < 100.0:
                self.SCROLL = self.Scrolls['resurrection']
            
            self.ScrollCraft()
            self.Destocka()    
   
## CALL ##
IT = InscriptionTrainer()
IT.SetChest()
IT.Main()   
IT.Destocka(0)       
