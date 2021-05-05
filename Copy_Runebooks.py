#Runebook and Runic Atlas Copier by Frank Castle
#
#What you need:
# 1) 100% LRC Suit
# 2) Plenty of mana
# 3) Enough blank runes to copy the entire book
#    DO NOT HAVE ANY RUNES IN YOUR BACKPACK THAT YOU DO NOT WANT MARKED OVER!!!!!!!!!!!!!!
#
# THIS SCRIPT WILL NOT AUTODEFEND.  COPY DANGEROUS RUNES AT YOUR OWN RISK
# THIS SCRIPT WILL STOP AFTER THE LAST RUNE IN THE BOOK IS COPIED.  IF IT IS NOT A SAFE
# RUNE YOU WILL NEED TO WATCH IT 
#
#
# This will copy runebook to runebook or runic atlas to runic atlas so have an empty book
# of the same type 
#
# You will need to set the runeTotal below to the number of runes in the book you are copying


runeTotal = 16 #set to the total number of runes you are copying from the runebook/runic atlas



from System.Collections.Generic import List
global oldBook
global newBook
global oldRune
global bookType
runeCounter = 0

contents =[]
blanks = Items.BackpackCount(0x1F14,-1)
sufficientRunes = True
if blanks < runeTotal:
    Misc.SendMessage('I DO NOT HAVE ENOUGH BLANK RUNES FOR THIS',33)
    Misc.SendMessage('BUY MORE RUNES AND RESTART SCRIPT',58)
    sufficientRunes = False
    
if not Player.BuffsExist('Protection'):
    Spells.CastMagery("Protection")
    Misc.Pause(2000)

def setBagContents():
    for items in Items.FindBySerial(Player.Backpack.Serial).Contains:
        if items.Serial not in contents:
            contents.append(items.Serial)
            
def findRune():
    global oldRune
    for rune in Items.FindBySerial(Player.Backpack.Serial).Contains:
        if rune.Serial not in contents:
            oldRune = Items.FindBySerial(rune.Serial)
            Misc.Pause(500)
            props = Items.GetPropStringList(rune)
            Misc.Pause(500)
            prop = props[2].split(' ')
            name = ''
            n = 3
            for x in prop:
                n = n + 1
                if n == len(prop)-1:
                    break
                name = '{}'.format(name)+ '{}'.format(prop[n] +' ')
            def Recall():
                while Player.Mana < 40:
                    Misc.Pause(2000)
                Journal.Clear()
                Spells.CastMagery("Recall")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(rune)
                Misc.Pause(4000)
            Recall()
            if Journal.Search('Something is blocking'):
                Misc.Pause(30000)
                Recall()
            Items.Move(oldRune,oldBook,0)
            Misc.Pause(1100)
            newRune = Items.FindByID(0x1F14,-1,Player.Backpack.Serial)
            Spells.CastMagery("Mark")
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(newRune)
            Items.UseItem(newRune)
            Misc.Pause(1100)
            Misc.ResponsePrompt('{}'.format(name))
            Misc.Pause(1100)
            Items.Move(newRune,newBook,0)
            Misc.Pause(1100)
            break
        


def ChooseBook():
    global oldBook
    global bookType
    OldBook = Target.PromptTarget('Target your Runebook or Runic Atlas')
    Misc.Pause(1100)
    oldBook = Items.FindBySerial(OldBook)
    if oldBook.ItemID == 0x22C5:
        bookType = 1
        DefineRunebook()
    elif oldBook.ItemID  == 0x9C16:
        bookType = 2
        DefineRunicAtlas()
    else:
        Misc.SendMessage('THAT IS NEITHER A RUNEBOOK NOR A RUNIC ATLAS')
        ChooseBook()
    
def DefineRunebook():
    global newBook
    NewBook = Target.PromptTarget('Target your new Runebook')
    Misc.Pause(1100)
    newBook = Items.FindBySerial(NewBook)
    if newBook.ItemID != 0x22C5 and newBook.ItemID != 0x9C16:
        Misc.SendMessage('THAT IS NEITHER A RUNEBOOK NOR A RUNIC ATLAS')
        DefineRunebook()
        
def DefineRunicAtlas():
    global newBook
    NewBook = Target.PromptTarget('Target your new Runic Atlas')
    Misc.Pause(1100)
    newBook = Items.FindBySerial(NewBook)
    if newBook.ItemID != 0x9C16:
        Misc.SendMessage('THAT IS NOT A RUNIC ATLAS')
        DefineRunicAtlas()

def dropRune():
    global runeCounter
    global bookType
    runeCounter = runeCounter + 1
    setBagContents()
    if bookType == 1:
        Items.UseItem(oldBook)
        Gumps.WaitForGump(89, 10000)
        Gumps.SendAction(89, 200)
    if bookType == 2:
        Items.UseItem(oldBook)
        Gumps.WaitForGump(498, 10000)
        Gumps.SendAction(498, 50000)
        Gumps.WaitForGump(498, 10000)
        Gumps.SendAction(498, 2)
    Misc.Pause(1100)
    findRune()
    
def Main():
    if sufficientRunes == True:
        ChooseBook()
        global runeCounter
        while runeCounter < runeTotal:
            dropRune()
            runeCounter

Main()