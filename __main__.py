import sys
import scripts
import os

args = sys.argv
sdkdir = ''
if sys.platform == 'Windows':
    prefix = '%AppData%'
else:
    prefix = '~'
datadir = prefix + '/.ftcandroid/'
confpath = datadir + 'sdkpath.conf'

if os.path.exists(confpath):
    with open(confpath) as f:
        sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
else:
    os.mkdir(datadir)

os.system('export ANDROID_HOME=' + sdkdir)

if args[1] == 'setup':
    #scripts.android.setup()
    pass
elif args[1] == 'sync':
    #scripts.gradle.sync()
    pass
elif args[1] == 'set':
    if args[2] == 'sdkdir':
