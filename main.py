import speech_recognition as sr 
import webbrowser
import pyttsx3 
import musiclibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source, timeout= 2, phrase_time_limit= 1)
            word= r.recognize_google(audio)
           # print(word)
            if(word.lower() == "jarvis"):
              speak("Ya")

            #listen for command
            with sr.Microphone() as source:
               print("Jarvis active...")
               audio = r.listen(source, timeout= 5, phrase_time_limit= 1)
            command= r.recognize_google(audio)

            processCommand(command)

        except Exception as e:
            print("Error {0}".format(e))
