#__init__.py
import os
from settings import ip_address_list, Timer_Type, Tapo
from scriptpaths import ipaddressesPATH, READWRITEPATHS
from tapo_timer import activate_plug

#Easy access definitions from functions/variables that were imported:
READWRITEPATHS = READWRITEPATHS()
READSTATE = READWRITEPATHS.READSTATE #requires strSTATE (as tstate or ipstate)
WRITESTATE = READWRITEPATHS.WRITESTATE #strSTATE and STATE (as a 0 or 1)

#converts the ip address list in the settings file to a file for the nmap software
def ip_address_list_generation():
    with open(ipaddressesPATH, 'w') as file:
        for ip in ip_address_list:
            file.write(f'{ip}\n')

def monitor_initialisation():
	#Monitor has to have known start states.
	print("Setting inital tstate and ipstate to: 1")
	#set monitor as initially on so we know the state
	os.popen('DISPLAY=:0.0 xrandr --output HDMI-1 --auto') #monitor initially set to on
	tstate = 1 #tstate set to 1 because monitor is on
	ipstate = 1 #ipstate set to 1 because monitor is on
	if Timer_Type in (1,3): #we are only going to write the states that we will use.
		WRITESTATE(strSTATE = "tstate", STATE = tstate) #write the state
	elif Timer_Type in (2,3):
		WRITESTATE(strSTATE = "ipstate", STATE = ipstate)
	else:
		WRITESTATE(strSTATE = "tstate", STATE = tstate)
		WRITESTATE(strSTATE = "ipstate", STATE = ipstate)
	if int(Tapo) == 1:
		activate_plug(Timer_Type = int(Timer_Type))
	else:
		pass
	print("\n**********Initialisation Complete**********")
	print (f"**********starting program #{Timer_Type}**********\n")
