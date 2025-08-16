import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.9)

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

engine.say("Hi, myself Madara Uchiha. Nice to meet u!")
engine.runAndWait()





#Speech Recognition
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#initialise the recognizer
recognizer = sr.Recognizer()


def recognise_speech():
    # use a mic as input source
    with sr.Microphone() as source:
        speak("Hello, How are u?")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("Listening")
        audio = recognizer.listen(source) #listen for the first phrase and extract the audio data

        try:
            print("recognizing")
            text = recognizer.recognize_google(audio)
            print(f"You said {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, Please Try Again!")
            return ""
        except sr.RequestError:
            print("Unable to get request.")
            return ""
        
if __name__=="__main__":
    print("Say something")
    command = recognise_speech() #call the recognise speech function
    if command: #if a command was recognised
        speak(f"You said :{command}") #convert the recognised text to speech
        