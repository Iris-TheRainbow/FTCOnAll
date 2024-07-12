import subprocess
import os
import sys

class gradle:
    @staticmethod
    def sync():
        os.system('./gradlew sync')

class android():
    @staticmethod
    def adbsetup():
        if sys.platform == 'Windows':
            platform = 'win'
            sdkdir = 'C:\\....'
        else:
            platform = '*nix'
            sdkdir = '/opt/android-sdk'
        if platform == '*nix'
            print('Superuser is required to install ADB')
            os.system('sudo sdkmanager --install "platform-tools"')
        else:
            print('Installing ADB')
            os.system('sdkmanager --install "platform-tools"')

        print('Please accept the licenses')
        os.system('sdkmanager --licenses')

    @staticmethod
    def sdksetup():
        if sys.platform == 'Windows':
            platform = 'win'
            sdkdir = 'C:\\....'
        else:
            platform = '*nix'
            sdkdir = '/opt/android-sdk'

        try:
            subprocess.check_output('sdkmanager --version', shell=True, text=True)
        except:
            print('Android sdkmanager not found. Please install it and try again')
            exit()

        if platform == '*nix'
            if not os.path.exists('~/.ftcandroid'):
                os.mkdir('~/.ftcandroid')
                os.mkdir('~/.ftcandroid/sdkmanager')
            os.system('git clone https://gitlab.com/fdroid/sdkmanager.git ~/.ftcandroid/sdkmanager')
            print('Attempting to install the android sdk')
            os.system('sudo sdkmanager "platforms;android-29"')

        print('Please accept the licence agreements for the Android platform')
        os.system('sdkmanager --licenses')

        print('Creating \'local.properties\'')
        with open('local.properties', 'w') as f:
            f.write('sdk.dir=/opt/android-sdk/platforms/android-29')

        print('Android SDK is set up!')

    @staticmethod
    def setup():
        android.sdksetup()
        android.adbsetup()
        platform = sys.platform
        if platform == 'Linux' or 'Darwin':
            with open('~/.android-sdk-locaiton.info', 'w') as f:
                f.write('/opt/android-sdk')
        if platform == 'windows':
            os.mkdir('%AppData%/local/ftc-android')
            with open('%AppData%/local/ftc-android/android-sdk-location.info', 'w') as f:
                f.write('C://...')
