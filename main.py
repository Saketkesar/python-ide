import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import os


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("Welcome back sir!")
    
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")

    speak("Jarvis at your service. Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query 



if __name__ == "__main__":
    wishme()
	
while True:
		query = takeCommand().lower()
		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'wikipedia' in query:
			speak("Searching...")
			query = query.replace("wikipedia","")
			result = wikipedia.summary(query, sentences=2)
			print(result)
			speak(result)
if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "Wake up Jarvis" in permission:
            Taskexecution()
        elif "good bye sir" in permission:
              sys.exit()
              
                
            
		
		
			

		




    



