#pressing escape
import sys

python27InstallDir = 'C:\\Python2713'
pathsToAdd = [
    python27InstallDir,
    python27InstallDir + '\\Lib',
    python27InstallDir + '\\Lib\\site-packages',
]

for path in pathsToAdd:
    if not path in sys.path:
        sys.path.append( path )

import keyboard
Player.HeadMessage(54, 'pressing esc')
keyboard.press( 'esc' )
Misc.Pause( 20 )
keyboard.release( 'esc' )
