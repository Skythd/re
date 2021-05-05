# Start / Stop scripts in game with !scriptname by MatsaMilla
# • scripts must be in script-grid to start/stop
prefix = "^"

def parseJournal (str):
    # Fetch the Journal entries (oldest to newest)
    regularText = Journal.GetTextBySerial(Player.Serial)
    
    # Reverse the Journal entries so that we read from newest to oldest
    regularText.Reverse()

    # Read back until the item ID was started to see if it succeeded
    for line in regularText[ 0 : len( regularText ) ]:
        #if line == str:
        if str in line:
            line = line.split(str, 1)[1]
            Journal.Clear()
            return line
            
def scriptStartOrRestart(scriptName):
    if Misc.ScriptStatus(scriptName):
        Misc.ScriptStop(scriptName)
        Misc.Pause(100)
        Misc.ScriptRun(scriptName)
    else:
        Misc.ScriptRun(scriptName)
    Misc.Pause(100)
    
def toggleScript(scriptName):
    if Misc.ScriptStatus(scriptName):
        Misc.ScriptStop(scriptName)
    else:
        Misc.ScriptRun(scriptName)
    Misc.Pause(100)
            
while True:
    if Journal.SearchByName(prefix, Player.Name):
        scriptName = parseJournal(prefix)
        toggleScript(scriptName + ".py")