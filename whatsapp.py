from os import startfile
from unicodedata import name
import pyautogui
from keyboard import press
from keyboard import write
from time import sleep

def whatsappMsg(name,message):

    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")

    sleep(30)

    pyautogui.click(x=212, y=122)

    sleep(1)

    write(name)

    sleep(7)

    pyautogui.click(x=223, y=308)

    sleep(2)

    pyautogui.click(x=576, y=730)

    sleep(2)

    write(message)

    press('enter')

def whatsappCall(name):

    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")

    sleep(30)

    pyautogui.click(x=95, y=103)

    sleep(1)

    write(name)

    sleep(7)

    pyautogui.click(x=345, y=245)

    sleep(2)

    pyautogui.click(x=1202, y=49)


def whatsappChat(name):

    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")

    sleep(30)

    pyautogui.click(x=95, y=103)

    sleep(1)

    write(name)

    sleep(7)

    pyautogui.click(x=345, y=245)

    sleep(2)

    pyautogui.click(x=515, y=602)


def whatsappVideocall(name):

    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")

    sleep(30)

    pyautogui.click(x=95, y=103)

    sleep(1)

    write(name)

    sleep(7)

    pyautogui.click(x=345, y=245)

    sleep(5)

    pyautogui.click(x=1149, y=46)

def whatsappOpen(name):

    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")
    sleep(20)
    pyautogui.click(x=95, y=103)
    sleep(1)
    write(name)
    sleep(5)
    pyautogui.click(x=345, y=245)
    sleep(3)
    pyautogui.click(x=515, y=602)

def whatsappVoicemess(name):
    startfile(r"C:\Users\jatin\OneDrive\Desktop\WhatsApp - Shortcut.lnk")
    sleep(20)
    pyautogui.click(x=95, y=103)
    sleep(1)
    write(name)
    sleep(5)
    pyautogui.click(x=345, y=245)
    sleep(3)
    pyautogui.click(x=1323, y=692)
    sleep(10)
    pyautogui.click(x=1319, y=692)

    














