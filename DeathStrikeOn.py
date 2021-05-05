Misc.ScriptStop('PrimaryOn.py')
Misc.ScriptStop('SecondaryOn.py')
Misc.ScriptStop('EvasionOn.py')
Misc.ScriptStop('FocusAttackOn.py')

def main():
    if not Player.SpellIsEnabled('Death Strike'):
        Spells.CastNinjitsu("Death Strike")
        Misc.Pause(500)

while True:
    main()
    Misc.Pause(500)
