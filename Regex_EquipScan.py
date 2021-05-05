#==============================================#
#               Regex Equip Scan               #
#==============================================#
#                                              #
#   Author: CookieLover                        #
#   Release Date: 12/21/2017                   #
#   Updated: 12/22/2017                        #
#                                              #
#==============================================#
#                                              #
#   Info:                                      #
#   - target a player to scan his equip        #
#     properties. The list will be saved in    #
#     Razor Enhanced main folder.              #
#                                              #
#==============================================#

import re

class Props(object):
    NoProp = [
        'durability', 'weight', 'lower ammo cost',
        'strength requirement', 'lower requirements',
        'artifact rarity'
        ]

    @staticmethod
    def GetProp(txt):
        k = re.findall(r'^[a-zA-Z- ]*(?=[ ])', txt)
        if '%' in txt:            
            v = re.findall(r'\d+(?=[%])', txt)
        else:
            v = re.findall(r'\d+$', txt)
            
        if k == [] or v == [] or k[0] == '' or v[0] == '':
            return None, None
        return k[0], v[0]

    @staticmethod
    def Dict(plist):
        tmp = {}
        for p in plist:
            if any(n for n in Props.NoProp if n in p.lower()):
                continue
            k,v = Props.GetProp(p)
            if k is None or v is None:
                continue
            try:
                v = int(v)
            except:
                continue
            tmp[k] = v

        return tmp

class ScanEquip(object):
    pResult = {}
    Targ = None

    def __init__(self, targ):
        self.Targ = Mobiles.FindBySerial(targ)
        Mobiles.Message(self.Targ, 82, 'Scanning properties...')
        Misc.WaitForContext(targ, 5000)
        Misc.ContextReply(targ, 0)
        Misc.Pause(500)
        

    def Scan(self):
        for itm in self.Targ.Contains:
            Items.WaitForProps(itm, 5000)
            plist = [p for p in Items.GetPropStringList(itm)]
            pdict = Props.Dict(plist)
            for k,v in pdict.iteritems():
                if k in self.pResult.keys():
                    self.pResult[k] += v
                else:
                    self.pResult[k] = v

    def Save(self):
        txt = []
        for k,v in self.pResult.iteritems():            
            txt.append('{0}: {1}'.format(k,v))
    
        with open('{0}.txt'.format(self.Targ.Name), 'w') as txt_file:
            txt_file.write('\n'.join(t for t in txt))
            
        Player.HeadMessage(82, 'Saved as {0}.txt in RazorEnhanced folder.'.format(self.Targ.Name))

SE = ScanEquip(Target.PromptTarget())
SE.Scan()
SE.Save()
        
