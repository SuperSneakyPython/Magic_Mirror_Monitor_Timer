#monitor_timer.py
import os
from time import sleep
from datetime import datetime as dt
from __init__ import ip_address_list_generation, monitor_initialisation #Set initial monitor state as on (tstate/ipstate = 1) and load ip addresses.
from scriptpaths import ipaddressesPATH, READWRITEPATHS
from settings import On_Time, Off_Time, Timer_Type, Tapo
from tapo_timer import activate_plug

#Easy access definitions from functions/variables that were imported:
READWRITEPATHS = READWRITEPATHS()
READSTATE = READWRITEPATHS.READSTATE #requires strSTATE (as tstate or ipstate)
WRITESTATE = READWRITEPATHS.WRITESTATE #strSTATE and STATE (as a 0 or 1)

def timer():
    time = int(dt.now().strftime('%H%M')) #get time as integer in form of 0 to 2399
    print("The current time is: " + str(time))
    if(On_Time < time > Off_Time): #on/off from settings.py
        if int(READSTATE(strSTATE = "tstate")) == 0:
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
            pass
        else:
            os.popen('DISPLAY=:0.0 xrandr --output HDMI-1 --off')  #Bash command that turns off the display
            tstate = '0'
            WRITESTATE(strSTATE = "tstate", STATE = tstate)
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
    else:
        if READSTATE(strSTATE = "tstate") == 1:
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
            pass
        else:
            os.popen('DISPLAY=:0.0 xrandr --output HDMI-1 --auto')  #Bash command that turns on the display
            tstate = '1'
            WRITESTATE(strSTATE = "tstate", STATE = tstate)
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
    if int(Tapo) == 1: #calls on tapo plug module if you set tapo=1 in settings.py
        activate_plug(Timer_Type = int(Timer_Type))
    else:
        pass

def timer_loop():
    while True:
        timer()
        print("____________________\n")
        print("waiting 30 minutes to check again")
        print("____________________\n")
        sleep(1800)
        print("checking again")

def nmap_protocol():
    #nmap processing here. checks if any of the input ip are avaliable.
    nmap = os.popen('nmap --unprivileged -iL ' + ipaddressesPATH)
    nmap_output = nmap.read()
    nmap_output_val = nmap_output.find('host up') #will be -1 if no ip in the list found
    print("nmap got network information. Printing below:\n")
    print(nmap_output)
    #if statements for monitor on or off if ip address is connected to network
    if nmap_output_val == -1:  #-1 if no ip found. Therefore we will turn off the monitor and plugs.
        if int(READSTATE(strSTATE = "ipstate")) == 0:
            print("monitor is on or off: " + str(READSTATE(strSTATE = "ipstate")))
        else:
            os.popen('DISPLAY=:0.0 xrandr --output HDMI-1 --off')  #Bash command that turns off the display
            ipstate = '0'
            WRITESTATE(strSTATE = "ipstate", STATE = ipstate)
            print("monitor is on or off: " + str(READSTATE(strSTATE = "ipstate")))
    else:
        if int(READSTATE(strSTATE = "ipstate")) == 1:
            print("monitor is on or off: " + str(READSTATE(strSTATE = "ipstate")))
        else:
            os.popen('DISPLAY=:0.0 xrandr --output HDMI-1 --auto') #Bash command to turn on the display
            ipstate = '1'
            WRITESTATE(strSTATE = "ipstate", STATE = ipstate)
            print("monitor is on or off: " + str(READSTATE(strSTATE = "ipstate")))
    if int(Tapo) == 1: #calls on tapo plug module if you set tapo=1 in settings.py
        activate_plug(Timer_Type = int(Timer_Type))
    else:
        pass

def nmap_protocol_loop():
    while True:
        nmap_protocol()
        print("____________________\n")
        print("waiting 60 seconds to check again")
        print("____________________\n")
        sleep(60)
        print("checking again")

def Check_tSTATE():
    #just for checking tSTATE without turning the monitor on or off. Required for timer_AND_nmap_loop()
    time = int(dt.now().strftime('%H%M')) #get time as integer in form of 0 to 2399
    print("The current time is: " + str(time))
    if(On_Time < time > Off_Time): #on/off from settings.py
        if int(READSTATE(strSTATE = "tstate")) == 0:
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
            pass
        else:
            tstate = '0'
            WRITESTATE(strSTATE = "tstate", STATE = tstate)
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
    else:
        if READSTATE(strSTATE = "tstate") == 1:
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))
            pass
        else:
            tstate = '1'
            WRITESTATE(strSTATE = "tstate", STATE = tstate)
            print("monitor is on or or off: " + str(READSTATE(strSTATE = "tstate")))

def timer_AND_nmap_loop():
    print("Checking time")
    while True:
        if int(READSTATE(strSTATE = "tstate")) == 1:
            Check_tSTATE() #need to know if the tstate is still 1 before running nmap again.
            nmap_protocol()
            print("____________________\n")
            print("waiting 60 seconds to check again")
            print("____________________\n")
            sleep(60)
            print("checking again")
        else:
            timer()
            print("____________________\n")
            print("waiting 30 minutes to check again")
            print("____________________\n")
            sleep(1800) #only allows Time_on and Time_off to be set in 30 min intervals. Reduce to allow smaller.
            print("checking again")

#This is the function that decides which loop to run based on the Timer_Type in the settings.py. Specify it in start.py or as a main() variable.
def main(Timer_Type):
    if int(Timer_Type) == 2 or int(Timer_Type) == 3:
        ip_address_list_generation()
    else:
        pass
    monitor_initialisation()
    if int(Timer_Type) == 1:
        timer_loop()
    elif int(Timer_Type) == 2:
        nmap_protocol_loop()
    elif int(Timer_Type) == 3:
        timer_AND_nmap_loop()
    else:
        pass

#last line ensures that only main() is run when imported later.
if '__main__' == __name__:
        main()
