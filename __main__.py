import sys
import scripts
import os, os.path

args = sys.argv
sdkdir = ''
prefix = os.path.expanduser('~')
datadir = prefix + '/.ftcandroid/'
confpath = datadir + 'sdkpath.conf'

if os.path.exists(confpath):
    with open(confpath) as f:
        sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
else:
    print('Please run \'ftc setup\' or specify an Android SDK directory with \'ftc set sdkdir <dir>\'')
try:
    if args[1] == 'setup':
        scripts.android.sdksetup(confpath, datadir)
        pass
    elif args[1] == 'sync':
        #scripts.gradle.sync()
        pass
    elif args[1] == 'set':
        if args[2] == 'sdkdir':
            scripts.android.setsdkdir(confpath, args[3])
except IndexError:
    print('args')
