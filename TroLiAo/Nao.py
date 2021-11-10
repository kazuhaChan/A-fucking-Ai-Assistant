import wikipedia
from playsound import playsound
def wiki(keyword):
    try:
        print('**Result from wiki**')
        print(wikipedia.summary(keyword))       # search wiki
    except:
        print('Some error occurred! Try again.')
        print('')
def ef():
    playsound("C:\TLA\stef_01.mp3")

def alarm():
    playsound("C:\TLA\alarm.mp3")