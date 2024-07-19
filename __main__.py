import sys
import scripts, manual, parser
import os

args = sys.argv
sdkdir = ''
prefix = os.path.expanduser('~')
datadir = prefix + '/.ftcandroid/'
confpath = datadir + 'ftcandroid.conf'
defaultconfig = ['sdkdir=']
version = 'v0.1.0'
args.pop(0)

if os.path.exists(datadir):
    if os.path.exists(confpath):
        with open(confpath, 'r') as f:
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

def cmdNotFound(arg):
    command = ''
    for i in range(len(arg)):
        command += arg[i]
        if i != len(arg) - 1:
            command += ' '
    print('Command: \'' + command + '\' not found')

manual = manual.help(cmdNotFound)
parser = parser.parser('ftc: command not found: ')

if len(args) <= 1:
    parser.check(['help', ''])
    exit()

if not os.path.exists('testing'):
    if sdkdir == '' and args[1] != 'setup':
        print('Please configure a SDK with \'ftc setup\' or with \'ftc set sdkdir <dir>\'')
        exit()

    if args[1] != 'setup' and args[1] != 'init' and not os.path.exists('local.properties'):
        if not os.path.exists('gradlew'):
            print('Please navigate to your FTC project and run \'ftc init\'')
        else:
            print('please run \'ftc init\' to finish setup')
        exit()


parser.add(['setup'], scripts.android.setup)
parser.add(['script'], scripts.gradle.sync)
parser.add(['set'], scripts.android.set)
parser.add(['init', 'initalize'], scripts.gradle.init)
parser.add(['build'], scripts.gradle.build)
parser.add(['run'], scripts.gradle.run)
parser.add(['install'], scripts.gradle.install)
parser.add(['help', '-h', '--h'], manual)

if len(args) == 0:
    print('FTCOnAll: ftc brought to all IDEs')
    while True:
        args = input('> ').split()
        parser.check(args)
else:
    parser.check(args)
