import pyttsx3
import speech_recognition

from Edith import speak

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",180-200)
speak("hello shahnawaz sir, how are you")