#tapo_timer.py
import asyncio
from time import sleep
from settings import Tapo_Username, Tapo_Password, Tapo_ip_Address
from scriptpaths import READWRITEPATHS
from tapo import ApiClient
from icecream import ic

#Easy access definitions from functions/variables that were imported:
READWRITEPATHS = READWRITEPATHS()
READSTATE = READWRITEPATHS.READSTATE #requires strSTATE (as tstate or ipstate)
WRITESTATE = READWRITEPATHS.WRITESTATE #strSTATE and STATE (as a 0 or 1)

async def plug_on():
    client = ApiClient(Tapo_Username, Tapo_Password)
    device = await client.generic_device(Tapo_ip_Address)
    await device.on()

async def plug_off():
    client = ApiClient(Tapo_Username, Tapo_Password)
    device = await client.generic_device(Tapo_ip_Address)
    await device.off()

def activate_plug(Timer_Type):
    #uses the timer_type variable in settings.py to set the strSTATE as either tstate or ipstate for the plug on/off
    #if we use tstate then tstate controls the plug.
    #if we use ipstate then ipstate controls the plug.
    if int(Timer_Type) == 1:
        if int(READSTATE(strSTATE = "tstate")) == 1:
            asyncio.run(plug_on())
            print("Plug turned on.")
        else:
            asyncio.run(plug_off())
            print("Plug turned off.")
    elif int(Timer_Type) == 2:
        if int(READSTATE(strSTATE = "ipstate")) == 1:
            asyncio.run(plug_on())
            print("Plug turned on.")
        else:
            asyncio.run(plug_off())
            print("Plug turned off.")
    elif int(Timer_Type) == 3:
        if int(READSTATE(strSTATE = "tstate")) == 1:
            if int(READSTATE(strSTATE = "ipstate")) == 1:
                asyncio.run(plug_on())
                print("Plug turned on.")
            else:
                asyncio.run(plug_off())
                print("Plug turned off.")
        else:
            if int(READSTATE(strSTATE = "tstate")) == 1:
                ic(asyncio.run(plug_on()))
                print("Plug turned on.")
            else:
                asyncio.run(plug_off())
                print("Plug turned off.")
    else:
        pass


if __name__ == "__main__":
    activate_plug()
