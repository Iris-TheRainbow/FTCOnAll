import subprocess
import os
import sys

class android:
    @staticmethod
    def setsdkdir(confpath, sdkpath):
        with open(confpath, 'w+') as f:
            content = f.readlines()
            content[0] = 'sdkdir=' + sdkpath
            f.writelines(content)
        os.system()

    @staticmethod
    def sdksetup(datadir):
        sdkmandir = datadir + 'sdkmanager'
        if not os.path.exists(sdkmandir):
            os.mkdir(sdkmandir)

            print('Downloading sdkmanager')
            os.system('git clone https://gitlab.com/fdroid/sdkmanager.git ' + sdkmandir)
