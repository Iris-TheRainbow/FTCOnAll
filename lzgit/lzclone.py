from sys import argv, platform
from os import system, getcwd, chdir
import sys
from tempfile import gettempdir

args = argv
args.pop(0)
if args[0] == '--help':
    print('lzclone: cloning for lazy people. It clones then automatically changes to that directory')
def getname(url):
    seperated = url.split('/')
    name = seperated[-1].split('.')[0]
    return name
tempdir = gettempdir()

system('git clone ' + args[0])
chdir(getname(args[0]))
dir = getcwd()
if platform == 'linux' or platform == 'darwin':
    with open(tempdir + '/cd.sh', 'w') as f:
        f.write('cd ' + dir)
    system(tempdir + '/cd.sh')
    system('rm ' + tempdir + '/cd.sh')
if platform == 'win32' or platform == 'cygwin':
    system('(dir 2>$1 *`|echo CMD);&<# rem #>echo PowerShell > ' + tempdir + '\\term.txt')
    term = open(tempdir + '\\term.txt', 'r').read()
    if term == 'CMD':
        with open(tempdir + '\\cd.bat', 'w') as f:
            f.write('cd ' + dir)
        system(tempdir + '\\cd.bat')
        system('rm ' + tempdir + '\\cd.bat')
    if term == 'PowerShell':
        with open(tempdir + '\\cd.ps1', 'w') as f:
            f.write('Push-Location ' + dir)
        system(tempdir + 'cd.ps1')
        system('rm ' + tempdir + '\\cd.bat')
