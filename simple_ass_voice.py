import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser
from pyttsx3 import engine

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk('Привет, скажите что-либо')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажи что-нибудь")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        tell = r.recognize_google(audio, languege='ru-RU'.lower)
        print('Вы сказали' + tell)

    except sr.UnknownValueError:
        print('Я не поняла, что вы сказали. Повторите снова')
        tell = command()

    except sr.RequestError:
        print('Я не распознала ваш голос' + r.recognize_google(audio))
        tell = command()
    
    return tell

def makeCommand(tell):
    if 'открой сайт' in tell:
        talk('Уже отклываю')
        url ='https://vk.com/id485891682'
        webbrowser.open(url)
    elif 'как тебя зовут' in tell:
        print('Меня зовут Помогатель')
    elif 'стоп' in tell:
        print('Конечно, без проблем')

while True:
    makeCommand(command())





