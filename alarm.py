
import pyttsx3
import datetime
import os

engine=pyttsx3.init('sapi5')
voices  =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",200)


def speak(audio):
   engine.say(audio)                                                        
   engine.runAndWait()

extractedtime=open("data.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("data.txt","r+")
datetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("Edith","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Time to wake up,sir")
            speak("the weather outside is good,lets rise and shine")
            os.startfile("cheap thrills.mp3")

        elif currenttime>Alarmtime:
            exit()

ring(time)