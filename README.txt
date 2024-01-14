#README.txt
Module was debugged with icecream -> (https://github.com/gruns/icecream)
This code is designed to function with a Raspberry Pi 5 using Rasbian OS.
I have tested it with a Raspberry pi B+ and it also works.

For this to work please install nmap for raspbian:
        >sudo apt-get install nmap
and please disable monitor sleeping in the raspi-config:
        >sudo raspi-config
        then navigate to the display settings and make sure monitor sleep is set to off. Restart.
To switch the monitor on and off we use xrandr which is installed by default on Raspbian with the Desktop environment.

The following module has three functions that can be used. They are defined in the settings.py file by adding a value to Timer_Type.
Timer_Type can be a number between 1 to 3.

The following Timer_Type values will do the following things:

1. This will turn the monitor on and off by using the time (local time of computer). 
        You set the On_Time and Off_Time with the variables in settings.py.

2. This will turn the monitor on and off by using the ip address of a device on the local network.
        For example a phone which when connected to the network will turn the screen on or off.
        Set the ip address that you want to check as a list in settings.py under ip_address_list.
        The list should look like follows:
        ip_address_list = [
                        'ip.one.X.X',
                        'ip.two.X.X',
                        'ip.three.X.X',
                        ]

3. Uses both options 1 and 2. If the time means the screen can be turned on, then it will check for the
        ip address on the network. If it finds the ip address it will then allow the monitor to be turned on, otherwise
        the monitor will be switched off.

Useage:
For those unfamiliar with python3 and would just like to use the script do the following:
    To download:
        mkdir Monitor_Timer
        cd Monitor_Timer
        git clone https://github.com/JJGaston/Magic_Mirror_Monitor_Timer.git
    Edit the following file with a 1, 2 or 3 as stated above to use the relevant loops:
        >sudo nano ~/Monitor_Timer/settings.py
        In the settings file add the following settings (#indicates a comment!):
            On_Time = 0 - 2399 #time in the format of 00:00 without leading zeros, e.g. 7:30 am is 730 and 3:13 pm is 1513
            Off_Time = 0 - 2399 #same format as On_Time
            Timer_Type = 1-3 #use an integer of the type 1, 2, or 3
            #1 = timer using the time only
            #2 = timer using ip address only
            #3 = timer using time, but if it's within the time specified, then it will also check if the ip address is available.
    Save the config file with ctrl+x.
    Add the script start.py to your bashrc file.
    To do this do the following:
        $sudo nano ~/.bashrc
        #Paste the following at the bottom of the file:
        python3 ~/Monitor_Timer/start.py
        save the config file with ctrl+x.
    Try to install the tapo adapters module:
        >pip install tapo
if you get an error during tapo installation then follow the instructions below. otherwise skip to the last part.

You may also need to install a venv. If you run 'pip install tapo' and get an error you'll need to follow instructions below.
What you will do here is make a 'virtual environment' (venv) for the module to run in. Then when you start the module it can run.
You can install whatever python programs you want in venv that aren't supported by your sysem because it won't break them.
To do this do the following:
        $cd ~/Monitor_Timer
        $python3 venv .venv
        $source .venv/bin/activate
        $pip install -r requirements.txt
        instead of calling python3 in your .bashrc file as described above change it to:
                ~/Monitor_Timer/.venv/bin/python3 ~/Monitor_Timer/start.py
                this will let the script run independent of the python install in the system.

Now you can test the program with it setup:
        test the program runs and get some ouput by typing:
                $python3 start.py
                $You should see some ouput. if you configured the settings.py properly. Using any value for ip_address_list will suffice for testing.
        sudo reboot and the timer should start automatically.
