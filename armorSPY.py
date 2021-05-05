#
# Script to Generate JSON data for "Knucklehead's Desktop Suit Calculator"
# (C) 2020 Kaj Kajsen.
#  FreeWare

props = ["Physical Resist",
         "Fire Resist",
         "Cold Resist",
         "Poison Resist",
         "Energy Resist",
         "Lower Mana Cost",
         "Lower Reagent Cost",
         "Mana Regeneration",
         "Hit Point Regeneration",
         "Strength Bonus",
         "Dexterity Bonus",
         "Intelligence Bonus",
         "Hit Point Increase",
         "Mana Increase",
         "Stamina Increase",
         "Hit Chance Increase",
         "Defense Chance Increase",
         "Damage Increase",
         "Spell Damage Increase",
         "Casting Focus",
         "Enhanced Potion",
         "Luck",
         "Faster Casting",
         "Faster Cast Recovery",
         "Hit Lower Defense",
         "Reflect Physical Damage",
         "Swing Speed Increase"]

convert=["Phy",
         "Fire",
         "Cold",
         "Poison",
         "Energy",
         "LMC",
         "LRC",
         "MR",
         "HPR",
         "Str",
         "Dex",
         "Int",
         "HPI",
         "MI",
         "SI",
         "HCI",
         "DCI",
         "DI",
         "SDI",
         "CF",
         "EP",
         "Luck",
         "FC",
         "FCR",
         "HLD",
         "RPD",
         "SSI"]

itam = Target.PromptTarget('Target Item')
with open ('armor.json','a') as f:
    
    f.write ("\t{\n")
    f.write ("\t\t\"Name\": \"Insert name here\",\n")
    f.write ("\t\t\"Type\": \"Insert Type here\",\n")
    for i in range (len(props)) :
        Items.WaitForProps(itam,3000)
        hej = Items.GetPropValue(itam,props[i])
        f.write ("\t\t")
        f.write ("\"" +convert[i]+ "\": ")
        ud = int (hej)
        f.write (str(ud)+",\n")
    f.write ("\t},\n")
f.close ()

