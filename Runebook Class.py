from System.Collections.Generic import List
myRuneBookSerial = 0x43E4E2F6 #put your rune book serial here

class runeBook():
    bookSerial = 0
    numberMarked = 0
    empties = 0
    delay = {
        'base' : 500,
        'drag' : 600,
        }
    defaultLocList = {
                '1' : 4,
                '2' : 10,
                '3' : 16,
                '4' : 22,
                '5' : 28,
                '6' : 34,
                '7' : 40,
                '8' : 46,
                '9' : 52,
                '10' : 58,
                '11' : 64,
                '12' : 70,
                '13' : 76,
                '14' : 82,
                '15' : 88,
                '16' : 94
                }
                
    runeIndexList = {
                '1' : 5,
                '2' : 11,
                '3' : 17,
                '4' : 23,
                '5' : 29,
                '6' : 35,
                '7' : 41,
                '8' : 47,
                '9' : 53,
                '10' : 59,
                '11' : 65,
                '12' : 71,
                '13' : 77,
                '14' : 83,
                '15' : 89,
                '16' : 95
                }
    
    def __init__(self, serl):
        self.bookSerial = serl

    #--------------------------------------------------------------------
    #member function:   recall
    #author:            Epoch
    #parameters:        a rune index (as a string)
    #returns:           "blocked" = rune is blocked
    #                   "mana" = not enough mana to recall
    #                   "success" = successfully recalled
    #purpose:           recall to a location given an index
    #--------------------------------------------------------------------        
    def recall(self, runeIndex):
        #recall to a rune index
        currentX = Player.Position.X
        currentY = Player.Position.Y
        Items.UseItem(self.bookSerial)
        Gumps.WaitForGump(1431013363, 10000)
        Misc.SendMessage("attempting to recall to rune index: " + str(self.runeIndexList[runeIndex]), 70)
        Gumps.SendAction(1431013363, self.runeIndexList[runeIndex])

        #make sure we have recalled
        recallResult = self.checkPositionChanged(currentX, currentY)
        if recallResult == "blocked":
            #do something that lets us know that this index was blocked
            Misc.SendMessage("Rune Blocked", 100)
            return recallResult
        elif recallResult == "mana":
            #do something that lets us get mana back... probably recall home
            Misc.SendMessage("out of mana", 100)
            return recallResult
        else:
            Misc.SendMessage("success!!!", 70)
            return recallResult
            
    #--------------------------------------------------------------------
    #member function:   setDefault
    #author:            Epoch
    #parameters:        a rune index
    #returns:           Nothing
    #purpose:           set a rune as defualt location given a rune index
    #--------------------------------------------------------------------        
    def setDefault(self, defaultIndex):
        Items.UseItem(self.bookSerial)
        #1431013363 is the runebook gump
        Gumps.WaitForGump(1431013363, 10000)
        Gumps.SendAction(1431013363, self.defaultLocList[defaultIndex])

    #--------------------------------------------------------------------
    #member function:   checkPositionChanged
    #author:            Epoch
    #parameters:        character position X and character position Y
    #returns:           "blocked" = rune is blocked
    #                   "mana" = not enough mana to recall
    #                   "success" = successfully recalled
    #purpose:           waits for character position to change
    #                   or for "blocked" or "mana" to be in journal
    #--------------------------------------------------------------------           
    def checkPositionChanged(self, posX, posY):
        recallStatus = None
        while Player.Position.X == posX and Player.Position.Y == posY:
            if Journal.Search("blocked"):
                Journal.Clear()
                recallStatus = "blocked"
                return recallStatus
            if Journal.Search("mana"):
                Journal.Clear()
                recallStatus = "mana"
                return recallStatus
        recallStatus = "good"
        return recallStatus
        
    #--------------------------------------------------------------------
    #member function:   moveRuneToBook
    #author:            Epoch
    #parameters:        serial for a rune
    #returns:           True or False depending on success
    #purpose:           moves a rune to this book
    #--------------------------------------------------------------------        
    def moveRuneToBook(self, runeSrl):
        if self.getEmpty() != 0:
            #move a rune to the book
            rne = Items.FindBySerial(runeSrl)
            Items.Move(rne, self.bookSerial, 1)
            Misc.Pause(self.delay['drag'])
            return True
        else:
            Misc.SendMessage("runeBook full", 100)
            return False
    
    #--------------------------------------------------------------------
    #member function:   getEmpty
    #author:            Epoch
    #parameters:        none
    #returns:           number of empty rune spots in book
    #purpose:           used to determine if we can fit a new rune in book
    #-------------------------------------------------------------------- 
    def getEmpty(self):
        tempEmpty = 0
        Items.UseItem(self.bookSerial)
        Gumps.WaitForGump(1431013363, 10000)
        Misc.Pause(500)
        totalLines = Gumps.LastGumpGetLineList()
        for line in totalLines:
            if "Empty" in line:
                tempEmpty += 1        
        self.empties = tempEmpty / 2
        #close the book
        Gumps.SendAction(1431013363, 0)
        return self.empties
    

    #--------------------------------------------------------------------
    #member function:   recallFromBook
    #author:            Epoch
    #parameters:        None
    #returns:           "blocked" = rune is blocked
    #                   "mana" = not enough mana to recall
    #                   "success" = successfully recalled
    #purpose:           recall directly off of the book (no rune index)
    #--------------------------------------------------------------------
    def recallFromBook(self):
        Spells.CastMagery("Recall")
        Target.WaitForTarget(15000, True)
        Target.TargetExecute(self.bookSerial)
        currentX = Player.Position.X
        currentY = Player.Position.Y
        recallResult = self.checkPositionChanged(currentX, currentY)
        if recallResult == "blocked":
            #do something that lets us know that this index was blocked
            Misc.SendMessage("Rune Blocked", 100)
            return recallResult
        elif recallResult == "mana":
            #do something that lets us get know we need to get mana back...
            Misc.SendMessage("out of mana", 100)
            return recallResult
        else:
            Misc.SendMessage("success!!!", 70)
            return recallResult

#=======================================================================
#Just some examples of how to use the class:        
Journal.Clear()
#-------------------------create runebook object------------------------
testBook = runeBook(myRuneBookSerial)
#----------------figure out how many times "Empty" occurs---------------
rBookSpace = testBook.getEmpty()
Misc.SendMessage(rBookSpace, 200)
#------------------------Move a rune to this book-----------------------
if not testBook.moveRuneToBook(0x401F7338):
    Misc.SendMessage("couldnt add rune to book", 70)
    #do whatever... the runebook is full
else:
    #do whatever... the rune was placed in the book.
    Misc.SendMessage("success!!!! rune placed in book", 70)
    #might to call populateRunesList to update the runes list
    space = testBook.getEmpty()
    Misc.SendMessage(space, 70)    
#----------------------------recall to places---------------------------
testBook.recall('1')
testBook.recall('2')
testBook.recall('3')
#----------set default location and then recall off of the book---------
testBook.setDefault('9')
testBook.recallFromBook()