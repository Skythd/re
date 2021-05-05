from System.Collections.Generic import List
#put bottles on scavenger
piratefil = Mobiles.Filter()
piratefil.Enabled = True
piratefil.Bodies = List[int]((0x0190,0x0190))
piratefil.RangeMax = 50

def getwinedrunk():    
    wine = Items.FindByID(0x09C7,-1,Player.Backpack.Serial)
    if wine:
        chugs = 0
        Player.HeadMessage(30,'I Brought My Own Shit')
        while chugs <= 5:
            Items.UseItem(wine.Serial)
            Target.WaitForTarget(2000,False)
            Target.Self()            
            chugs +=1
            Journal.Clear()
            Misc.Pause(1500)
        
def throwbottle():        
    pirates = Mobiles.ApplyFilter(piratefil)
    Misc.Pause(100)
    pirate = Mobiles.Select(pirates,'Nearest')
    if Items.BackpackCount(0x099B) > 0 and Player.Hits > 40 and pirate != None:
        Items.UseItemByID(0x099B,-1)
        Target.WaitForTarget(500,False)
        Target.TargetExecute(pirate)
        Misc.Pause(800)
    if Items.BackpackCount(0x099B) == 0:
        Misc.SendMessage(str(Items.BackpackCount(0x099B))+' Bottles Left',43)
    if pirate == None:
         Misc.SendMessage('No Pirates in Range',43)
if not Misc.ReadSharedValue("predrink"):
    getwinedrunk()
    Misc.SetSharedValue("predrink",True)
if Journal.Search('sober.') == True:
    getwinedrunk()
else:
    throwbottle()
