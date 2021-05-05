from System.Collections.Generic import List
from System import Byte

usePets = False
move = False
targetingRange = 1
honor = True




StartWep = Player.GetItemOnLayer("LeftHand")
startX = Player.Position.X
startY = Player.Position.Y
startZ = Player.Position.Z

def WeaponSetup():
    global targetingRange
    #Misc.SendMessage("Detecting Weapon Type")
    wep = Player.GetItemOnLayer("LeftHand")

    if wep != None:
        typeCount = len(wep.Properties)
        index = typeCount - 2
        if typeCount > 5 and wep.Properties[index]!= None:
            search = str(wep.Properties[index])
            if search.find("Ranged") != -1:
                #Misc.SendMessage("Setting Range to 7")
                targetingRange = 7
            elif search.find("Melee") != -1:
                targetingRange = 1
                #Misc.SendMessage("Setting Range to 1")
                
    else:
        #Misc.SendMessage("Defaulting Range to 1")
        targetingRange = 7
                               
def SendPets(e):
    if usePets:
        if Player.Followers > 1:
            if not(Timer.Check("PetAttack")):
                Player.ChatSay(690, "All Kill")
                Target.WaitForTarget(300, False)
                Target.TargetExecute(e)
                Timer.Create("PetAttack", 4000 )
                
            
def MoveToEnnemy(e):
    if move:
        Player.PathFindTo(e.Position.X, e.Position.Y, e.Position.Z)
        Misc.Pause(1000)
        
def FindEnemies():
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.RangeMax = targetingRange
    fil.Friend = -1
    enemies = Mobiles.ApplyFilter(fil)
    return enemies
        
def honor(e):
    if honor:
        if not(Timer.Check("honor")):
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(300, False)
            Target.TargetExecute(e)
            Timer.Create("honor", 5000 )
    
    
def Main():
    Misc.SendMessage(targetingRange)
    eNumber = 0
    while not Player.IsGhost:
        WeaponSetup()
        CurWep = Player.GetItemOnLayer("LeftHand")
        if CurWep != None:
            if StartWep.Name != CurWep.Name:
                Misc.SendMessage("Detected Weapon Change")
                break
        enemies = FindEnemies()
        enemy = Mobiles.Select(enemies,'Nearest')
        eNumber = len(enemies)
        
        if eNumber > 0:
            if not(Timer.Check("EOO")):
                Spells.CastChivalry("Enemy Of One")
                Misc.Pause(10)
                Timer.Create("EOO", 30000 )
            if not(Timer.Check("Divine")):
                Spells.CastChivalry("Divine Fury")
                Misc.Pause(10)
                Timer.Create("Divine", 10000 )
            if not(Timer.Check("Consecrate")):
                Spells.CastChivalry("Consecrate Weapon")
                Misc.Pause(10)
                Timer.Create("Consecrate", 10000 )
        
        if eNumber == 1:
            eNumber = 0
            if not Player.HasSpecial:
                if not(Timer.Check("Primary")):
                    Player.WeaponPrimarySA()
                    Timer.Create("Primary", 800 )
            honor(enemy)
            Player.Attack(enemy)
            MoveToEnnemy(enemy)
            SendPets(enemy)
        if eNumber == 2:
            eNumber = 0
            if not Player.SpellIsEnabled('Momentum Strike'):
                Spells.CastBushido('Momentum Strike')
            honor(enemy)
            Player.Attack(enemy)
            SendPets(enemy)
            MoveToEnnemy(enemy)
        if eNumber > 2 :
            eNumber = 0
            if not Player.HasSpecial:
                if not(Timer.Check("Secondary")):
                    Player.WeaponSecondarySA()
                    Timer.Create("Secondary", 800 )
            Player.Attack(enemy)
            SendPets(enemy)
            MoveToEnnemy(enemy)
        Misc.Pause(250)
Main()