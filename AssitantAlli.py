# by mourn 8182 discord contact
# this is an E razor script for an guild/ alliance assistant. It requires char to have Vet 100+, Animal Lore 100+, 
# Spellweaving 75,Magery 110+, Spirit Speak 100 and Hiding 100.
# Through "Alliance or Guild" chat the Script will come or gate to set locations and rez pets, people, invis you. 
# or self res after killed for justice.
# The Char must be in VVV and have target filter and dress agent set named("dress")
# Uses A single runic atlas in your bag

# REQUIRED Equipment, LRC SUIT, first aid belt full of bandages!

import sys
from System.Collections.Generic import List
from System import Byte

############   set up ######################## 

chatType = "Guild"           #### change to "Alliance" if need
if chatType == "Guild":
    Chat = Player.ChatGuild
else:
    Chat = Player.ChatAlliance
    
recallcommand = "!come" 
gatecommand = "!gate"

home = 1
guild = 2
bucs = 3
dest = 4
fire = 5
khal = 6
delu = 7 

commandList = ["!commands", "!come", "!gate" ,"!loc"]
localCommandList =["!rez", "!justice", "!killblue", "!invis"]
   
locList = ["home","guild","bucs","dest","fire","khal","delu"]    
minmana = 40
currentloc = "not set"
bandBelt = Items.FindByID(0xA1F6,-1,Player.Backpack.Serial)


#####################################################
help = ["say {} to recall or {} to gate to: ".format(recallcommand,gatecommand),
"Valid Locations are home, guild ,bucs , dest , fire , khal , delu",
"for example in {} type: {} home".format(chatType,recallcommand),
"Local Commands are: !rez, !petrez, !invis, !justice, !killblue" ]
def chatCommands():
    if Player.IsGhost:
        Player.Chat("Im Dead at {}".format(currentloc))
        Misc.Pause(60000)
    for loc in locList:
        if Journal.SearchByType("{} {}".format(recallcommand,loc),chatType):
            Chat("Coming to {}".format(loc))             
            if loc == "home":            
                recall(home)               
            elif loc == "guild":
                recall(guild)
            elif loc == "bucs":
                recall(bucs)            
            elif loc == "dest":
                recall(dest)              
            elif loc == "guild":
                recall(guild)              
            elif loc == "fire":
                recall(fire)                
            elif loc == "khal":
                recall(khal)                
            elif loc == "delu":
                recall(delu)              
            elif loc == "guild":
                recall(guild)                
            currentloc = loc    
                
        if Journal.SearchByType("{} {}".format(gatecommand,loc),chatType):
            Chat("Gating to {}".format(loc))
            if loc == "home":
                gate(home)
            elif loc == "guild":
                gate(guild)
            elif loc == "bucs":
                gate(bucs)            
            elif loc == "dest":
                gate(dest)              
            elif loc == "guild":
                gate(guild)              
            elif loc == "fire":
                gate(fire)                
            elif loc == "khal":
                gate(khal)                
            elif loc == "delu":
                gate(delu)              
            elif loc == "guild":
                gate(guild) 
                
    for command in commandList:
        if Journal.SearchByType("{}".format(command),chatType):
            if command == "!commands":
                for h in help:
                    Chat(h)
                    Misc.Pause(3000)
                
def localCommands():
    rezfil = Mobiles.Filter()
    rezfil.Enabled = True
    rezfil.RangeMax = 15
    rezfil.Notorieties = List[Byte](bytes([1,2,3,4,5,6]))   
    if Journal.SearchByType("!rez",'Regular'):
        rezables = Mobiles.ApplyFilter(rezfil)
        if len(rezables) > 0:
            Player.ChatSay(52,"Come Close")
            Misc.Pause(2000)
        else:
            Player.ChatSay(52,"Noone To Rez")
        for r in rezables:
            if "!rez" in Journal.GetTextBySerial(r.Serial):
                if r.IsGhost:
                    if Player.InRangeMobile(r,1): 
                        Spells.CastMagery('Resurrection')
                        Target.WaitForTarget(4000)
                        Target.TargetExecute(r)
                        Misc.Pause(400)
                        Spells.CastMagery('Greater Heal')
                        Target.WaitForTarget(3000)
                        Target.TargetExecute(r)
                        Misc.Pause(400)
                    else:
                        Player.ChatSay(52,"Ghost out of Range")
                else:
                    Player.ChatSay(52,"Youre alive Dummy")
                    
    if Journal.SearchByType("!petrez",'Regular'):
        rezables = Mobiles.ApplyFilter(rezfil)
        if len(rezables) > 0:
            Player.ChatSay(52,"Bring Pet Close")
            Misc.Pause(2000)
        else:
            Player.ChatSay(52,"Noone To Rez")
        for r in rezables:
            if not r.Body in peopleList:
                if r.IsGhost:
                    while r.IsGhost:
                        if Player.InRangeMobile(r,2): 
                            Items.UseItemByID(0x0E21)
                            Target.WaitForTarget(2000)
                            Target.TargetExecute(r)
                            Misc.Pause(7000)
                        else:
                            Player.ChatSay(52,"Pet out of Range")
                        Misc.Pause(1000)
            else:
                Player.ChatSay(52,"Dead Pet Not Found")
                                                    
    if Journal.SearchByType("!invis",'Regular'):
        invisables = Mobiles.ApplyFilter(rezfil)
        if len(invisables) > 0:
            for i in invisables:
                if "!invis" in Journal.GetTextBySerial(i.Serial):       
                    Player.ChatSay(52,"Stand by")          
                    Spells.CastMagery('Invisibility')
                    Target.WaitForTarget(3000)
                    Target.TargetExecute(i)
        else:
            Player.ChatSay(52,"Noone To Invis")    
        Misc.Pause(400)
                                 
    if Journal.SearchByType("!justice",'Regular'):
        if Player.BuffsExist('Criminal'):
            Player.ChatSay(52, "Im crim and can't self rez, wait")
            Misc.Pause(1000)
            Journal.Clear()
            Misc.Pause(400)
            if Player.Mana <= minmana:
                Player.ChatSay(52, "Mana low wait for me to undress")
            while Player.Mana <= minmana:
                Misc.Pause(2000)                                
            Player.ChatSay(52, "Wait for Gift of Life")
            Misc.Pause(1000)
            while not Player.BuffsExist("Gift Of Life"):
                Spells.CastSpellweaving("Gift Of Life")
                Target.WaitForTarget(4000)
                Target.Self()
                Misc.Pause(2000)
                
        Misc.Pause(400)
        Dress.UnDressFStart()
        Player.ChatSay(52, "Kill me now")
        while not Player.IsGhost:
            Misc.Pause(2000)   
        Gumps.WaitForGump(2223, 4000)
        Gumps.SendAction(2223, 2)
        Misc.Pause(2000)
        Dress.ChangeList("dress")       #dress default
        Misc.Pause(400)
        Dress.DressFStart()
        Misc.Pause(2000)
        Spells.CastMagery("Protection")
        Misc.Pause(2000)
        Items.UseItemByID(0xA1F6)     #firstaidbelt MANDANTORY             
        Misc.Pause(400)
                    
    elif Journal.SearchByType("!killblue",'Regular'):
        bluefil = Mobiles.Filter()
        bluefil.Enabled = True
        bluefil.RangeMax = 11
        bluefil.Notorieties = List[Byte](bytes([1]))  
        Player.ChatSay(52, "Get Nekkid and report me!")
        Misc.Pause(400)
        blues = Mobiles.ApplyFilter(bluefil)
        if len(blues) > 0:
            for b in blues:
                if "!blue" in Journal.GetTextBySerial(b.Serial):
                    while b.Hits > 0:
                        Misc.Pause(400)
                        Spells.CastMagery('Mind Blast')
                        Target.WaitForTarget(3000)
                        Target.TargetExecute(b)
                        Misc.Pause(2000)
        else:
            Player.ChatSay(52,"Not in Range or not Blue")
            
def recall(runenumber):
    newrunenumber = 49999 + runenumber   
    Items.UseItemByID(0x9C16)
    Misc.Pause(1000)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, newrunenumber)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, 4000)
    newrunenumber = 0
    Misc.Pause(4000)
    if Journal.Search("fizzles.") == True or Journal.Search("reagents") == True:
        Journal.Clear()
        Misc.Pause(1000)
        recall(runenumber)
        
def gate(runenumber):
    newrunenumber = 49999 + runenumber   
    Items.UseItemByID(0x9C16)
    Misc.Pause(1000)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, newrunenumber)
    Gumps.WaitForGump(498, 3000)
    Gumps.SendAction(498, 2000)
    newrunenumber = 0
    Misc.Pause(4000)
    if Journal.Search("fizzles.") == True or Journal.Search("reagents") == True:
        Journal.Clear()
        Misc.Pause(1000)
        gate(runenumber)
        
def dropRobe():                                       
    for item in Player.Backpack.Contains:
        if item.ItemID == 0x1F03 and item.Hue == 0:
            Items.MoveOnGround(item, 1, Player.Position.X,Player.Position.Y,Player.Position.Z)
            Misc.Pause(1100)
                
def ojCheck():
    OJfil = Mobiles.Filter()
    OJfil.Enabled = True
    OJfil.RangeMax = 15
    OJfil.Notorieties = List[Byte](bytes([5]))
    enemies = Mobiles.ApplyFilter(OJfil)
    if len(enemies) > 0: 
        for e in enemies:
            Misc.SendMessage("Spotted OJ {} at {}".format(e.Name,currentloc))
        if Player.Visible:    
            recall(1)
                                   
def hide():     
    if not Player.Visible:
        Misc.Pause(400)
        if Timer.Check("logintimer") == False:
            Items.UseItem(Player.Backpack)                                               
            Timer.Create("logintimer", 60000)
    else:
        Player.UseSkill("Hiding")

def active():
    if not Timer.Check("active"):
        Items.WaitForContents(bandBelt,2000)
        Timer.Create("active",60000)
           
def Main():
    while True:
        ojCheck()
        chatCommands()
        localCommands()
        hide()
        dropRobe()
        active()
        Journal.Clear()
        Misc.Pause(3000)    
Main()
