#===================================================================================
# Required: Add PathfFinder.py to the script grid 
# Optional: Add PathFinder_Debugtool.py to the script grid 
#===================================================================================
import PathFinder

#===================================================================================
def MainLoop():
    
    #gridSearchSize is the map size fed to astar
    #value used for testing is 51
    #value must be uneven!
    gridSearchSize = 51

    # PathFinder is relying on certain fixed terrain rules. 
    # Anomalous tiles can be overriden in the array below
    # ignoreTilePositionArray turns a blocking tile into a walkable tile
    ignoreTilePositionArray =   [
                                    [1420, 1633],   #Britain NorthWest Wall Overhead 
                                    [1420, 1637],   #Britain NorthWest Wall Overhead 
                                    [1464, 1639],   #Britain NorthWest Wall Overhead 
                                    [1464, 1643],   #Britain NorthWest Wall Overhead 
                                    [1513, 1635],   #Britain Sewer Entrance North
                                    [1513, 1647]    #Britain Sewer Entrance South
                                ]
                          
    # PathFinder is relying on certain fixed terrain rules. 
    # Anomalous tiles can be overriden in the array below
    # blockTilePositionArray turn a walkable tile into a blocking tile
    blockTilePositionArray =    [
                              
                                ] 
                    
    #1 time Initialize required to set up PathFinder
    #value used for testing is 51
    PathFinder.Initialize(gridSearchSize, ignoreTilePositionArray, blockTilePositionArray)

    while True:
        # PathFinder is a threaded and thus nonblocking script command
        destination = [1643, 1718]
        PathFinder.MoveToDestination(destination)
    
MainLoop()
