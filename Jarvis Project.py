# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:09:49 2020

@author: Admin
"""
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

import datetime
import wikipedia#pip install wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<8:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, Please tell how may I help you")
    
def takeCommand():
    #it takes microphone input from user and gives string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold =1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
     
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('competitive.corner2020@gmail.com','')
    server.sendMail('competitive.corner2020@gmail.com',to, content)
    server.close()
    
    
        
if __name__=="__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
        if 'wikipedia'in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Google' in query:
            webbrowser.open("facebook.com")
        elif 'open Stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir,the time is {strTime}")
            speak(f"Sir,the time is {strTime}")
        elif 'message to patil' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="vv@hs.iitr.ac.in"
                sendMail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry vikas bro i am not able to send mail")
                
            
            
            