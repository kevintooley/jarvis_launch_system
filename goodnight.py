#!/usr/bin/env python3
import time

from subprocess import call

cmd_beg= 'espeak '
cmd_end= ' 2>/dev/null' # To dump the std errors to /dev/null

goodnight = "goodnight_klair"
print("goodnight claire")

#Calls the Espeak TTS Engine to read aloud a Text
call([cmd_beg + goodnight + cmd_end], shell=True)

time.sleep(1)

call([cmd_beg + "I_love_you" + cmd_end], shell=True)


