import subprocess
import os
import sys
import sdkmanager

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

def version(confpath: str, datadir: str, sdkdir: str, args):
    print('FTC On All v0.1.0')

class android:
    @staticmethod
    def set(confpath: str, datadir: str, sdkdir: str, args):
        if args[0] == 'sdkdir':
            content = []
            with open(confpath, 'r') as f:
                content = f.read().splitlines()
            with open(confpath, 'w+') as f:
                content[0] = 'sdkdir=' + sdkdir
                f.writelines(content)

    @staticmethod
    def sdksetup(confpath: str, datadir: str, sdkdir: str, args):
        print('Setting SDK path')
        sdkdir = datadir + 'android_sdk'
        args = ['sdkdir', sdkdir]
        android.set(confpath, datadir, sdkdir, args)
        os.environ['ANDROID_HOME'] = sdkdir

        print('Installing Android SDK')
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platforms;android-29", sdkdir)
        print('Installing Platform Tools')
        sdkmanager.install("platform-tools", sdkdir)

        print('Please accept the Android SDK licenses')
        sdkmanager.licenses()

    @staticmethod
    def setup(confpath: str, datadir: str, sdkdir: str, args):
        android.sdksetup(confpath, datadir, sdkdir, args)
        gradle.init(confpath, datadir, sdkdir, args)

class gradle:
    @staticmethod
    def init(confpath: str, datadir: str, sdkdir: str, args):
        if os.path.exists('gradlew'):
            if sys.platform.lower() == 'darwin' or sys.platform.lower() == 'linux':
                os.system('sudo chmod +x gradlew')
            if not os.path.exists('local.properties'):
                with open('local.properties', 'w') as f:
                    f.write('sdkdir=' + sdkdir)
        else:
            print('Please navigate to your FTC project and run \'ftc init\'')

    @staticmethod
    def sync(confpath: str, datadir: str, sdkdir: str, args):
        os.system('./gradlew --stop')
        os.system('./gradlew')

    @staticmethod
    def build(confpath: str, datadir: str, sdkdir: str, args):
        os.system('./gradlew build')

    @staticmethod
    def run(confpath: str, datadir: str, sdkdir: str, args):
        os.system('./gradlew --offline build')
        gradle.install(confpath, datadir, sdkdir, args)

    @staticmethod
    def install(confpath: str, datadir: str, sdkdir: str, args):
        os.system(sdkdir + '/platform-tools/adb install TeamCode/build/outputs/apk/releases/TeamCode-release.apk')
        os.system(sdkdir + '/platform-tools/adb reboot')


class adb:
    @staticmethod
    def connect(confpath: str, datadir: str, sdkdir: str, args):
        device = args[0]
        ip = ''
        if device == 'chub':
            ip = '192.168.43.1'
        elif device == 'phone':
            ip = '192.168.48.1'
        else:
            print('device not found. Valid devices are \'chub\' or \'phone\'')
            return
        os.system(sdkdir + '/platform-tools/adb connect ' + ip)
