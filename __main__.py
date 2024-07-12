import sys
import scripts
import os

args = sys.argv

if args[1] == 'setup':
    scripts.gradle.setup()
elif args[2] == 'sync':
    scripts.gradle.sync()
