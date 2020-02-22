import os
name = 'MovieCut'
os.system('pyinstaller --workpath builds --distpath builds\distpath --specpath builds\specpath -n '+name+' -F main.py')
