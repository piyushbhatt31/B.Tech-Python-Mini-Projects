import pyttsx3
import speech_recognition as sr
def take_commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=0.7
        audio=r.listen(source)
    try:
        print("Recognizing")
        Query=r.recognize_google(audio, language='en-in')
        print("the query is printed=",Query,"'")
    except Exception as e:
        print(e)
        print("say it again sir")
        return "None"
    return Query
def Speak (audio):
        engine=pyttsx3.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(audio)
        engine.runAndWait()
if __name__ == '__main__':
    while True:
        command=take_commands()
        if 'exit' in command:
            pyttsx3.speak("Sure Sir as you wish Bye Hope I helped you")
            print("Sure Sir as you wish Bye Hope I helped you")
            break
        if 'hello' in command:
            pyttsx3.speak("Hi")
            break
        if 'how are you' in command:
            pyttsx3.speak("I am fine what about you")
            break
        if 'like' in command :
            pyttsx3.speak("Thank you")
