pname = Player.Name.lower().replace(' ', '')

if pname == 'plushrush':
    Tallyserial = 0x40C87041
elif pname == 'silentnox':
    Tallyserial = 0x40758A3B
elif pname == 'gloompox':
    Tallyserial = 0x448FAB0F

# True = will track XP only since running the script
# False = will track XP since running script since launch of Enhanced,
#         so if you stop/restart script it'll still track starting xp
trackOnScript = False
    
minxp = 0
counter = 0
currentxp = 0
Items.UseItem(Tallyserial)
Misc.Pause(600)
temp = Gumps.LastGumpGetLine(4)
temp = temp.split("/", 1)[0]
currentxp = int(temp)

if trackOnScript:
    startingxp = currentxp
    Misc.SendMessage('Starting XP: ' + startingxp, 33)
else:
    if Misc.CheckSharedValue( pname + 'xp' ):
        startingxp = Misc.ReadSharedValue( pname + 'xp' )
        Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)
    else:
        startingxp = currentxp
        Misc.SetSharedValue( pname + 'xp', startingxp )
        Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)

def hasInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

while True:
    Gumps.ResetGump()
    Items.UseItem(Tallyserial)
    Misc.Pause(600)
    temp = Gumps.LastGumpGetLine(4)
    temp = temp.split("/", 1)[0]
    if hasInt(temp):
        newxp = int(temp)
    difference = newxp - currentxp
    if difference > 0:
        Player.HeadMessage(54, 'Gained ' + str(difference) + ' xp')
        currentxp = newxp
    Misc.Pause(6000)
    minxp = difference + minxp 
    counter = counter + 1
    if counter >= 10:
        overallxp = currentxp - startingxp
        if minxp > 0:
            Player.HeadMessage(54, 'Gained ' + str(minxp) + ' xp per min')
            Misc.Pause(200)
        Player.HeadMessage(44, str(overallxp) + 'xp total.')
        counter = 0
        minxp = 0
    
    

