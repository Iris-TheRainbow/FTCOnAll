import subprocess
import os
import sys
import sdkmanager

class android:
    @staticmethod
    def setsdkdir(confpath, sdkpath):
        with open(confpath, 'w+') as f:
            content = f.readlines()
            content[0] = 'sdkdir=' + sdkpath
            f.writelines(content)

    @staticmethod
    def sdksetup(confpath, datadir):
        print('Setting SDK path')
        sdkdir = datadir + '/android_sdk'
        android.setsdkdir(confpath, sdkdir)

        print('Installing Android SDK')
        sdkmanager.build_package_list(use_net=False)
        sdkmanager.install("platforms;android-29", sdkdir)

        print('Please accept the Android SDK licenses')
        sdkmanager.licenses()

    @staticmethod
    def adbsetup(confpath, datadir):
        pass
