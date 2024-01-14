#ScriptPaths.py
import os

#Defining any paths to folders for the module
MODULEPATH = os.path.dirname(os.path.realpath(__file__))
STATESPATH = MODULEPATH + "/states"

#Defining any paths to files for the module
tSTATEPATH = STATESPATH + "/tstate"
ipSTATEPATH = STATESPATH + "/ipstate"
ipaddressesPATH = STATESPATH + "/ip_addresses"

#functions for reading and writing files in PATHS
class READWRITEPATHS:
    def READSTATE(self, strSTATE):
        #requires the tstate or ipstate string to know which file to open in the states folder
        if strSTATE == "tstate":
            READPATH = tSTATEPATH
        else:
            READPATH = ipSTATEPATH
        with open(READPATH, 'r') as file:
            STATE = file.read()
        return STATE

    def WRITESTATE(self, strSTATE, STATE):
        #same as READSTATE but now takes an integer 'STATE' in the form of a 0 or 1
        if strSTATE == "tstate":
            WRITEPATH = tSTATEPATH
            print("writing to states file " + strSTATE)
            print("Write path is: " + str(WRITEPATH))
        else:
            WRITEPATH = ipSTATEPATH
            print("writing to states file " + strSTATE)
            print("Write path is: " + str(WRITEPATH))
        with open(WRITEPATH, 'w') as file:
            file.write(str(STATE))
