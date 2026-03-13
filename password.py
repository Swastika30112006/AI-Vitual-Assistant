import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",180-200)


def speak(audio):
   engine.say(audio)                                                        
   engine.runAndWait()

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

def Pass(pass_imp):
    password = "jatin@1108"

    passss = str(password)

    if passss == str(pass_imp):
        speak("Access granted, thank you for logging in.")

        from AI import TaskExecution
        TaskExecution()

    else:
        speak("Access denied, please enter the correct password")

if __name__=="__main__":

    speak("This particular file is password protected.")
    speak("Kindly provide the password")
    passsss =input("Enter the password:")

    Pass(passsss)