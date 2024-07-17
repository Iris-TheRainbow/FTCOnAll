# FTC On All
A simple program to allow you to build and install the FTCRobotController without using Android Studio

## Commands

`ftc setup`: installs the necessary Android SDK for the FTC Robot Controller, as well as Platform Tools (adb)
This maps essentially to what Android Studio does when you open a project for the first time


`ftc init`: creates `local.properties` for your FTC Robot Controller project
This maps essentially to what Android Studio does when you open a project for the first time


`ftc sync`: downloads all the Gradle dependences for your project
Since the Gradle sync that Android Studio does is not an actual Gradle function, this tries to force download them


`ftc run`: builds and installs the RC app
This is basically the equivalent of the run button in Android Studio. It builds, installs, then reboots the RC


`ftc build`: builds the RC app but does not install.
Good if `ftc sync` doesn't download dependencies and you need to install over wireless adb


`ftc install`: installs the most recently build RC app
If for some reason `ftc sync` isnt working, this will install the last build app


`ftc connect <chub/phone>`: connects to either a REV Control Hub or an Android phone over Wi-Fi ADB
This internally just runs adb connect 192.168.43.1/192.168.48.1 (depending on if you have a REV Control Hub or Android phone)


`ftc help`: provides more verbose help about a command with `ftc help <command>`. If no command is given, it shows this page.
