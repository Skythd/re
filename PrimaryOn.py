#===========================================#
#   Primary & Secondary Weapon Ability      #
#===========================================#
#                                           #
#   Author: Abigor                          #
#   Release Date: 3/20/2020                 #
#                                           #
#===========================================#
#                                           #
#   Info:                                   #
#   - must have both PrimaryOn.py and       #
#     SecondaryOn.py files in your script-  #
#     ing list.                             #
#   - set hot keys for each script          #
#   - will pause below 20 man, set your     #
#     minimum on line 22                    #
#===========================================#

Misc.ScriptStop('SecondaryOn.py')
Misc.ScriptStop('DeathStrikeOn.py')
Misc.ScriptStop('EvasionOn.py')
Misc.ScriptStop('FocusAttackOn.py')

while True:
    if not Player.HasSpecial and Player.Mana >= 20:
        Player.WeaponPrimarySA()
        