MibFileName = 'C:/Program Files (x86)/UOAM/MIBData.map'    
MibContainer = Items.FindBySerial(0x41324CFD)
TargetName = "SOS"
#
LordBritishThrone=[1624, 1323]    
WorldSize = [4096, 5120]
TilesPerDegree= [ WorldSize[0]/360.0, WorldSize[1]/360.0 ] 
#
def splitToPieces(location):
    degree, secTemp= location.split('\xb0')
    seconds, direction = secTemp.split('\x27')
    return int(degree), int(seconds), direction

def convertDegreesToDecimal(degree, seconds, direction):
    result = 0
    if direction.lower() == 'w': 
        result = (LordBritishThrone[1]-(seconds/60.0)* TilesPerDegree[1]-degree*TilesPerDegree[1])%WorldSize[1]
    #    
    if direction.lower() == 'e': 
        result = (LordBritishThrone[1]+(seconds/60.0)* TilesPerDegree[1]+degree*TilesPerDegree[1])%WorldSize[1]
    #    
    if direction.lower() == 'n': 
        result = (LordBritishThrone[0]-(seconds/60.0)* TilesPerDegree[0]-degree*TilesPerDegree[0])%WorldSize[0]
    #    
    if direction.lower() == 's': 
        result = (LordBritishThrone[0]+(seconds/60.0)* TilesPerDegree[0]+degree*TilesPerDegree[0])%WorldSize[0]
    #    
    return int(result)+1

def GetDecimalCoordinates(mib):
    x = -1
    y = -1
    Items.UseItem(mib)
    Gumps.WaitForGump(0, 3000)
    if Gumps.HasGump():
        texts = Gumps.LastGumpGetLineList()
        location = texts[len(texts)-1]
        NSloc, EWloc = location.split(',')
        deg1, sec1, dir1 = splitToPieces(NSloc) 
        deg2, sec2, dir2 = splitToPieces(EWloc)
        Gumps.CloseGump(0)
        #
        Misc.SendMessage("deg: {} sec: {} dir: {}".format(deg1, sec1, dir1))
        Misc.SendMessage("deg: {} sec: {} dir: {}".format(deg2, sec2, dir2))
        x = convertDegreesToDecimal(deg2, sec2, dir2)
        y = convertDegreesToDecimal(deg1, sec1, dir1)
        return x, y
    else:
        Misc.SendMessage("Gump did not Open for mib 0x{:x}".format(mib.Serial))
    return x, y
 

if MibContainer != None:
    for maybeMIB in MibContainer.Contains:
        if maybeMIB.ItemID == 0x099F and maybeMIB.Hue == 0x0:
            mib = maybeMIB
            Items.UseItem(mib.Serial)
            Misc.Pause(1000)
    Items.WaitForContents(MibContainer, 3000)        
    #
    with open(MibFileName, 'w') as file:
        file.write("3\n")
    #        
        for maybeMIB in MibContainer.Contains:
            if maybeMIB.ItemID == 0x14EE and maybeMIB.Hue == 0x0:
                mib = maybeMIB
                x, y = GetDecimalCoordinates(mib)
                Misc.SendMessage("X: {}".format(x))
                Misc.SendMessage("Y: {}".format(y))
                file.write("+treasure: {} {} 0 {}\n".format(x, y, TargetName))
            if maybeMIB.ItemID == 0x14EE and maybeMIB.Hue == 0x0481:
                mib = maybeMIB
                x, y = GetDecimalCoordinates(mib)
                Misc.SendMessage("X: {}".format(x))
                Misc.SendMessage("Y: {}".format(y))
                file.write("+treasure: {} {} 0 {}\n".format(x, y, "Ancient "+TargetName))                

