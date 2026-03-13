
import os
import speech_recognition as sr


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

while True:

    wake_Up=takeCommand()

    if 'wake up' in wake_Up:
        os.startfile("D:\\Edith\\main edith")

    else:
        print('nothing...')