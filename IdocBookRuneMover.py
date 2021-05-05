#===========================================#
#              Abigor IDOC Book             #
#           Auto-Filler for Guildhosue      #
#===========================================#
#                                           #
#   Author: Abigor                          #
#   Discord: Abigor#2005                    #
#   Release Date: 2/1/2021                  #
#   Run on Loop                             #
#                                           #
#   Have a chest for Guildmates to drop     #
#   runes in beside an Atlas or Runebook    #
#   Guildies drop a rune in the chest       #
#   and it gets added to the book and       #
#   Security is set to Anyone               #
#                                           #
#===========================================#
def pause(time):
    Misc.Pause(time)

#runeChest = Target.PromptTarget("Select IDOC Rune Chest")   #unhash these two if you want to manually select
#book = Target.PromptTarget("Select the IDOC Atlas")         #the crate and book
runeChest = 0x46BB6722
book = 0x46BB7662
chestPause = 60000                                            #time between checking the crate for new runes
bookX = Items.FindBySerial(book).Position.X
bookY = Items.FindBySerial(book).Position.Y
bookZ = Items.FindBySerial(book).Position.Z
chestTimer = 0
runeID = 0x1F14
pause(1500)

def LoadBook():
    Items.UseItem(runeChest)
    pause(1150)
    for runes in Items.FindBySerial(runeChest).Contains:
        if runes.ItemID == runeID:
            Items.Move(runes, Player.Backpack, 0, runes.Position.X, runes.Position.Y)
            pause(1500)
    

    Misc.SendMessage("Done Moving", 95)
    pause(800)
    Target.TargetExecuteRelative(book,1)
    pause(800)
    Misc.WaitForContext(book, 10000)
    Misc.ContextReply(book, 1012)  #retrieve book
    pause(1300)
    for runes in Player.Backpack.Contains:
        if runes.ItemID == runeID:
            Items.Move(runes, book, 0, runes.Position.X, runes.Position.Y)   # Put Runes in the book
            pause(1500)

    pause(2000)        
    Misc.SendMessage("Done Filling Book", 95)
    pause(500)

    Items.MoveOnGround(book, 0, bookX, bookY, bookZ)
    pause(500)
    Player.ChatSay(60, "I wish to secure this")
    Target.WaitForTarget(book,10000)
    Target.TargetExecute(book)
    pause(800)
    Misc.WaitForContext(book, 10000)
    Misc.ContextReply(book, 600)  #Set Security
    pause(1500)
    Gumps.WaitForGump(661, 10000)
    Gumps.SendAction(661, 4)  #anyone

def checkChest():
    Items.UseItem(runeChest)
    Items.WaitForContents(runeChest, 5000)
    numRunes = Items.ContainerCount(runeChest, runeID, -1)
    if numRunes >= 1:
        LoadBook()
        pause(2000)
        Timer.Create("chestTimer", chestPause)
        
if Timer.Check("chestTimer") == False:
    checkChest()



pause(4000)
