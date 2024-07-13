import sys
import scripts
import os, os.path

args = sys.argv
sdkdir = ''
prefix = os.path.expanduser('~')
datadir = prefix + '/.ftcandroid/'
<<<<<<< HEAD
confpath = datadir + 'ftcandroid.conf'
<<<<<<< HEAD
defaultconfig = ['sdkdir=']
=======
confpath = datadir + 'sdkpath.conf'
>>>>>>> parent of 74bcb81 (working sdk install and start of adb install)
=======
defaultconfig = ['sdkdir=', '\nadbdir=']
>>>>>>> parent of 36630e2 (instals adb sorta now, also sets up your ftc project and stuff)

if os.path.exists(confpath):
    with open(confpath) as f:
        sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
else:
<<<<<<< HEAD
    os.mkdir(datadir)
    with open(confpath, 'w') as f:
        f.writelines(defaultconfig)

if sdkdir == '':
    print('Please configure a SDK with \'ftc setup\' or with \'ftc set sdkdir <dir>\'')

if args[1] == 'setup':
    scripts.android.setup(confpath, datadir, sdkdir)
    pass
elif args[1] == 'sync':
    #scripts.gradle.sync()
    pass
elif args[1] == 'set':
    if args[2] == 'sdkdir':
        scripts.android.setsdkdir(confpath, args[3])
<<<<<<< HEAD
elif args[1] == 'init':
    scripts.android.init(sdkdir)
=======
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
>>>>>>> parent of 74bcb81 (working sdk install and start of adb install)
=======
>>>>>>> parent of 36630e2 (instals adb sorta now, also sets up your ftc project and stuff)
