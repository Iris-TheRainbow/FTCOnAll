import subprocess
import os
import sys
import sdkmanager

class android:
    @staticmethod
    def setsdkdir(confpath: str, sdkpath: str):
        content = []
        with open(confpath, 'r') as f:
            content = f.read().splitlines()
        with open(confpath, 'w+') as f:
            content[0] = 'sdkdir=' + sdkpath
            f.writelines(content)

    @staticmethod
    def sdksetup(confpath: str, datadir: str):
        print('Setting SDK path')
        sdkdir = datadir + 'android_sdk'
        android.setsdkdir(confpath, sdkdir)
        os.environ['ANDROID_HOME'] = sdkdir

        print('Installing Android SDK')
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platforms;android-29", sdkdir)
        print('Installing Platform Tools')
        sdkmanager.install("platform-tools", sdkdir)

        print('Please accept the Android SDK licenses')
        sdkmanager.licenses()

    @staticmethod
    def setup(confpath: str, datadir: str, sdkdir: str):
        android.sdksetup(confpath, datadir)
        gradle.init(sdkdir)

class gradle:
    @staticmethod
    def init(sdkdir: str):
        if os.path.exists('gradlew'):
            if not os.path.exists('local.properties'):
                with open('local.properties', 'w') as f:
                    f.write('sdkdir=' + sdkdir)
        else:
            print('Please navigate to your FTC project and run \'ftc init\'')

    @staticmethod
    def sync():
        os.system('./gradlew --stop')
        os.system('./gradlew')

    @staticmethod
    def build():
        os.system('./gradlew build')

    @staticmethod
    def run(sdkdir: str):
        os.system('./gradlew build')
        gradle.install(sdkdir)

    @staticmethod
    def install(sdkdir: str):
        os.system(sdkdir + '/platform-tools/adb install TeamCode/build/outputs/apk/releases/TeamCode-release.apk')
        os.system(sdkdir + '/platform-tools/adb reboot')


class adb:
    @staticmethod
    def connect(device: str, sdkdir: str):
        ip = ''
        if device == 'chub':
            ip = '192.168.43.1'
        else:
            ip = '192.168.48.1'
        os.system(sdkdir + '/platform-tools/adb connect ' + ip)

class manual:
    @staticmethod
    def full():
        print('placeholder for a full manual')

    @staticmethod
    def single(command: str):
        if command == 'setup'
            print('placeholder')
