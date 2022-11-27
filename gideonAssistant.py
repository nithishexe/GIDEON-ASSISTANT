import speech_recognition as sr
import requests, json
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from gtts import gTTS
import os
from playsound import playsound
from datetime import datetime
import pyjokes
import randfacts
from selenium.common.exceptions import NoSuchElementException
from random import randint
import time

file='todo.txt'
def speak(s):
    language='en'
    myobj = gTTS(text=s,lang=language,slow=False)
    myobj.save("temp.mp3")
    playsound('temp.mp3')
    os.remove("temp.mp3")

def listen():
    while(1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Give me a Command!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            sp=r.recognize_google(audio)
            break
        except sr.UnknownValueError:
            speak("Gideon could not understand audio, Please speak again")
            continue
        except sr.RequestError as e:
            print("Gideon error; {0}".format(e))
            continue
    return sp

def weather():
    str1="which city?"
    speak(str1)
    city=listen()
    url='https://www.google.com/search?q=weather+'+str(city)+''
    op=webdriver.ChromeOptions();
    op.add_argument('headless');
    driver=webdriver.Chrome("D:\Coding\coolProjects\chromedriver.exe", options=op)
    driver.get(url)
    w=driver.find_element("xpath",'//*[@id="wob_tm"]').text
    w+="°C"
    f="weather in "+str(city)+" is "+str(w)
    speak(f)

def telltime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(current_time)

def joke():
    My_joke = pyjokes.get_joke(language="en", category="all")
    speak(My_joke)

def boring():
    a="Haha! I'm sorry to dissapoint you but this is the best I can do"
    speak(a)
 
def facts():
    x=randfacts.get_fact()
    speak(x)

def question(q):
    print(q)
    op=webdriver.ChromeOptions()
    op.add_argument('headless')
    driver=webdriver.Chrome("D:\Coding\coolProjects\chromedriver.exe", options=op)
    url='https://www.google.com/search?q='+str(q)
    driver.get(url)
    driver.implicitly_wait(10)
    if("who" in q):
        try:
            a=driver.find_element_by_class_name('hgKElc').text
            speak(a)
        except NoSuchElementException:
            try:
                a=driver.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
                speak(a)
            except NoSuchElementException:
                a="sorry I do not know that" 
                speak(a)
        driver.close()   
    elif("what" in q):
        try:
            a=driver.find_element_by_class_name('Z0LcW').text  
            speak(a)
        except NoSuchElementException:
            try:
                a=driver.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
                speak(a)
            except NoSuchElementException:
                a="sorry I do not know that"
                speak(a)
        driver.close()
    elif("when" in q):   
        try:
            a=driver.find_element_by_class_name('zCubwf').text  
            speak(a)
        except NoSuchElementException:
            try:
                a=driver.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
                speak(a)
            except NoSuchElementException:
                a="sorry I do not know that"
                speak(a)
        driver.close()
    elif("where" in q):   
        try:
            a=driver.find_element_by_class_name('sXLaOe').text  
            speak(a)
        except NoSuchElementException:
            try:
                a=driver.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
                speak(a)
            except NoSuchElementException:
                a="sorry I do not know that"
                speak(a)
            driver.close()
    else:
        try:
            a=driver.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
            speak(a)
        except NoSuchElementException:
            a="sorry I do not know that"
            speak(a)
        driver.close()
def news():
    op=webdriver.ChromeOptions()
    op.add_argument('headless')
    driver=webdriver.Chrome("D:\Coding\coolProjects\chromedriver.exe", options=op)
    url='https://indianexpress.com/latest-news/'
    driver.get(url)
    driver.implicitly_wait(10)
    for i in range(1,5):
        n=driver.find_element("xpath",'//*[@id="section"]/div/div/div[1]/div[2]/div['+str(i)+']/div[3]').text
        speak(n)
def toss():
    p=randint(-10,10)
    if p>0:
        speak("You got heads")
    else:
        ("You got tails")
def covid():
    op=webdriver.ChromeOptions()
    op.add_argument('headless')
    driver=webdriver.Chrome("D:\Coding\coolProjects\chromedriver.exe", options=op)
    url='https://www.google.com/search?q=covid+india'
    driver.get(url)
    tot_cases=driver.find_element("xpath",'//*[@id="kEEOx"]/div[2]/div[1]/div/div[1]/table/tbody/tr/td[1]/div[2]/div[1]/span').text
    tot_deaths=driver.find_element("xpath",'//*[@id="kEEOx"]/div[2]/div[1]/div/div[1]/table/tbody/tr/td[2]/div[2]/div[1]/span').text
    a="As of today there are "+tot_cases+" total cases and "+tot_deaths+" total deaths in India."
    speak(a)
def createList():
    speak("what tasks do you want to add")
    f = open(file,"w")
    a=listen()
    f.write(a)
    f.close()
def toDoList():
    if os.path.isfile(file) == False:
        createList()
    f = open(file,"r")
    x = f.read()
    f.close()
    speak(x)
def showtoDoList():
    if os.path.isfile(file)==False:
        speak("It looks like that list is empty")
    else:
        f=open(file,"r")
        speakList=f.read()
    speak(speakList)

f=1
while(1):
    if(f==1):
        time.sleep(5)
        speak("Hey whats up!, I am Gideon, A desktop assistant made by nithish")
        f=0
    a=""
    a=listen()
    if("how are you" in a):
        speak("I am fine, hoping that you are fine too mate!")
    elif("stop" in a):
        break
    elif("boring" in a):
        boring()
    elif("weather" in a):
        weather()
    elif("time" in a):
        telltime()
    elif("joke" in a):
        joke()
    elif("fact" in a):
        facts()
    elif ("news" in a):
        news()
    elif("covid" in a):
        covid()
    elif("Toss" in a):
        toss()
    elif("task" in a or "tasks" in a):
        speak("do you want to create a new task or show current ones?")
        c=listen()
        if("show" in c):
            showtoDoList()
        else:
            createList()
    else:
        question(a)