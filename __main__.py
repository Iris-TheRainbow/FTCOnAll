import sys
import scripts
import os

args = sys.argv
sdkdir = ''
prefix = os.path.expanduser('~')
datadir = prefix + '/.ftcandroid/'
confpath = datadir + 'ftcandroid.conf'
defaultconfig = ['sdkdir=']

if os.path.exists(datadir):
    print('data exists')
    if os.path.exists(confpath):
        print('conf exists')
        with open(confpath, 'r') as f:
            print('read sdk dir')
            try:
                sdkdir = str(f.read().splitlines()[0]).removeprefix('sdkdir=')
                os.environ['ANDROID_HOME'] = sdkdir

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

if len(args) <= 1:
    scripts.manual.full()
    exit()

if sdkdir == '' and args[1] != 'setup':
    print('Please configure a SDK with \'ftc setup\' or with \'ftc set sdkdir <dir>\'')
    exit()
if args[1] != 'setup' and args[1] != 'init' and not os.path.exists('local.properties'):
    if not os.path.exists('gradlew'):
        print('Please navigate to your FTC project and run \'ftc init\'')
    else:
        print('please run \'ftc init\' to finish setup')
    exit()

if args[1] == 'setup':
    scripts.android.setup(confpath, datadir, sdkdir)
    pass
elif args[1] == 'sync':
    scripts.gradle.sync()
    pass
elif args[1] == 'set':
    if args[2] == 'sdkdir':
        scripts.android.setsdkdir(confpath, args[3])
elif args[1] == 'init':
    scripts.gradle.init(sdkdir)
elif args[1] == 'build':
    scripts.gradle.build()
elif args[1] == 'run':
    scripts.gradle.run(sdkdir)
elif args[1] == 'install':
    scripts.gradle.install(sdkdir)
elif args[1] == 'help':
    if len(args) <= 2:
        scripts.manual.full()
    elif len(args) > 2:
        scripts.manual.single(args[3])
