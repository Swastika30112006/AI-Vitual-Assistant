
import os
from playsound import playsound
import datetime



extracted_time = open('data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time=open('data.txt','r+')
delete_time.truncate(0)
delete_time.close()

def RingerNow(time):

    time_to_set=str(time)
    time_now=time_to_set.replace("lucifer","")
    time_now=time_now.replace("set alaram for","")
    time_now=time_now.replace("set","")
    time_now=time_now.replace(" and ",":")

    Alaram_Time=str(time_now)

    while True:

        current_time = datetime.datetime.now().strftime("%/H:%M")

        if current_time==Alaram_Time:
            print("wake up sir, its time to work.")
            os.startfile("cheap thrills.mp3")

        elif current_time>Alaram_Time:
            break

RingerNow(Time)