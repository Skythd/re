
def isVisible(mobser,range):
    Misc.Resync() ##############################?!??!?!?
    mobile = Mobiles.FindBySerial(mobser)
    global mobile
    if not mobile:
        return False
    if not Player.InRangeMobile(mobile, range):
        return False
    if Player.Position.X == mobile.Position.X and Player.Position.Y == mobile.Position.Y and Player.Position.Z == mobile.Position.Z:
        return True
    
    def coordsToMobile(mobile):   # makes list of xyz coords from mobile back to player
        mobX = mobile.Position.X
        mobY = mobile.Position.Y
        x = Player.Position.X
        y = Player.Position.Y
        
        if mobX >= x:
            Xdist = mobX - x
        else:
            Xdist = x - mobX
        if mobY >= y:
            Ydist = mobY - y
        else:
            Ydist = y - mobY
            
        if mobY < y and mobX == x:
            dir = 'North'
        elif mobY > y and mobX == x:    
            dir = 'South'
        elif mobY == y and mobX > x:    
            dir = 'East'
        elif mobY == y and mobX < x:
            dir = 'West'                
        elif mobY >= y and mobX >= x:
            dir = 'Down'
        elif mobY > y and mobX < x:    
            dir = 'Left'
        elif mobY < y and mobX < x:    
            dir = 'Up'
        elif mobY < y and mobX > x:
            dir = 'Right'
        #Misc.SendMessage("{},{},{}".format(dir,Xdist,Ydist),80)
                
        coords = []        
        if dir =='North':
            while mobY != y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobY +=1                
        elif dir =='South':
            while mobY != y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobY -= 1               
        elif dir == 'East':            
            while mobX != x:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX -=1
        elif dir == 'West':            
            while mobX != x:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX +=1  
        elif dir == 'Up':
            if Xdist > Ydist:
                off = Xdist - Ydist               
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobX -=1
            elif Ydist > Xdist:
                off = Ydist - Xdist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobY -=1       
            while mobX != x and mobY !=y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX += 1
                mobY += 1                    
        elif dir == 'Down':
            if Xdist > Ydist:
                off = Xdist - Ydist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobX -=1
            elif Ydist > Xdist:
                off = Ydist - Xdist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobY -=1        
            while mobX != x and mobY !=y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX -= 1
                mobY -= 1                                    
        elif dir == 'Left':
            if Xdist > Ydist:
                off = Xdist - Ydist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobX -=1
            elif Ydist > Xdist:
                off = Ydist - Xdist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobY -=1       
            while mobX != x and mobY !=y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX += 1
                mobY -= 1                                    
        elif dir == 'Right':
            if Xdist > Ydist:
                off = Xdist - Ydist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobX -=1
            elif Ydist > Xdist:
                off = Ydist - Xdist
                while off != 0:
                    coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                    off -=1
                    mobY -=1                           
            while mobX != x and mobY !=y:
                coords.append([mobX,mobY,Statics.GetLandZ(mobX,mobY,Player.Map)])
                mobX -= 1
                mobY += 1
                
        coords.append([x,y,Statics.GetLandZ(x,y,Player.Map)])        
        if not len(coords):            
            Misc.SendMessage('{} is broken'.format(dir)) # direction to mobile debug msg       
        else:            
            Misc.NoOperation() #SendMessage('{} tiles to check'.format(len(coords)),30) #length of coords to check 
        return coords
                
    def checkCoords(list):
        
        badLand = []##### MAKE LIST OF BLOCKING LAND ART?
        zlist = []
        
        def terrain(zlist):
            pz = Player.Position.Z
            mz = mobile.Position.Z
         
            
            if pz > mz:
                angle = 'Down'
            elif mz > pz:
                angle = 'Up'
            else:
                angle = None
                
            if angle == None:
                if zlist.count(zlist[0]) == len(zlist):  ## flat ground
                    #Misc.SendMessage('Flat Ground',88)
                    return True                    
                for z in zlist:
                    if z > pz + 8:
                        #Misc.SendMessage('Tall Hill',48) 
                        return False
                        
            if angle == 'Up':
                #Misc.SendMessage('Up Hill')
                altitude = mz - pz
                steps = altitude/len(zlist)
                count = 0
                while count < (len(zlist)):                                        
                    acceptable = mz - (steps * count)
                    #Misc.SendMessage('{} / {}'.format(zlist[count],acceptable),48)
                    if zlist[count] > acceptable + 10:
                        #Misc.SendMessage('Steep Hill')
                        return False
                    count += 1    
                
            if angle == 'Down':
                #Misc.SendMessage('Down Hill')
                altitude = pz - mz
                steps = altitude/len(zlist)
                count = 0
                while count < (len(zlist)):                                        
                    acceptable = mz + (steps * count)
                    #Misc.SendMessage('{} / {}'.format(zlist[count],acceptable),48)
                    if zlist[count] > acceptable + 14:
                        #Misc.SendMessage('Steep Drop')
                        return False
                    count += 1    
                                        
            return True
                       
        def checkTile(x,y,z): 
            tile = Statics.GetLandID(x,y,Player.Map)
            statics = Statics.GetStaticsTileInfo(x,y,Player.Map)
            
            def isStaticWall(static):###  static walls 
                staticName = Statics.GetTileName(static.StaticID)
                if 'wall' in staticName and not 'torch' in staticName:
                    if Player.Position.Z >= static.StaticZ + 20 or mobile.Position.Z >= static.StaticZ + 20:
                        #Misc.SendMessage('Above Wall',80)
                        Misc.NoOperation()
                    else:
                        #Misc.SendMessage('{} Found'.format(staticName),145)
                        return True
                    
            def isFloorBlocking(static,mobile):### Checks for floors between z
                staticName = Statics.GetTileName(static.StaticID)
                badFloor = ['roof','planks','pavers']
                for bfloor in badFloor:
                    if bfloor in staticName:
                        #Misc.SendMessage('{} Found'.format(staticName),145)
                        if static.StaticZ > Player.Position.Z and static.StaticZ <= mobile.Position.Z:
                            #Misc.SendMessage('Floor Above Blocking',48)
                            return True
                        if static.StaticZ <= Player.Position.Z and static.StaticZ > mobile.Position.Z:    
                            #Misc.SendMessage('Floor Below Blocking',48)
                            return True 
                                        
            if statics:                
                for static in statics:
                    if isStaticWall(static) == True:### works for static walls
                        return False
                    elif isFloorBlocking(static,mobile):
                        return False
                    else:
                        return True
                                                
            elif tile in badLand:### list of land tiles u cant see thru, currently empty
                return False
            else:
                return True 
                
        for coord in list:
            zlist.append(coord[2])
            #Misc.SendMessage('{} {} {}'.format(coord[0],coord[1],coord[2]),10)
            if checkTile(coord[0],coord[1],coord[2]) == False:
                return False
        if terrain(zlist) == False:
            return False
        return True
                            
    if checkCoords(coordsToMobile(mobile))== False:
        Misc.SendMessage("{} cannot be seen ".format(mobile.Name),48)
        return False
    else:
        Misc.SendMessage("{} is visible".format(mobile.Name),89)
        return True
             
isVisible(0x02701628,10)   #### mobile serial , range
   