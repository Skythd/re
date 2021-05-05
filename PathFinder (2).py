#===================================================================================
scriptName_PathFinder               = "PathFinder.py"
sharedValue_PathFinderInitialize    = "PathFinderInitialize"
sharedValue_PathFinderDataInput     = "PathFinderDataInput"
sharedValue_PathFinderDataOutput    = "PathFinderDataOutput"

scriptName_PathFinderDebugTool      = "PathFinder_DebugTool.py"
sharedValue_PathFinderDebugToolData = "PathFinderDebugToolData"

#===================================================================================
import System, math, time, datetime
import Misc, Player, Statics, Mobiles

#===================================================================================
def Log(string):
    Misc.SendMessage(">{}".format(string), 201)
 
#===================================================================================
currentTime = 0
def SetUnixTime():
    global currentTime
    currentTime = int(time.time()* 1000)

#===================================================================================
class Astar:
    def __init__(self, matrix):
        self.mat = self.prepare_matrix(matrix)

    class Node:
        def __init__(self, x, y, weight=0):
            self.x = x
            self.y = y
            self.weight = weight
            self.heuristic = 0
            self.parent = None

        def __repr__(self):
            return str(self.weight)

    def prepare_matrix(self, mat):
        matrix_for_astar = []
        for y, line in enumerate(mat):
            tmp_line = []
            for x, weight in enumerate(line):
                tmp_line.append(self.Node(x, y, weight=weight))
            matrix_for_astar.append(tmp_line)
        return matrix_for_astar

    def equal(self, current, end):
        return current.x == end.x and current.y == end.y

    def heuristic(self, current, other):
        return abs(current.x - other.x) + abs(current.y - other.y)

    def neighbours(self, matrix, current):
        neighbours_list = []
        if current.x - 1 >= 0 and current.y - 1 >= 0 and matrix[current.y - 1][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x - 1])
        if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x - 1])
        if current.x - 1 >= 0 and current.y + 1 < len(matrix) and matrix[current.y + 1][
            current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x - 1])
        if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x])
        if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x])
        if current.x + 1 < len(matrix[0]) and current.y - 1 >= 0 and matrix[current.y - 1][
            current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x + 1])
        if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x + 1])
        if current.x + 1 < len(matrix[0]) and current.y + 1 < len(matrix) and matrix[current.y + 1][
            current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x + 1])
        return neighbours_list

    def build(self, end):
        node_tmp = end
        path = []
        while (node_tmp):
            path.append([node_tmp.x, node_tmp.y])
            node_tmp = node_tmp.parent
        return list(reversed(path))

    def run(self, point_start, point_end):
        matrix = self.mat
        start = self.Node(point_start[0], point_start[1])
        end = self.Node(point_end[0], point_end[1])
        closed_list = []
        open_list = [start]

        while open_list:
            current_node = open_list.pop()

            for node in open_list:
                if node.heuristic < current_node.heuristic:
                    current_node = node

            if self.equal(current_node, end):
                return self.build(current_node)

            for node in open_list:
                if self.equal(current_node, node):
                    open_list.remove(node)
                    break

            closed_list.append(current_node)

            for neighbour in self.neighbours(matrix, current_node):
                if neighbour in closed_list:
                    continue
                if neighbour.heuristic < current_node.heuristic or neighbour not in open_list:
                    neighbour.heuristic = neighbour.weight + self.heuristic(neighbour, end)
                    neighbour.parent = current_node
                if neighbour not in open_list:
                    open_list.append(neighbour)

        return None
        
#===================================================================================
def GetTileBlockingStatus(gridSearchSize, tilePositionX, tilePositionZ, mobilesList, ignoreTilePositionArray, blockTilePositionArray):
                
    isTileBlocking = False
    
    tileId = Statics.GetLandID(tilePositionX, tilePositionZ , 0)                        
 
    landFlag_None = Statics.GetLandFlag(tileId, "None")
 
    landFlag_Impassable = False
    landFlag_Impassable = Statics.GetLandFlag(tileId, "Impassable")
    if landFlag_Impassable == True:
        isTileBlocking = True                    
 
    tileFlag_Impassable     = False
    tileFlag_Wall           = False
    tileFlag_Bridge         = False
    tileFlag_Surface        = False
    tileFlag_Wet            = False
    tileFlag_Foliage        = False
    tileFlag_Translucent    = False
    tileFlag_NoShoot        = False
    tileFlag_Roof           = False
    staticsTileInfoList = Statics.GetStaticsTileInfo(tilePositionX, tilePositionZ, 0)
    for staticsTile in staticsTileInfoList:
        if Statics.GetTileFlag(staticsTile.StaticID, "Impassable") == True:
            tileFlag_Impassable = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Wall") == True:
            tileFlag_Wall = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Bridge") == True:
            tileFlag_Bridge = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Surface")   == True:
            tileFlag_Surface = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Wet") == True:
            tileFlag_Wet = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Foliage") == True:
            tileFlag_Foliage = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Translucent") == True:
            tileFlag_Translucent = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "NoShoot") == True:
            tileFlag_NoShoot = True;
        if Statics.GetTileFlag(staticsTile.StaticID, "Roof") == True:
            tileFlag_Roof = True;
 
    if tileFlag_Impassable == True and tileFlag_Foliage == True:
        isTileBlocking = True
 
    if tileFlag_Impassable == True and tileFlag_Wall == True:
        isTileBlocking = True
 
    if tileFlag_Impassable == True and tileFlag_Wet == True:
        isTileBlocking = True
 
    if landFlag_None == True and tileFlag_Impassable == True:
        isTileBlocking = True
        
    if tileFlag_Bridge == True and tileFlag_Wall == False:
        isTileBlocking = False
        
    if tileFlag_Impassable == False and tileFlag_Surface == True:
        isTileBlocking = False
        
    if (landFlag_None == False or landFlag_Impassable == False) and tileFlag_Surface == True and tileFlag_Translucent == True and tileFlag_Wet == True and tileFlag_Wall == False:
        isTileBlocking = False
 
    if tileFlag_Roof == True:    
        isTileBlocking = True
        
    for tilePosition in ignoreTilePositionArray:
        if tilePositionX == tilePosition[0] and tilePositionZ == tilePosition[1]:
            isTileBlocking = False
            
    for tilePosition in blockTilePositionArray:
        if tilePositionX == tilePosition[0] and tilePositionZ == tilePosition[1]:
            isTileBlocking = True
    
    if mobilesList is not None:
        for mobile in mobilesList:
            if tilePositionX == mobile.Position.X and tilePositionZ == mobile.Position.Y:
                isTileBlocking = True
                if mobile.Serial == Player.Serial:
                    isTileBlocking = False
                break
 
    if tilePositionX == (int((gridSearchSize - 1) / 2) + 1) and tilePositionZ == (int((gridSearchSize - 1) / 2) + 1):
        isTileBlocking = False
            
    if Statics.CheckDeedHouse(tilePositionX, tilePositionZ) == True:            
        isTileBlocking = True
 
    return isTileBlocking
    
#==========================================================================================================            
def CreateMap(gridSearchSize, mobilesList, ignoreTilePositionArray, blockTilePositionArray):
    map = []
    
    pPosX = Player.Position.X
    pPosZ = Player.Position.Y
 
    mapRow = []
    rowX = 0
    rowZ = 0
 
    while rowZ < gridSearchSize:
        while rowX < gridSearchSize:
            tilePosX = ( pPosX - int((gridSearchSize - 1) / 2) ) + rowX
            tilePosZ = ( pPosZ - int((gridSearchSize - 1) / 2) ) + rowZ
            
            isTileBlocking = GetTileBlockingStatus(gridSearchSize, tilePosX, tilePosZ, mobilesList, ignoreTilePositionArray, blockTilePositionArray)
 
            if isTileBlocking == False:
                mapRow.append(0)
            else:
                mapRow.append(None)
 
            rowX += 1
            
        map.append(mapRow)
        mapRow = []
 
        rowX = 0
        rowZ += 1
 
    return map

#===================================================================================
def GetStringDirection(nextTileX, nextTileZ):
    if abs(nextTileX) > 1:
        #Log("GetStringDirection: Input To Big >> "+str(nextTileX))
        return
 
    if abs(nextTileZ) > 1:
        #Log("GetStringDirection: Input To Big >> "+str(nextTileX))
        return
        
    direction = ""
    if nextTileX == 0 and nextTileZ == -1:
        direction = "North"
    elif nextTileX == 1 and nextTileZ == -1:
        direction = "Right"
    elif nextTileX == 1 and nextTileZ == 0:
        direction = "East"
    elif nextTileX == 1 and nextTileZ == 1:
        direction = "Down"
    elif nextTileX == 0 and nextTileZ == 1:
        direction = "South"
    elif nextTileX == -1 and nextTileZ == 1:
        direction = "Left"
    elif nextTileX == -1 and nextTileZ == 0:
        direction = "West"
    elif nextTileX == -1 and nextTileZ == -1:
        direction = "Up"
        
    #Log(str(nextTileX)+" <>"+str(nextTileZ)+" <> "+str(direction))
        
    return direction

#==========================================================================================================            
Misc.SetSharedValue(sharedValue_PathFinderDebugToolData, []) 
def SetMapForm(map, path):
    global _mapFormInternalCounter
    
    input = [map, path]
    Misc.SetSharedValue(sharedValue_PathFinderDebugToolData, input) 
    
#==========================================================================================================            
def Initialize(gridSearchSize, ignoreTilePositionArray, blockTilePositionArray):
    global _isPathFinderCalcRunning
    
    input = [gridSearchSize, ignoreTilePositionArray, blockTilePositionArray]
    Misc.SetSharedValue(sharedValue_PathFinderInitialize, input)
    
    Misc.ScriptRun(scriptName_PathFinder)
    
    #if Misc.ScriptStatus(scriptName_PathFinderDebugTool) == True:
    Misc.ScriptRun(scriptName_PathFinderDebugTool)

    _isPathFinderCalcRunning = False
    Misc.SetSharedValue(sharedValue_PathFinderDataInput, [])
    Misc.SetSharedValue(sharedValue_PathFinderDataOutput, [])
    
    Log("PathFinder Initialized...")

#==========================================================================================================            
_isPathFinderCalcRunning = False
def MoveToDestination(positionEnd):
    global _isPathFinderCalcRunning

    output = []

    positionStart = [Player.Position.X, Player.Position.Y]

    if positionStart == positionEnd:
        return output
    
    if _isPathFinderCalcRunning == False:
        _isPathFinderCalcRunning = True
        
        input = [positionStart, positionEnd]
        Misc.SetSharedValue(sharedValue_PathFinderDataInput, input) 
    else:
        output = Misc.ReadSharedValue(sharedValue_PathFinderDataOutput)
    
        if len(output) > 0:
            _isPathFinderCalcRunning = False 
            Misc.SetSharedValue(sharedValue_PathFinderDataOutput, [])
    
    return output
    
#==========================================================================================================            
def MainLoop():
    
    input = Misc.ReadSharedValue(sharedValue_PathFinderInitialize)
    
    if type(input) == int or type(input) == None:
        return
    
    if len(input) == 0:
        return

    gridSearchSize          = input[0]
    ignoreTilePositionArray = input[1]
    blockTilePositionArray  = input[2]
    
    isMainRunning = True
    while isMainRunning:
        
        input = Misc.ReadSharedValue(sharedValue_PathFinderDataInput)
        if len(input) > 0:
            positionStart           = input[0]
            positionEnd             = input[1]
            Misc.SetSharedValue(sharedValue_PathFinderDataInput, [])

            filter = Mobiles.Filter()
            filter.Enabled = False
            mobilesList = Mobiles.ApplyFilter(filter)
            
            map = CreateMap(gridSearchSize, mobilesList, ignoreTilePositionArray, blockTilePositionArray)

            centerTile = int((len(map) - 1) / 2)

            path = []
            if abs(positionEnd[0] - positionStart[0]) <= centerTile and abs(positionEnd[1] - positionStart[1]) <= centerTile: 
                destinationX = centerTile + (positionEnd[0] - positionStart[0])
                destinationZ = centerTile + (positionEnd[1] - positionStart[1])

                astar = Astar(map)
                path = astar.run((centerTile, centerTile), (destinationX, destinationZ))            
                if path == None:
                    path = []

            if len(path) > 1:
                hasPlayerMoved = False
                
                nextTileX = path[1][0] - path[0][0]
                nextTileZ = path[1][1] - path[0][1]
                
                direction = GetStringDirection(nextTileX, nextTileZ)

                while hasPlayerMoved == False:

                    if direction != Player.Direction:
                        #Log("Facing: "+str(Player.Direction) +" MoveTowards: "+str(direction)  )
                        Player.Run(direction, False)
                        Misc.Pause(10)
                    else:
                        #Log("WALK " + str(direction))
                        Player.Run(direction, False)
                        Misc.Pause(40)
                        hasPlayerMoved = True
                        break

            SetMapForm(map, path)
            output = [map, path]
            Misc.SetSharedValue(sharedValue_PathFinderDataOutput, output)

        
        
                


if __name__ == '__main__':
    # executed only in the main script
    Log("MainLoop()")
    MainLoop()
else:
    # excecuted only in submodules
    Misc.SetSharedValue(sharedValue_PathFinderInitialize, [])