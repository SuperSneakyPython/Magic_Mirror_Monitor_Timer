#settings.py
#contains setting variables only.

#time in the format of 00:00 without leading zeros, e.g. 7:30 am is 730 and 3:13 pm is 1513
On_Time = 500 
Off_Time = 2230
Timer_Type = 3 #integer of value 1, 2, or 3. See README for details.

#write ip addresses between the [] in a list
ip_address_list = [
'ip1',
] 

Tapo = #integer 0 or 1. 1 = on, 0 = off. Other Tapo settings ignored when 0.
Tapo_Username = "" #tapo app username.
Tapo_Password = "" #tapo app password.
Tapo_ip_Address = "" #tapo plug ip address.
