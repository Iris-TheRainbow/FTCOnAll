import sys
import scripts
import os

args = sys.argv
sdkdir = ''
prefix = os.path.expanduser('~')
datadir = prefix + '/.ftcandroid/'
confpath = datadir + 'ftcandroid.conf'
defaultconfig = ['sdkdir=', '\nadbdir=']

if os.path.exists(datadir):
    print('data exists')
    if os.path.exists(confpath):
        print('conf exists')
        with open(confpath, 'r') as f:
            print('read sdk dir')
            try:
                sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
            except:
                print('wrote default')
                with open(confpath, 'w+') as fi:
                    fi.writelines(defaultconfig)
    else:
        with open(confpath, 'w') as f:
            f.writelines(defaultconfig)
else:
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
