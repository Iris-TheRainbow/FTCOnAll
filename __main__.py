import sys
import scripts
import os

args = sys.argv
sdkdir = ''
if sys.platform == 'Windows':
    prefix = '%AppData%'
else:
    prefix = '~'
datapath = prefix + '/.ftcandroid/'
confpath = datapath + 'sdkpath.conf'
if os.path.exists(confpath):
    with open(confpath) as f:
        sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
else:
    os.mkdir(datapath)

os.system('export ANDROID_HOME=' + sdkdir)

if args[1] == 'setup':
    scripts.android.setup()
elif args[1] == 'sync':
    scripts.gradle.sync()
elif args[1] == 'set':
    if args[2] == 'sdkdir':
        with open(confpath, 'w+') as f:
            content = f.readlines()
            content[0] = 'sdkdir=' + args[3]
            f.writelines(content)
