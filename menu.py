import time
import subprocess
import os
import uuid
import pyttsx3
# connecting to sound driver by creating an object


while True :
    user_input='''
    Press 1 to Check current time and Date :- 
    Press 2 to Check RAM Size of Your current OS  :- 
    Press 3 to KNow Name of YOur current OS :- 
    Press 4 to Check What is Mac address lapTOP/PC/VM/CLoudVM :- 
    Press 5 to create one directory IN your Desktop :- 
    Press 6 to Restart Your current OS :- 
    Press 7 to Print list of all available Wifi in your laptop Range :-
    Press 8 to Run another code in your current folder :-  
    Press 9 to exit:-

    '''
    myaudio=pyttsx3.init()
   # storing data in a buffer 
    myaudio.say(user_input)


    myaudio.runAndWait()
    print(user_input)
    # to accept input from user 
    user_choice=input()
    # printing user input 
    #print("user has entered ",user_choice)

    if  user_choice ==  '1' :
        mytime=time.ctime()
        print("current date and time IS ",mytime)
        
    elif  user_choice  ==  '2' :
        RAM_Size=subprocess.getoutput("wmic MemoryChip get capacity")
        print(" RAM Size of Your current OS ",RAM_Size)
    
    elif  user_choice  ==  '3' :
        os_info = subprocess.getoutput("hostname")
        print("Name of Your current OS",os_info) 

    elif  user_choice  ==  '4' :
        print(os.system("getmac"))

    elif  user_choice  ==  '5' :
        path = "helloworld.py"
        print(os.mkdir(path))

    elif user_choice  ==  '6' :
        restart = input()
        print(os.system("Shutdown/r /t  1"))

    elif user_choice  ==  '7' :
        print(os.system("netsh wlan show profiles"))

    elif  user_choice  ==  '8' :
        # calling another code
        os.system("python hello.py")

    elif  user_choice  ==  '9' :
        break
    





