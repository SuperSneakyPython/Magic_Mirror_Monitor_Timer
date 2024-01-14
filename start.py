#main.py
from __init__ import ip_address_list_generation, monitor_initialisation #convert ip in settings file to nmap readable file, and get initial monitor state as on (tstate/ipstate = 1)
from settings import Timer_Type #gets the value for which loop the user specified. You can also specify it as the main() variable.
from monitor_timer import main #this contains the 3 loops.

main(Timer_Type = int(Timer_Type))
