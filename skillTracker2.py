URI = 'https://discordapp.com/api/webhooks/REPLACE_THIS_WHOLE_STRING'# your webhook url string 

def DiscordMessage(player, msg):    
    report = "username=" + player.Name + "&content=" + msg
    PARAMETERS=report
    from System.Net import WebRequest
    request = WebRequest.Create(URI)
    request.ContentType = "application/x-www-form-urlencoded"
    request.Method = "POST"
    from System.Text import Encoding
    bytes = Encoding.ASCII.GetBytes(PARAMETERS)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()
    response = request.GetResponse()
    from System.IO import StreamReader
    result = StreamReader(response.GetResponseStream()).ReadToEnd().replace('\r', '\n')

from System.Collections.Generic import List
    
skills = [ "Alchemy", "Anatomy", "Animal Lore", "Item ID", "Arms Lore", "Parry", "Begging", "Blacksmith", "Fletching", "Peacemaking", "Camping", "Carpentry", "Cartography", "Cooking", "Detect Hidden", "Discordance", "EvalInt", "Healing", "Fishing", "Forensics", "Herding", "Hiding", "Provocation", "Inscribe", "Lockpicking", "Magery", "Magic Resist", "Tactics", "Snooping", "Musicianship", "Poisoning", "Archery", "Spirit Speak", "Stealing", "Tailoring", "Animal Taming", "Taste ID", "Tinkering", "Tracking", "Veterinary", "Swords", "Macing", "Fencing", "Wrestling", "Lumberjacking", "Mining", "Meditation", "Stealth", "Remove Trap", "Necromancy", "Focus", "Chivalry", "Bushido", "Ninjitsu", "Spell Weaving", "Imbuing" ]
skill_values = [0] * len(skills) # Initialize skill values to 0

# Initialization
# Iterate through all skills and set values to skill_values list
i = 0
while i < len(skills):
    skill_values[i] = Player.GetSkillValue(skills[i])
    Misc.Pause(100)
    i += 1
 
# Main Loop
# Iterate through all skills and see if a skill raised, then report it
while not Player.IsGhost:
    i = 0
    while i < len(skills):
        # We have gained in skill!
        if Player.GetSkillValue(skills[i]) > skill_values[i]:
            skill_values[i] = Player.GetSkillValue(skills[i])
            alert = skills[i] + ' has increased to ' + str( skill_values[i] )
            DiscordMessage(Player, alert)
            
        #Misc.SendMessage('{}: {}'.format (skills[i], skill_values[i]))
        Misc.Pause(100)
        i += 1
    