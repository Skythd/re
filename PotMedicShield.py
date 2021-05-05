Items.WaitForContents(Player.Backpack,1000)

hpDown = 10   # hits down to start bandage
healHits = 75 # total hp for heal potion
refresh = 120 # stam for refresh pot
dex = 127     # dex for dex pot
str = 119     # str for str pot

HealingSkill = True  ### set BOOL FALSE IF NO HEALING

healPot = 0x0F0C
curePot = 0x0F07
strPot = 0x0F09
dexPot = 0x0F08
apple = 0x2FD8
bandage = Items.FindByID(0x0E21,-1,-1)

def drinkPot(potID):  #no UO3D
    if Player.Visible and Target.HasTarget() == False:
        Misc.Pause(100)
        if Items.BackpackCount(potID,-1) > 0:
            #Misc.SendMessage('pot found')
            if Player.CheckLayer('LeftHand') == False:
                Items.UseItemByID(potID,-1)
                Misc.Pause(400)
            else:
                Dress.ChangeList('onehand')
                Dress.DressFStart()
                Misc.Pause(1500)
                Items.UseItemByID(pot,-1)
                Misc.Pause(200)
        
            
def arm():        
    if not Player.Poisoned and Player.CheckLayer('LeftHand') == False:
        Misc.Pause(1300)            
        Dress.ChangeList('arm')
        Dress.DressFStart()
        
def rearm():        
    if Journal.SearchByType("Your confusion has passed, you may now arm a weapon!","System"):
        Dress.ChangeList('arm')
        Dress.DressFStart()
        Journal.Clear()
         
while not Player.IsGhost:
    #Misc.SendMessage('Cycled',30)   # cycle check
    rearm()
    if apple:
        if Timer.Check("appletimer") == False:
            if Player.BuffsExist('Mortal Strike') or Player.BuffsExist('Sleep'):
                Items.UseItemByID(apple.ItemID,-1)
                Timer.Create("appletimer", 30500)
                Misc.Pause(400)
            
    if Timer.Check("healpottimer") == False:    
        if Player.Hits <= healHits and not Player.Poisoned and not Player.BuffsExist('Mortal Strike'):         
            drinkPot(healPot)
            Timer.Create('healpottimer',3000)
            arm()
        
    if Player.Poisoned and not Player.BuffsExist('Mortal Strike'):
        Player.HeadMessage(30,'poisoned')
        drinkPot(curePot)
        Misc.Pause(100)
        if not Player.Poisoned:
            arm()
        
    if Player.Hits == Player.HitsMax:
        if Player.Dex < dex or Player.Str < str:
            if Player.Dex < dex:
                drinkPot(dexPot)
            if Player.Str < str:
                drinkPot(strPot)
            else:
                arm()
                

    
    if Timer.Check('bTimer') == False and HealingSkill == True:
        
        if Player.HitsMax - Player.Hits >= hpDown or Player.Poisoned and not Player.BuffsExist('Mortal Strike'):
            if bandage:
                Items.UseItemOnMobile(bandage,Player.Serial)
                if Player.Dex >= 140:
                    Timer.Create('bTimer',5900)
                elif Player.Dex >= 120:
                    Timer.Create('bTimer',4900)
                elif Player.Dex >= 100:
                    Timer.Create('bTimer',3900)
                elif Player.Dex >= 80:
                    Timer.Create('bTimer',2900)
                elif Player.Dex >= 60:
                    Timer.Create('bTimer',1900) 
            else:
                Player.HeadMessage(48,'No Bandages')
                Misc.Pause(2000)
        else:
            Timer.Create('bTimer',10)
            
    Misc.Pause(750) #Cycle Delay
        

  