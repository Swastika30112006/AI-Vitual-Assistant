from ipaddress import ip_address
from flask import request
import requests
import speech_recognition
import pyttsx3

from AI import speak

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",180-200)


def My_Location():

    ip_add = request.get("https://api.ipiny.org").text

    url='https://get.geogs.io/v1/ip/geo/' +ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"sir, you are in {state, country} .")

My_Location()



