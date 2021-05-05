#===========================================#
#        Drop Shield and Chug Example       #
#===========================================#
#                                           #
#   Author: Abigor                          #
#   Release Date: 11/17/20                  #
#                                           #
#===========================================#
#                                           #
#   Info:                                   #
#       Set the timers according to your    #
#       Personal Prefs.  This is meant as   #
#       as an example of how to chug while  #
#       having both hands full, but can be  #
#       modified to handle all sorts of     #
#       drop-shield duties.                 #
#                                           #
#===========================================#


leastHits = Player.HitsMax * .99    #Percentage of full health to start healing.   .8 is 80% 
movepause = 980                    #Pause between moving items.  Depends on latency
healpause = 15000                  #pause between chugging heals
potpause = 980                     #general chugging pause.. 

lhand = Player.GetItemOnLayer('LeftHand')

while True:
    if Player.Hits < leastHits and Player.Visible == True:
        if Items.BackpackCount(0x0F0C, -1) > 0 and Timer.Check("healtimer") == False:
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause(movepause)
            Misc.SendMessage("Heal Pot")
            Items.UseItemByID(0x0F0C, -1)
            Misc.Pause(movepause)
            while True:
                if Player.GetItemOnLayer('LeftHand')!= lhand:
                    Player.EquipItem(lhand)
                    Misc.Pause(2000)
            Timer.Create("healtimer", healpause)
            Misc.Pause(potpause)
Misc.Pause(800)