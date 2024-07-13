import subprocess
import os
import sys
import sdkmanager

class android:
    @staticmethod
    def setsdkdir(confpath, sdkpath):
        content = []
        with open(confpath, 'r') as f:
            content = f.read().splitlines()
        with open(confpath, 'w+') as f:
            content[0] = 'sdkdir=' + sdkpath
            f.writelines(content)

    @staticmethod
    def sdksetup(confpath, datadir):
        print('Setting SDK path')
        sdkdir = datadir + 'android_sdk'
        android.setsdkdir(confpath, sdkdir)

        print('Installing Android SDK')
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platforms;android-29", sdkdir)

        print('Please accept the Android SDK licenses')
        sdkmanager.licenses()

    @staticmethod
    def adbsetup(confpath, datadir, sdkdir):
        print('Installing Platform Tools')
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platform-tools", sdkdir)
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platform-tools", sdkdir)

    @staticmethod
    def setup(confpath, datadir, sdkdir):
        android.sdksetup(confpath, datadir)
        android.adbsetup(confpath, datadir, sdkdir)
        android.init(sdkdir)

    @staticmethod
    def init(sdkdir):
        if os.path.exists('gradlew'):
            if not os.path.exists('local.properties'):
                with open('local.properties', 'w') as f:
                    f.write('sdkdir=' + sdkdir)
        else:
            print('Please navigate to your FTC project and run \'ftc init\'')
