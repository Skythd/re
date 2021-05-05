#===================================================================================
scriptName_PathFinderDebugTool      = "PathFinder_Debugtool.py"
sharedValue_PathFinderDebugToolData = "PathFinderDebugToolData"

#===================================================================================
import System, math, time, datetime
import Misc, Player, Statics, Mobiles

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
 
from System import *
from System.Windows.Forms import *
from System.Drawing import *
from System.Drawing.Imaging import *
from System.Drawing.Drawing2D import *

#===================================================================================
def Log(string):
    Misc.SendMessage(">{}".format(string), 201)
 
#===================================================================================
currentTime = 0
def SetUnixTime():
    global currentTime
    currentTime = int(time.time()* 1000)

#===================================================================================
class Pathfinder_Form(Form):
    
    graphicsLayer1 = None
    graphicsLayer2 = None
    isFormRunning = False
    internalCounterPrevious_map = 0
    internalCounterPrevious_path = 0
    
    def __init__(self):
        Form.__init__(self)
        
        self.Text = "Pathfinding Debug Tool"
        self.HelpButton = False
        self.MinimizeBox = True 
        self.MaximizeBox = False
        self.Width = 500
        self.Height = 500
        self.BackColor = Color.Black
        self.FormBorderStyle = FormBorderStyle.FixedSingle
        self.StartPosition = FormStartPosition.CenterScreen
        self.Opacity = 100
        self.SetStyle(ControlStyles.DoubleBuffer, True)
        self.FormClosed += FormClosedEventHandler(self.OnFormClosed)
        self.Show()
        self.Visible = True
        
        self.Main()

    def OnFormClosed(self, e):
        self.Dispose()
        self.isFormRunning = False

    brushBlack = None
    brushGreen = None
    brushRed = None
    brushYellow = None
    brushWhite = None
    def Main(self):
        
        self.isFormRunning = True
        self.graphicsLayer1 = self.CreateGraphics()
        self.graphicsLayer2 = self.CreateGraphics()
        
        self.brushBlack = SolidBrush(Color.Black)
        self.brushGreen = SolidBrush(Color.Green)
        self.brushRed = SolidBrush(Color.Red)
        self.brushYellow = SolidBrush(Color.Yellow)
        self.brushWhite = SolidBrush(Color.White)
        
        while self.isFormRunning == True:
            
            self.DrawGrid()  
                
            Application.DoEvents()
    
    def DrawGrid(self):

        squareSize = 7
        gapSize = 9
        gridSearchSize = 51

        if Misc.CheckSharedValue(sharedValue_PathFinderDebugToolData) == True:
            result = Misc.ReadSharedValue(sharedValue_PathFinderDebugToolData)
            if len(result) == 0:
                return
            
            maze = result[0]
            path = result[1]
            Misc.SetSharedValue(sharedValue_PathFinderDebugToolData, []) 
            
            rowX = 0
            rowZ = 0
            for m in maze:
                for t in m:
                    
                    isTileBlocking = t
                    
                    if isTileBlocking == False:
                        if rowX == int((gridSearchSize - 1) / 2) and rowZ == int((gridSearchSize - 1) / 2):
                            self.graphicsLayer1.FillRectangle(self.brushYellow, (rowX * gapSize)-2, (rowZ * gapSize)-2, squareSize+4, squareSize+4);
                            
                        self.graphicsLayer1.FillRectangle(self.brushGreen, (rowX * gapSize), (rowZ * gapSize), squareSize, squareSize)
                        
                    elif isTileBlocking == None:
                        if rowX == int((gridSearchSize - 1) / 2) and rowZ == int((gridSearchSize - 1) / 2):
                            self.graphicsLayer1.FillRectangle(self.brushYellow, (rowX * gapSize)-2, (rowZ * gapSize)-2, squareSize+4, squareSize+4);
     
                        self.graphicsLayer1.FillRectangle(self.brushRed, (rowX * gapSize), (rowZ * gapSize), squareSize, squareSize)
                    
                    rowX += 1
                
                rowX = 0
                rowZ += 1
            
                
            for p in path:
                rowX = p[0]
                rowZ = p[1]
                self.graphicsLayer2.FillRectangle(self.brushWhite
                                      , ((int((gridSearchSize - 1) / 2)) * gapSize)+  ((rowX - int((gridSearchSize - 1) / 2))) * gapSize
                                      , ((int((gridSearchSize - 1) / 2)) * gapSize)+  ((rowZ - int((gridSearchSize - 1) / 2))) * gapSize
                                      , squareSize
                                      , squareSize)
            
pathfinderForm = Pathfinder_Form()