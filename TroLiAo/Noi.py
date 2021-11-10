import pyttsx3
import time
from Nao import ef
def talk(n):
    brain = pyttsx3.init()
    newVoiceRate = 200
    brain.setProperty('rate', newVoiceRate)
    brain.say(n)
    brain.runAndWait()
def wait(n):
    time.sleep(n)
    ef()
