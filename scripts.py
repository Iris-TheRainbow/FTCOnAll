import subprocess
import os

class gradle:
    @staticmethod
    def sdksetup():
        try:
            subprocess.check_output('sdkmanager --version', shell=True, text=True)
        except:
            print('Android sdkmanager not found. Please install it and try again')
            exit()
        print('Superuser is required for \'mkdir /opt/android-sdk\' and \'chmod 777 /opt/android-sdk\'')
        os.system('sudo mkdir /opt/android-sdk')
        os.system('sudo chmod 777 /opt/android-sdk')
        print('made /opt/android-sdk readable and writiable for all')
        print('w')

    @staticmethod
    def setup():
        gradle.sdksetup()
