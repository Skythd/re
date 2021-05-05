from System.Collections.Generic import List
from System import Byte, Int32

#
# A function I'll need later to check if runbook entry is Empty
#
def RuneBookFirstNameIndex():    
    gumpList = Gumps.LastGumpGetLineList()
    textParts = ["Charges:", "Max Charges:", "Rename book", "Drop rune", 
                 "Set default", "Recall", "Gate Travel", "Sacred Journey" ]
    index = 0
    #Misc.SendMessage("text: {}".format(gumpList[index]), 7)
    while gumpList[index].strip() in textParts:
        #Misc.SendMessage("text: {}".format(gumpList[index]), 7)
        index = index + 1
        # now index should be at the charges numbers so skip 1 more
    index = index + 2
    #Misc.SendMessage("Starts at: {}".format(index))
    return index

def main():
    #
    # First keep track of position in book 
    #
    RuneBooks = [0x40A6DA33]
    RuneBookIndex = 0
    RuneBookIndexName = "BOD RuneBook Order"
    if Misc.CheckSharedValue(RuneBookIndexName):
        RuneBookIndex = Misc.ReadSharedValue(RuneBookIndexName)
    #    
    #
    #
    # Next keep track of position in book. At end of a book we'll set next book 
    #
    RuneOrder = [ 5, 11, 17, 23, 29, 35, 41, ] #  47, 53, 59, 65, 71, 77, 83, 95 ] 
    #
    # First set which rune to use to 0 in case its not stored yet
    # if its stored we'll use the stored value 
    RuneIndex = 0
    RuneIndexName = "BOD Rune Order"
    if Misc.CheckSharedValue(RuneIndexName):
            RuneIndex = Misc.ReadSharedValue(RuneIndexName)       
    #    
    # Now store whatever it is +1 so next time we'll do the next one
    new_rune_index = RuneIndex+1
    # check if the new index is past the end, then start back at 0
    if new_rune_index >= len(RuneOrder):
        new_rune_index = 0
        # and move to the next book
        new_book_index = RuneBookIndex+1
        # check if the new book index is past the end, then start back at 0
        # Maybe want to stop here, because probably chests have not respawned
        if new_book_index >= len(RuneBooks):
            new_book_index = 0
        Misc.SetSharedValue(RuneBookIndexName, new_book_index) 

    # Now store the next rune so that next time we come here we start with the new one
    Misc.SetSharedValue(RuneIndexName, new_rune_index)
    #
    #
    # Now finally everything is set. 
    #
    #
    # RuneBookIndex is set to the current book to use
    # RuneIndex is set to which rune in that book to use
    Gumps.ResetGump()
    Items.UseItem(RuneBooks[RuneBookIndex])
    Gumps.WaitForGump(Gumps.CurrentGump(), 10000)
    bookSlotName = Gumps.LastGumpGetLine(RuneBookFirstNameIndex()+RuneIndex)
    Misc.SendMessage(bookSlotName.strip().lower()) 
    if bookSlotName.strip().lower() != "empty":
        Gumps.SendAction(Gumps.CurrentGump(), RuneOrder[RuneIndex])
        Misc.Pause(2000)
        Misc.Resync()
        Misc.Pause(3000)
        Vendor_ids = [(0x00000E09, 1), 
                      (0x00000E0A, 1),
                      (0x00000E04, 1),
                      (0x00000DFF, 1),
                      (0x00000E06, 1),
                      (0x00004008, 3),
                      #(0x00006830, 1),
                      #(0x00004258, 1),
                      ]
                      #(0x0000410E, 1),
                      #(0x00004FE4, 1),
                      
        if RuneIndex < len(Vendor_ids):              
            vendor = Mobiles.FindBySerial(Vendor_ids[RuneIndex][0])
            if Player.DistanceTo(vendor) > 2:
                Player.PathFindTo(vendor.Position.X, vendor.Position.Y, vendor.Position.Z)
                while Player.DistanceTo(vendor) > 2:
                    Misc.Pause(1000)
            has_more = True
            while has_more:
                Misc.WaitForContext(Vendor_ids[RuneIndex][0], 10000)
                Misc.ContextReply(Vendor_ids[RuneIndex][0], "Bulk Order Info")
                Misc.Pause(2000)
                if Gumps.HasGump():
                    Misc.SendMessage("HAS GUMP", 5)
                    Gumps.WaitForGump(0, 3000)
                    Gumps.SendAction(0, 1)
                else:
                    Misc.SendMessage("NO GUMP", 5)    
                    has_more = False
            return True        
        else:            
            Misc.SendMessage("No Vendor associated with this index {}".format(RuneIndex))
    else:
        Misc.SendMessage("Skipping recall slot {} because it is empty".format(RuneIndex))
    return False

#
bod_request_books = [0x4025EBD6, 0x408B2AA7 ] 
Player.HeadMessage(5, "Requesting BODs Locally")
for bod_book in bod_request_books:
    Journal.Clear()
    while not Journal.Search("offer may be available"):
        Items.UseItem(bod_book)
        Misc.Pause(2000)
# 
more = True 
while more:
    if len(Player.Backpack.Contains) < 120:
        more = main()
#        
Misc.ScriptRun("BOD_store.py")        
        
