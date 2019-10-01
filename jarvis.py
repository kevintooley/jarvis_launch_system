#!/usr/bin/env python3
'''
## License

This program is the property of Kevin Tooley and shall be considereproprietary. 
 
'''

from num2words import num2words
from subprocess import call
import time
import sys
import os

cmd_beg = 'pico2wave -w tmp.wav '
cmd_end = 'aplay tmp.wav'


def conv_message(message):
    return message.replace(' ', '_')
	
def speak_message(message):
    
    print(message)

    cmd_beg = 'pico2wave -l \"en-US\" -w tmp.wav \"' + message + '\"'
	
    print(cmd_beg)
	
	#call([cmd_beg], shell=True)
    os.system(cmd_beg)
    os.system(cmd_end) #call([cmd_end], shell=True)
	
	
def main_menu():
	
	print("")
	print(" 1. Turn Key to ON")
	print(" 2. Turn Key to OFF")
	print(" 3. ARM the system")
	print(" 4. DISARM the system")
	print(" 5. Set a launch timer")
	print(" 6. Conduct a manual launch")
	try:
		choice = int(input("Enter a number: "))
	except KeyboardInterrupt:
		print("\n\nGoodbye...\n")
		sys.exit(1)
	
	exec_menu(choice)
	return
	
def exec_menu(choice):
	
	try:
		menu_actions[choice]()
	except KeyError:
		print("Invalid selection, please try again.")

	
def key_on():
	speak_message("I detected that you enabled the launch system.")
	speak_message("running system diagnostics now.")

	
def key_off():
	speak_message("Launcher power is off.")

	
def arm_system():
	speak_message("Warning.  The fire control loop has been activated and armed.")
	speak_message("Standing by for rocket launch.")

	
def disarm_system():
	speak_message("The system has been disarmed.  The launcher is safe.")


def set_timer():
    speak_message("I will start a launch countdown for you.  How many seconds for the timer?")
    x = int(input("Enter a number: "))
    tmp_message = "Starting a " + str(x) + " second countdown."
    speak_message(tmp_message)
	
    #To do a Count Down
    for i in range(x,-1,-1): # To count numbers down from the entered number till zero
        if i == 0:
            speak_message("Launch!")
        else:
            cmd = num2words(i) + "." #To convert the Numbers to Text
            print(cmd)
            speak_message(cmd)
	
	
menu_actions = {
	1: key_on,
    2: key_off,
    3: arm_system,
    4: disarm_system,
	5: set_timer,
}


speak_message("Good day sir.")

speak_message("I am standing by for your instructions.")

while True:
	main_menu()


