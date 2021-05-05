from System.Collections.Generic import List
from math import sqrt
bladeList = [0xf52, 0xec4, 0x13f6, 0xec3]

runebook = 0x42D98AFC
homebook = 0x463A1704
feyweapon =0x42CC30FD
dragonweapon = 0x40B4CB5B
beetle = 0x0029CCA0
Tallyserial = 0x448FAB0F
slayerdaggermodel = 0x0EC4
sheild = 0x44D7795F




currentxp = 0


dragDelay = 750
step = 0
unloadbag = 0x41A9C32F
arrowmodel = 0x0F3F  
goldmodel = 0x0EED 
#leathermodel = 0x1079 #uncut
leathermodel = 0x1081 #cut
scalemodel = 0x26B4
daggermodel = 0x0F52

def webhook(msg):
    URI = 'https://discordapp.com/api/webhooks/654131394854781018/KySfeUnLjoFmqfmf154_1V22nxkzGnDmOP6-j8Kj__Ei8boMeHwzir6irC57rIY65_6q'
    alert = msg
    report = "content="+ alert
    PARAMETERS=report
    from System.Net import WebRequest
    request = WebRequest.Create(URI)
    request.ContentType = "application/x-www-form-urlencoded"
    request.Method = "POST"
    from System.Text import Encoding
    bytes = Encoding.ASCII.GetBytes(PARAMETERS)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()
    response = request.GetResponse()
    from System.IO import StreamReader
    result = StreamReader(response.GetResponseStream()).ReadToEnd().replace('\r', '\n')


def returnweapon():
    if Player.CheckLayer('RightHand'):
        x = Player.GetItemOnLayer('RightHand')
        return x

def weaponselector(killtarget):
    if Player.CheckLayer('LeftHand') == False:
        Player.EquipItem(sheild)
    if killtarget.Body == 0x0065:
        if returnweapon() != feyweapon:
            #Player.UnEquipItemByLayer('LeftHand')
            Player.UnEquipItemByLayer('RightHand')
            Misc.Pause(750)
            Player.EquipItem(feyweapon)
            Misc.Pause(750)
    elif killtarget.Body == 0x0067:
        if returnweapon() != dragonweapon:
            #Player.UnEquipItemByLayer('LeftHand')
            Player.UnEquipItemByLayer('RightHand')
            Misc.Pause(750)
            Player.EquipItem(dragonweapon)
            Misc.Pause(750)
    elif killtarget.Body == 0x003A:
        if returnweapon() != feyweapon:
            #Player.UnEquipItemByLayer('LeftHand')
            Player.UnEquipItemByLayer('RightHand')
            Misc.Pause(750)
            Player.EquipItem(feyweapon)
            Misc.Pause(750)





def CheckEnemy():
    if Items.BackpackCount(0x0E21 ,-1):
        while Player.Visible == True and Player.Hits < Player.HitsMax or Player.Poisoned: 
            Misc.Pause(50)
            
    #enemy = Target.GetTargetFromList( 'enemy' )
    enemy = Target.GetTargetFromList( 'fey' )
    weaponselector(enemy)
    #if enemy != None and enemy.WarMode:
    if enemy != None:
        #Misc.ScriptRun( 'pvm_pvp_attack_list_enemy.py' )
        while enemy != None:
            if Target.HasTarget():
                Target.TargetExecute( enemy )
            else:
                Player.Attack( enemy )      
            Target.SetLast( enemy )
            Misc.Pause( 1000 )
            enemy = Mobiles.FindBySerial( enemy.Serial )
            if enemy:
                if Player.DistanceTo( enemy ) > 1:
                    enemyPosition = enemy.Position
                    enemyCoords = PathFinding.Route()
                    enemyCoords.MaxRetry = 5
                    enemyCoords.StopIfStuck = False
                    enemyCoords.X = enemyPosition.X
                    enemyCoords.Y = enemyPosition.Y - 1
                    PathFinding.Go( enemyCoords )

        corpseFilter = Items.Filter()
        corpseFilter.Movable = False
        corpseFilter.RangeMax = 2
        corpseFilter.Graphics = List[int]( [ 0x2006 ] )
        corpses = Items.ApplyFilter( corpseFilter )
        corpse = None

        Misc.Pause( dragDelay )

        for corpse in corpses:
            if corpse:
                Misc.Pause(750)
                beetledismount()
                Items.UseItem(corpse)
                Misc.Pause(550)

                if Items.FindByID(slayerdaggermodel, -1 , Player.Backpack.Serial):
                    cutter = Items.FindByID(slayerdaggermodel, -1 , Player.Backpack.Serial) #find serial for deed in bank         
                else:
                    cutter = Items.FindByID(daggermodel, -1 , Player.Backpack.Serial)
                Items.UseItem(cutter)
                Target.WaitForTarget(3000, True)
                Target.TargetExecute(corpse)
                Misc.Pause(1000)
            else:
                Misc.SendMessage('No Blades Found')
                
            loot(corpse)
        Misc.Pause(750)   
        beetlemount()
        Misc.Pause(750) 
            
           
def loot(corpse):
    Player.HeadMessage(53, 'foundcorpse')
    Items.UseItem(corpse.Serial)
    Misc.Pause(750)
    for item in corpse.Contains:
        if item.ItemID == goldmodel : #gold
                    Items.Move( item.Serial, beetle, 0 )
                    Misc.Pause( dragDelay )
                    
        elif item.ItemID == arrowmodel: #arrows
                    Items.Move( item.Serial, beetle, 0 )
                    Misc.Pause( dragDelay )       
        elif item.ItemID == scalemodel: #scales
                    Items.Move( item.Serial, beetle, 0 )
                    Misc.Pause( dragDelay ) 
        elif item.ItemID == scalemodel: #scales
                    Items.Move( item.Serial, beetle, 0 )
                    Misc.Pause( dragDelay ) 
        elif item.ItemID == leathermodel: #leather
                    Items.Move( item.Serial, beetle, 0 )
                    Misc.Pause( dragDelay )                     
                    
        Misc.Pause(250)
        
        
def waypoint1():
    global step
    Player.HeadMessage(54,str(Player.Position))
    enemyCoords = PathFinding.Route()
    enemyCoords.MaxRetry = 5
    enemyCoords.StopIfStuck = False
    enemyCoords.X = 436
    enemyCoords.Y = 1572
    PathFinding.Go( enemyCoords )
    Player.HeadMessage(54,'Waypoint1 reached')
    step = 1

def waypoint2():
    global step
    Player.HeadMessage(54,str(Player.Position))
    enemyCoords = PathFinding.Route()
    enemyCoords.MaxRetry = 5
    enemyCoords.StopIfStuck = False
    enemyCoords.X = 488
    enemyCoords.Y = 1570
    PathFinding.Go( enemyCoords )
    Player.HeadMessage(54,'Waypoint2 reached')
    step = 2
    
def gohome(): 
    while Player.Mana < 15:
        Misc.Pause( 50 )
    Items.UseItem(0x42D98AFC)
    Misc.Pause(500)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 32)
    Misc.Pause(1500)
                
def unload():
    global currentxp
    Misc.Pause(1500)
    beetledismount()
    Misc.Pause(750)
    Misc.WaitForContext(0x00046490, 10000)
    Misc.ContextReply(0x00046490, 10)
    Misc.Pause(750)
    beetles = Mobiles.FindBySerial( beetle ) 
    goldcount = Items.ContainerCount(beetles.Backpack.Serial, goldmodel, -1) 
    arrowcount = Items.ContainerCount(beetles.Backpack.Serial, arrowmodel, -1) 
    leathercount = Items.ContainerCount(beetles.Backpack.Serial, leathermodel, -1) 
    
    Items.UseItem(Tallyserial)
    Misc.Pause(600)
    temp = Gumps.LastGumpGetLine(4)
    temp = temp.split("/", 1)[0]
    currentxp2 = int(temp)
    difference = currentxp2 - currentxp
    
    webhook('Gold Farmer deposited: ' + str(goldcount) + ' gold //' + str(arrowcount) + ' arrows //'+ str(leathercount) + ' leather //')
    webhook('Gained ' + str(difference) + 'XP')
    while Items.FindByID(goldmodel,-1, beetles.Backpack.Serial):
        moveitem = Items.FindByID(goldmodel,-1, beetles.Backpack.Serial)
        Items.Move(moveitem, unloadbag, 0)
        Misc.Pause(750)        
    while Items.FindByID(leathermodel,-1, beetles.Backpack.Serial):
        moveitem = Items.FindByID(leathermodel,-1, beetles.Backpack.Serial)
        Items.Move(moveitem, unloadbag, 0)
        Misc.Pause(750)
    while Items.FindByID(arrowmodel,-1, beetles.Backpack.Serial):
        moveitem = Items.FindByID(arrowmodel,-1, beetles.Backpack.Serial)
        Items.Move(moveitem, unloadbag, 0)
        Misc.Pause(750)                
    
def equipweapon():
    Player.UnEquipItemByLayer('RightHand')

def beetlemount():
    if Mobiles.FindBySerial( beetle ):
        Mobiles.UseMobile( beetle )
        Misc.Pause( dragDelay )

def beetledismount():
    if not Mobiles.FindBySerial( beetle ):
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( dragDelay )

        
        
Items.UseItem(Tallyserial)
Misc.Pause(600)
temp = Gumps.LastGumpGetLine(4)
temp = temp.split("/", 1)[0]
currentxp = int(temp)
if Misc.ScriptStatus('DefenceBotManager.py') == False:
    Misc.ScriptRun('DefenceBotManager.py')    
    Misc.Pause(500)
Player.HeadMessage(54, str(currentxp))
for rune in range(0,5): 
    currentlocation = Player.Position
    Misc.Pause(1000)
    #targetrecall = 5+6*rune #casting
    targetrecall = 2+6*rune #scrolls
    while currentlocation == Player.Position:
        Items.UseItem(runebook)
        Misc.Pause(750)
        Gumps.SendAction(1431013363, targetrecall)
        Misc.Pause(1000)
    while Target.GetTargetFromList( 'fey' ):
        CheckEnemy()
        Misc.Pause(1000)    
    


gohome() 
Misc.Pause(1500)     
unload()

    
    