

from asyncio import sleep
from encodings import search_function
from pickletools import TAKEN_FROM_ARGUMENT4U
from re import search
from openai import OpenAI
import sys
import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import time
import pyjokes
import psutil
import instaloader 
import pyautogui
from pywikihow import search_wikihow
##from PyDictionary import PyDictionary as Diction
import keyboard
from ollama_ai import ask_ai


engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",180-200)

def speak(audio):
   engine.say(audio)                                                        
   engine.runAndWait()


def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=5 and hour<12:
      speak("Good Morning!, sir")  

   elif hour>=12 and hour<16:
         speak("Good Afternoon!, sir")

   elif hour>=16 and hour<24:
         speak ("Good Evening!, sir")
   else:
         speak("wow! i cant belive you are still active at midnight")

   speak("I am your personal assistant . Please tell me how can i help you")

def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"User said: {query}\n")

   except:
      # print(e)
      print("Say that again please...")
      return "None"
   return query


def TaskExecution():
   speak("Hello Sir, welcome back")
   wishMe()
   while True:
      query=takeCommand().lower()

      
      if'search google' in query or 'google search' in query or 'google' in query:
         text = query.replace("search google for","")
         text= text.replace("can you google search for","")
         webbrowser.open("https://www.google.com/search?q=" +text) 
         speak('here are your results sir')
         speak(text)
      
   

      elif'search for' in query or 'search in youtube' in query:
         youtube = query.replace("search in youtube for","")
         youtube = query.replace("search for","")
         speak("searching for"+youtube)
         webbrowser.open("https://www.youtube.com/search?q=" +youtube)
         speak("here are your results sir")
         speak('you would also like this')
         pywhatkit.playonyt(youtube)

      elif'play' in query:
          Play = query.replace("play","")
          speak("playing"+Play)
          pywhatkit.playonyt(Play)

         
      
      elif 'wikipedia' in query or 'who is' in query:
         speak("searching wikepedia...")
         query=query.replace("wekipedia", "")
         result=wikipedia.summary(query, sentences=2)
         speak("according to wikipedia")
         print(result)  
         speak(result)

      elif'open youtube' in query:
         speak("opening youtube, please wait")
         webbrowser.open("youtube.com")

      elif 'open instagram' in query:
         speak("opening instagram, please wait")
         webbrowser.open("instagram.com")

      elif'close youtube' in query:
         os.system("TASKKILL /F /im Chrome.exe")

      elif'close chrome' in query:
         os.system("TASKKILL /f /im Chrome.exe")

      elif'close instagram' in query:
         os.system("TASKKILL /f /im chrome.exe")

      elif'thank you' in query:
         speak("you are welcome sir")


      elif'who are you' in query:
         speak("hello i am an ai intelligent , my work is to make things easy for you")

      elif'you need a break' in query or 'go to sleep' in query or 'sleep' in query:
         speak("Okay sir, going to sleep mode. Just give the command wake up and I will be back at your service")
         break

      elif'what is up' in query:
         speak("Always at your service")

      elif'joke' in query:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())

   

      elif'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}") 

      elif 'temperature' in query:
         speak("Tell me the name of the place")
         name = takeCommand()

         url = f"https://wttr.in/{name}?format=%t"
         temp = requests.get(url).text

         speak(f"The temperature in {name} is {temp}")

 
   
      elif'are you up' in query:
         speak('for you,always sir')

      elif'hello ' in query:
         speak("hello sir , may i help you with something")

      elif'how are you' in query:
         speak("i am fine sir,what about you")

      elif'i am fine' in query or 'i am also good' in query or 'i am good' in query or 'i am also fine' in query:
         speak('thats great to hear from you')


      elif'how much power left' in query or 'how much power we have' in query or 'batter' in query or 'power' in query:

         battery=psutil.sensors_battery()
         percent = battery.percent
         speak(f'sir we have {percent} percent left')
         if percent>=75:
            speak("we have enough power to continue our work")
            print("We have enough power to continue our work")
         elif percent>=40 and percent<75:
            speak("we should connect our system to charging point to charge our battery")
            print("we should connect our system to charging point to charge our battery")
         elif percent>=15 and percent<40:
            speak("we dont have enough power to work,please connect to charging")
            print("we dont have enough power to work,please connect to charging")
         elif percent<15:
            speak("we have very low power,please connect to charging the system will shut down soon")
            print("we have very low power,please connect to charging the system will shut down soon")

      
         

      elif'instagram profile' in query or 'profile on instagram' in query:
         speak("sir please enter the username you want to search")
         name = input("enter the username : ")
         webbrowser.open("https://www.instagram.com//{name}/")
         speak(f"sir here is the profile of user {name}")
         time.sleep(5)
         speak("sir would you like to download profile pic of the this account")
         condition = takeCommand().lower()
         if 'yes' in condition:
            mod = instaloader.Instaloader()
            mod.download_profile(name, profile_pic_only=True)
            speak("i am done sir,profile is saved in our main folder.now i am ready for next command")
         else:
            speak("What can i do more for you sir")

      elif'take a screenshot' in query or 'screenshot' in query:
         speak("sir please tell me a name forthis screenshot file")
         name = takeCommand().lower()
         speak("please sir hold the screen for few seconds, i am taking a screenshot")
         time.sleep(3)
         img = pyautogui.screenshot()
         img.save(f'{name}.png')
         speak("i am done sir,the screenshot is saved in our main folder, now i am ready for next command")

      elif'activate how to do mode' in query:
         speak("How to do mode is activated,please tell me what you want to know")
         
         question = takeCommand()
         answer = ask_ai(question)

         print(answer)
         speak(answer)

         speak("how can i help you more, sir")

      elif'whatsapp message' in query:
         speak("whom do you want to message sir")
         time.sleep(3)
         name= query.replace("send whatsapp","")
         name= name.replace("send","")
         name= name.replace("to","")
         name= name.replace("please message her that","")
         name= name.replace("please message him that","")
         name= name.replace("please message them that","")
         Name= takeCommand()
         speak("whats the message for " +Name)
         MSG = takeCommand()
         from whatsapp import whatsappMsg
         whatsappMsg(Name,MSG)
         speak("Done sir message has been sent succesfully")

      elif'voice call' in query:
         from whatsapp import whatsappCall
         name= query.replace("call","")
         name= name.replace("lucifer","")
         name= name.replace("please","")
         Call= str(name)
         whatsappCall(Call)

      elif'show chat' in query or 'open chat' in query:
         speak("from whom?")
         sleep(3)
         Chat= takeCommand()
         from whatsapp import whatsappChat
         whatsappChat(Chat)

      elif'video call' in query:
         speak("whom do you want to call sir")
         Nname= takeCommand()
         name= query.replace("video call","")
         name= name.replace("video","")
         name= name.replace("call","")
         speak('Making video call to {Nname}')
         sleep(5)
         from whatsapp import whatsappVideocall
         whatsappVideocall(Nname)

      elif'voice chat' in query:
         speak('whom do you want to send chat sir' )
         VName= takeCommand()
         name= query.replace("voice","")
         name= name.replace("send a chat to","")
         speak('sending a voice chat to {VName}')
         from whatsapp import whatsappVoicemess
         whatsappVoicemess(VName)

      elif'code' in query or 'visual studio' in query:
         os.startfile("C:\\Users\\shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

      elif'chrome' in query:
         os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

   
      elif'meaning' in query:
         speak('sir please spell the word of which meaning do you want.')
         dict= takeCommand()
         dict= query.replace("what is the","")
         dict= dict.replace("lucifer","")
         dict= dict.replace("of","")
         dict= dict.replace("meaning of","")
        ## result= Diction.meaning(dict)
         speak(f'The meaning for {dict} is {result}')
         print(result)

      elif'pause' in query or 'play' in query:
         keyboard.press('space bar')

      elif'restart' in query:
         keyboard.press('0')

      elif'mute' in query:
         keyboard.press('m')

      elif'unmute' in query:
         keyboard.press('m')

      elif'skip' in query:
         keyboard.press('l')

      elif'back' in query:
         keyboard.press('j')

      elif'full screen' in query:
         keyboard.press('f')

      elif'exit full sreen' in query:
         keyboard.press('f')
 
      elif'film mode' in query:
         keyboard.press('t')
      
      
   


      


      
         
        


         
if __name__=="__main__":
   while True:
      permission=takeCommand()
      if'wake up' in permission:
        TaskExecution()
      elif'please shut down' in permission or 'shutdown' in permission:
         speak("thanks for using me sir have a good day")
         speak("shutting down the system sir, hope you enjoyed it")
         sys.exit()


        
         

      

      
     
      
      


      
      
      

      
