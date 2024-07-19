import os

class parser:
    def __init__(self, notfoundmsg):
        self.commands = []
        self.notfoundmsg = notfoundmsg

    def check(self, args):
        string = args[0]
        args.pop(0)
        for command in self.commands:
                for name in command[0]:
                    if name == string:
                        command[1](args)
                        return
        self.notFound()

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
        datadir = os.path.expanduser('~') + '/.ftcandroid'
        confpath  = datadir + '/ftcandroid.conf'
        sdkdir = open(confpath, 'r').read().removeprefix('sdkdir=')

        for command in self.commands:
            names = ''
            for name in command[0]:
                names += name
                if not name == command[0][-1]:
                    names += ', '
            cmdname = str(command[1].__name__)

            print(str(names) + ': ' + cmdname + '()')
