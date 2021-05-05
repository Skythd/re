from time import sleep
from datetime import datetime
import clr, time, thread, sys, System

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')

from System.Threading import ThreadStart, Thread
from System.Collections.Generic import List
from System import Byte
from System import Environment
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, BorderStyle, Label, FlatStyle, DataGridView,
 DataGridViewAutoSizeColumnsMode, DataGridViewSelectionMode, DataGridViewEditMode, RadioButton, GroupBox,
 TextBox, CheckBox, ProgressBar)
from System.Data import DataTable

import sys

bagofsedingID = 0x0E76
goldid = 0x0EED
nemico = Mobiles.FindBySerial(Target.GetLast())
enemy = Target.GetLast()
def Bagofseding():
 while Player.Gold > 25000 and Player.Weight > 450:
  for item in Player.Backpack.Contains:
     if item.ItemID == goldid:
        Items.UseItemByID(bagofsedingID)
        Target.WaitForTarget(1400, True)
        Target.TargetExecute(item.Serial)
        Misc.Pause(100)
def FRun():
    Bagofseding()
    
    nemico = Mobiles.FindBySerial(Target.GetLastAttack())
    
    while Player.InRangeMobile(nemico,1) == False:
   
        if  Player.Position.Y == nemico.Position.Y and Player.Position.X == nemico.Position.X: 
            break
        if Player.Position.Y < nemico.Position.Y and Player.Position.X < nemico.Position.X:
            go = 'Down'
        elif Player.Position.Y > nemico.Position.Y and Player.Position.X > nemico.Position.X:
            go = 'Up'
        elif Player.Position.Y > nemico.Position.Y and Player.Position.X < nemico.Position.X:
            go = 'Right'         
        elif Player.Position.Y < nemico.Position.Y and Player.Position.X > nemico.Position.X:
            go = 'Left'
        elif Player.Position.Y > nemico.Position.Y and Player.Position.X == nemico.Position.X:
            go = 'North'
        elif Player.Position.Y < nemico.Position.Y and Player.Position.X == nemico.Position.X:
            go = 'South'          
        elif Player.Position.X > nemico.Position.X and Player.Position.Y == nemico.Position.Y:
            go = 'West'         
        elif Player.Position.X < nemico.Position.X and Player.Position.Y == nemico.Position.Y:
            go = 'East'
        if Player.Direction == go:
            Player.Run(go, False)                
        else: 
                Player.Run(go, False)
                Player.Run(go, False)
        if Player.Position.X == Player.Position.X and Player.Position.Y == Player.Position.Y :
            Misc.Pause(5)
            
def honorNearest():
    if not Player.BuffsExist('Perfection') and nemico.Hits == 25:
        if nemico:
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(1000)
            Target.TargetExecute(nemico)
            Misc.Pause(100)
def CounterAttack():
 if not Player.BuffsExist('Counter Attack') and Player.Hits > 70:
       Spells.CastBushido('Counter Attack')
       Misc.Pause(200) 
 elif Player.Hits < 70 and  not Player.BuffsExist('Confidence'):
       Spells.CastBushido('Confidence')
       Misc.Pause(200)  
def Divine():   
    if Player.InRangeMobile(enemy, 2) == True:    
        if Player.Stam < 120 or not Player.BuffsExist("Divine Fury"):
                Spells.CastChivalry("Divine Fury")
                Misc.Pause(50)
def Bloodout():
    if Player.BuffsExist("Bload Oath (curse)"):    
        while Player.BuffsExist("Bload Oath (curse)"):
                Player.SetWarMode(False)
                Misc.Pause(50)
                while Player.BuffsExist("Counter Attack"):
                        Player.SetWarMode("OFF")
                        Spells.CastBushido("Confidence")
                        Player.SetWarMode(False)
                        Misc.Pause(50)
                Spells.CastChivalry("Remove Curse")
                Target.WaitForTarget(100)
                Target.SelfQueued()
                Player.SetWarMode(False)
                Misc.Pause(50)
        else:
            if not Player.BuffsExist("Bload Oath (curse)"):
                        Player.Attack(nemico)
                        Player.SetWarMode("on")

def ability():
   from System.Collections.Generic import List
   from System import Byte
   eNumber = 0
   fil = Mobiles.Filter()
   fil.Enabled = True
   fil.RangeMax = 2
   fil.Notorieties = List[Byte](bytes([4,5,3]))
   trovato = 0

   enemies = Mobiles.ApplyFilter(fil)
   enemy = Target.SetLastTargetFromList("closestenemy")

   for enemy in enemies:
    eNumber += 1
    if eNumber == 1:
       if not Player.HasSpecial and Player.Mana > 18:
        if not Player.BuffsExist("Feint"):
         Player.WeaponPrimarySA()
         Player.Attack(enemy)
        else:
            Player.WeaponSecondarySA()
            Player.Attack(enemy)
       else:
          if Player.Mana < 18:
           if not Player.BuffsExist('Lightning Strike') and Player.Mana > 2:
            Spells.CastBushido("Lightning Strike")
            Misc.Pause(50)
    else:
        if eNumber  > 1 and not Player.HasSpecial:
           Player.WeaponSecondarySA()
           Player.Attack(enemy)
           Misc.Pause(25) 
        
                
def consacrate():
    if not Player.BuffsExist('Consecrate Weapon') and Player.InRangeMobile(enemy, 2) == True:
            Spells.CastChivalry('Consecrate Weapon')
            Misc.Pause(10)
            
def arte():
    if Journal.SearchByName("For your valor", "system"):
             Player.HeadMessage(33,"Arte")
             Player.HeadMessage(33,"Arte")
             Player.HeadMessage(33,"Arte")
             Player.HeadMessage(33,"Arte")
             Journal.Clear() 
def CurseWeapon():   
    if Player.Hits < 80 and not Player.BuffsExist('Curse Weapon'):
            Spells.CastNecro('Curse Weapon')
            Misc.Pause(50)                    
                    
                
     
if Player.InRangeMobile(enemy, 1) == True:
  if not Player.BuffsExist("Bload Oath (curse)"):
      Player.Attack(nemico)
      Player.SetWarMode(True)
      Misc.Pause(5)
      Player.SetWarMode(True)      
  honorNearest()
  Misc.Pause(5)
  consacrate()
  Bloodout()
  Misc.Pause(5)
  arte()
  Misc.Pause(5)
  ability()
  Bloodout()
  Misc.Pause(5)
  Divine()
  Misc.Pause(5)
  Bloodout()
  Misc.Pause(5)
  CurseWeapon()
  Misc.Pause(5)
  CounterAttack()
  Misc.Pause(5)
  Bagofseding()
        
else:
    Player.Attack(enemy)
    if Player.InRangeMobile(enemy,1) == False and Player.InRangeMobile(enemy,18) == True :
      FRun()
      if not Player.BuffsExist('Perfection') and nemico.Hits == 25:
        honorNearest()
      Misc.Pause(15)
    else:
        if Player.InRangeMobile(enemy,24) == False:
          Bagofseding()
          Target.Cancel()
          Target.PerformTargetFromList("nearest")
          Misc.Pause(150)
          Player.Attack(nemico)
Misc.Pause(15)