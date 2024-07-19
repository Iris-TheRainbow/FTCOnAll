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
                os.environ['ANDROID_HOME'] = sdkdir
            except:
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
parser = parser.parser('ftc: command not found:')

parser.add(['setup'], scripts.android.setup)
parser.add(['sync'], scripts.gradle.sync)
parser.add(['set'], scripts.android.set)
parser.add(['init', 'initalize'], scripts.gradle.init)
parser.add(['build'], scripts.gradle.build)
parser.add(['run'], scripts.gradle.run)
parser.add(['install'], scripts.gradle.install)
parser.add(['connect'], scripts.adb.connect)
parser.add(['help', '-h', '--h'], manual.help)

parser.addlockout(scripts.sdkpathset, 'Please run \'ftc setup\' or set an Android SDK dir with \'set sdkdir <dir>\'', ['help', '-h', '--h', 'setup', 'set'])
parser.addlockout(scripts.inited, 'Please navigate to your FTC project and run \'ftc init\'', ['help', '-h', '--h', 'setup', 'set', 'init', 'initalize'])

if len(args) == 0:
    print('FTCOnAll: ftc brought to all IDEs')
    while True:
        args = input('> ').split()
        parser.check(args)
else:
    parser.check(args)
