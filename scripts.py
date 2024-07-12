import subprocess
import os
import sys

class gradle:
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
            print('Superuser is required for \'mkdir /opt/android-sdk\' and \'chmod 777 /opt/android-sdk\'')
            os.system('sudo mkdir /opt/android-sdk')
            os.system('sudo chmod 777 /opt/android-sdk')
            print('Made /opt/android-sdk readable and writiable for all')

            print('Attempting to install the android sdk')
            os.system('sudo sdkmanager "platforms;android-29"')

        print('Please accept the licence agreements for the Android platform')
        os.system('sdkmanager --licenses')

        print('Creating \'local.properties\'')
        with open('local.properties', 'w') as f:
            f.write('sdk.dir=/opt/android-sdk/platforms/android-29')

        print('Android SDK is set up!')

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
    def setup():
        gradle.sdksetup()
        gradle.adbsetup()
        platform = sys.platform
        if platform == 'Linux' or 'Darwin':
            with open('~/.android-sdk-locaiton.info', 'w') as f:
                f.write('/opt/android-sdk')
        if platform == 'windows':
            os.mkdir('%AppData%/local/ftc-android')
            with open('%AppData%/local/ftc-android/android-sdk-location.info', 'w') as f:
                f.write('C://...')


    @staticmethod
    def sync():
        os.system('./gradlew sync')
