def full(version):
    print('FTC For All ' + version)
    print('Help:')
    print('ftc setup: installs the necessary Android SDK for the FTC Robot Controller, as well as Platform Tools (adb)')
    print('ftc init: creates local.properties for your FTC Robot Controller project')
    print('ftc sync: downloads all the Gradle dependences for your project')
    print('ftc run: builds and installs the RC app')
    print('ftc build: builds the RC app but does not install.')
    print('ftc install: installs the most recently build RC app')
    print('ftc connect <chub/phone>: connects to either a REV Control Hub or an Android phone over Wi-Fi ADB')
    print('ftc help <optional command>: displays either this or the specific help for a command if a command is provided')

def single(command: str):
    if command == 'setup':
        print('ftc setup: installs the necessary Android SDK for the FTC Robot Controller, as well as Platform Tools (adb)')
        print('This maps essentially to what Android Studio does when you open a project for the first time')
    elif command == 'init':
        print('ftc init: creates local.properties for your FTC Robot Controller project')
        print('local.properties most importantly tells Gradle where to find the Android SDK')
    elif command == 'sync':
        print('ftc sync: downloads all the Gradle dependences for your project')
        print('Since the Gradle sync that Android Studio does is not an actual Gradle function, this tries to force download them')
    elif command == 'run':
        print('ftc run: builds and installs the RC app')
        print('This is basically the equivalent of the run button in Android Studio. It builds, installs, then reboots the RC')
    elif command == 'build':
        print('ftc build: builds the RC app but does not install.')
        print('Good if \'ftc sync\' doesn\'t download dependencies and you need to install over wireless adb')
    elif command == 'install':
        print('ftc install: installs the most recently build RC app')
        print('If for some reason \'ftc sync\' isnt working, this will install the last build app')
    elif command == 'connect':
        print('ftc connect <chub/phone>: connects to either a REV Control Hub or an Android phone over Wi-Fi ADB')
        print('This internally just runs adb connect 192.168.43.1/192.168.48.1 (depending on if you have a REV Control Hub or Android phone)')
