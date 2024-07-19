def argsToString(args):
    try:
        string = ''
        for i in range(len(args)):
            string += args[i]
            if i+1 != len(args):
                string += ' '
    except AttributeError:
        string = args
    return string

class commandhelp:
    def __init__(self, command, short, alt):
        self.command = command
        self.short = short
        self.alt = alt

class help:
    def __init__(self, cmdnotfound):
        setup = commandhelp('ftc setup', 'installs the necessary Android SDK for the FTC Robot Controller, as well as Platform Tools (adb)', 'This maps essentially to what Android Studio does when you open a project for the first time')
        init = commandhelp('ftc init', 'creates local.properties for your FTC Robot Controller project', 'This maps essentially to what Android Studio does when you open a project for the first time')
        sync = commandhelp('ftc sync', 'downloads all the Gradle dependences for your project', 'Since the Gradle sync that Android Studio does is not an actual Gradle function, this tries to force download them')
        run = commandhelp('ftc run',  'builds and installs the RC app', 'This is basically the equivalent of the run button in Android Studio. It builds, installs, then reboots the RC')
        build = commandhelp('ftc build', 'builds the RC app but does not install.', 'Good if \'ftc sync\' doesn\'t download dependencies and you need to install over wireless adb')
        install = commandhelp('ftc install', 'installs the most recently build RC app', 'If for some reason \'ftc sync\' isnt working, this will install the last build app')
        connect = commandhelp('ftc connect <chub/phone>', 'connects to either a REV Control Hub or an Android phone over Wi-Fi ADB', 'This internally just runs adb connect 192.168.43.1/192.168.48.1 (depending on if you have a REV Control Hub or Android phone)')
        help = commandhelp('ftc help', 'provides more verbose help about a command with \'ftc help <command>\'. If no command is given, it shows this page.', 'This is help. Its not that hard.')
        self.commands = [
            ('setup', setup),
            ('init', init),
            ('sync', sync),
            ('run', run),
            ('build', build),
            ('install', install),
            ('connect', connect),
            ('help', help)
        ]
        self.cmdnotfound = cmdnotfound


    def help(self, confpath: str, datadir: str, sdkdir: str, args):
        name = argsToString(args)
        alt = True
        if name == '':
            print('FTC For All v0.1.1')
            alt = False
        for command in self.commands:
            if name in command[0]:
                print(command[1].command + ': ' + command[1].short)
                if alt:
                    print(command[1].alt)
