import re 
#
MapFileName = 'C:/Program Files (x86)/UOAM/MAPData.map'    
MapContainer = Items.FindBySerial(0x40831496)
TargetName = "MAP"
#  
def OpenMap(map):
    Journal.Clear()
    drunken = Items.ContextExist(map, "Go To Wiki")
    if True: #drunken == 0:
        got_cords = False
        while not got_cords:
            Misc.SendMessage("Openning Map: 0x{:x}".format(map.Serial))
            Items.UseItem(map)
            Misc.Pause(1000)
            Items.WaitForProps(map, 3000)
            mapInfo = Misc.GetMapInfo(map.Serial)
            if mapInfo.MapOrigin.X != 0:
                return True  
            Stop() 
            #if Journal.Search("map is too difficult"):
            #    return False
        
    else:    
        answer = Items.ContextExist(map, "Open Map")    
        while answer == -1:
            Items.UseItem(map)
            Misc.Pause(1000)
            answer = Items.ContextExist(map, "Open Map")
            if Journal.Search("map is too difficult"):
                return False
    #    
    return True 
    
def GetDecimalCoordinates(map):
    if OpenMap(map):
        mapInfo = Misc.GetMapInfo(map.Serial)
        if mapInfo.MapOrigin.X+mapInfo.PinPosition.X+mapInfo.MapOrigin.Y+mapInfo.PinPosition.Y == 0:
            Misc.Pause(1000)
            mapInfo = Misc.GetMapInfo(map.Serial)
        #    
        return mapInfo.MapOrigin.X+mapInfo.PinPosition.X, mapInfo.MapOrigin.Y+mapInfo.PinPosition.Y
    return 0,0    

    
AreaIndex = {"felucca" : 1, "trammel" : 2, "ilshenar" : 3, "malas" : 4, "tokuno" : 5, "faraan" : 0  }    
if MapContainer != None:
    Items.UseItem(MapContainer)
    Items.WaitForContents(MapContainer, 3000)        
    #
    with open(MapFileName, 'w') as file:
        file.write("3\n")
    #        
        for maybeMAP in MapContainer.Contains:
            if maybeMAP.ItemID == 0x14EC and maybeMAP.Hue == 0x0:
                map = maybeMAP
                Items.WaitForProps(map, 3000)
                props = Items.GetPropStringList(map)
                completed = False
                for p in props:
                    if "completed" in p.lower():
                        completed = True
                if completed:
                    Misc.SendMessage("COMPLETED")
                    continue 
                Misc.SendMessage("Checking Map: 0x{:x}".format(map.Serial))                   
                x, y = GetDecimalCoordinates(map)
                if x+y != 0:
                    prop = Items.GetPropStringByIndex(map, 2)
                    areaName = "none"
                    match = re.search(r"For Somewhere In\s+(\S+)\s?", prop, re.IGNORECASE)
                    if match: 
                        areaName = match.group(1).lower()
                        if areaName in AreaIndex:
                            area = AreaIndex[areaName]
                        else:
                            continue    
                    else:
                        area = 0
                    Misc.SendMessage("X: {}".format(x))
                    Misc.SendMessage("Y: {}".format(y))
                    tempTargetName = TargetName
                    if areaName == "faraan":
                        tempTargetName = "F-"+TargetName
                    file.write("+treasure: {} {} {} {}-0X{:x}\n".format(x, y, area, tempTargetName, map.Serial))
            else:
                Misc.SendMessage("itemid : 0x{:x} hue: 0x{:x}".format(maybeMAP.ItemID, maybeMAP.Hue))
                

