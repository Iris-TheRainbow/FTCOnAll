import sys, os

args = sys.argv
args.pop(0)
if args[0] == '--help':
    print('lzcommit: committing for lazy people. It stagess your changes, commits with the message you leave after the `lzcommit` command, and then pushes to remote')
commitmsg = ''
for i in range(len(args)):
    commitmsg += args[i] + ' '
os.system('git stage .')
os.system('git commit -m "' + commitmsg + '"')
os.system('git push')
