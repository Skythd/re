while not Player.IsGhost:



    
    while Player.Visible:
        
#healstone
        
        if Player.Hits  < Player.HitsMax -80:       
            Items.UseItemByID (0x4078)
            
            
#sheild   rearm 

      
        if Player.CheckLayer('LeftHand') == False and Player.BuffsExist ("norearm"):
            Player.ChatSay(52, "left")    
            Player.EquipItem(0x45AE8B77)
            Misc.Pause (100)
           

        if Player.CheckLayer('RightHand') == False and not Player.BuffsExist ("norearm"):
            Player.ChatSay(52, "right")    
            Player.EquipItem(0x45BD019D)
            Misc.Pause (100)
            
        if Player.CheckLayer('RightHand') == True and Player.CheckLayer('LeftHand') == True:
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause (100)
           
            
#prep skills            

        if not Player.BuffsExist("Protection"): 
            Spells.CastMagery("Protection")
            Misc.Pause( 5000 )
            
        if not Player.BuffsExist("Stone Form"):
           Spells.CastMysticism("Stone Form")
           Misc.Pause( 5000 )
           
#Healing          
           
                
        if Player.Hits  < Player.HitsMax -10:
            Spells.CastBushido("Confidence")
            Misc.Pause( 1000 )
                
                
        if Player.Hits  < Player.HitsMax -80:       
            Items.UseItemByID (0x4078)
          

        if Player.Hits  < Player.HitsMax -30:
                Spells.CastMysticism("Cleansing Winds")
                Player.ChatSay(52, "Group heal") 
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(Player.Serial)
#                Misc.Pause( 1500 )
#                Spells.CastBushido("Confidence")
#                Misc.Pause( 1000 )


                
                
        if Player.Hits <= 80 and Player.Visible and not Player.Poisoned and not Player.BuffsExist('Mortal Strike'):                   
            Player.ChatSay(52, "Selfish heal") 
            Spells.CastMagery("Greater Heal")
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(Player.Serial)
            Misc.Pause( 1500 )
            Spells.CastBushido("Confidence")
            Misc.Pause( 1000 )
