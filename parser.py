import os

from requests.sessions import merge_setting

class parser:
    def __init__(self, notfoundmsg):
        self.commands = []
        self.notfoundmsg = notfoundmsg
        self.lockoutlist = []

    def check(self, args):
        datadir = os.path.expanduser('~') + '/.ftcandroid/'
        confpath  = datadir + 'ftcandroid.conf'
        sdkdir = open(confpath, 'r').read().removeprefix('sdkdir=')

        string = args[0]
        args.pop(0)
        if self.lockout(confpath, datadir, sdkdir, args, string) == -1:
            return
        for command in self.commands:
                for name in command[0]:
                    if name == string:
                        command[1](confpath, datadir, sdkdir, args)
                        return
        self.notFound()

    def addlockout(self, condition, msg, unless):
        self.lockoutlist.append((condition, msg, unless))

    def lockout(self, confpath, datadir, sdkdir, args, name):
        bypass = False
        for command in self.lockoutlist:
            for unless in command[2]:
                if name in unless:
                    bypass = True
            if not bypass and not command[0](confpath, datadir, sdkdir, args):
                print(command[1])
                return -1
        return 1


    def add(self, names, func):
        self.commands.append((names, func))

    def remove(self, name):
        try:
            self.commands.remove(name)
        except ValueError:
            self.notFound()

    def notFound(self):
        print(self.notfoundmsg)

    def list(self):
        for command in self.commands:
            names = ''
            for name in command[0]:
                names += name
                if not name == command[0][-1]:
                    names += ', '
            cmdname = str(command[1].__name__)

            print(str(names) + ': ' + cmdname + '()')
