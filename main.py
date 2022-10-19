import pyttsx3 as p
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser as wb

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 5000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)
    except Exception as e:
        print(e)
        print("Please, say that again")
        return "None"

    return query

def speak(audio):
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + " Hours and " + min + "Minutes")

def hello():
    speak("Hello, I am you desktop assistant")

def intro_self():
    speak("I am Jarvis, your digital assistant at your service")

def tell_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: "Monday", 2: "Tuesday",
        3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday",
        7: "Sunday"
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def give_info():
    speak("What information do you want?")
    query = take_command().lower()

    try:
        result = wiki.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(result)
        speak(result)
    except Exception as e:
        print(e)
        print("Sorry, error found reading the topic.")

def take_query():
    hello()
    while(True):
        query = take_command().lower()

        if "day" and "today" in query:
            tell_day()
            continue
        elif "time" and "now" in query:
            tell_time()
            continue
        elif "open google" in query:
            speak("Opening google")
            wb.open("www.google.com")
            speak("Is there anything you want?")
            continue
        elif "your name" and "who are you" in query:
            intro_self()
            continue
        elif "stop" and "exit" and "nothing" in query:
            speak("Thank you and have a nice day.")
            exit()
        elif "information" in query:
            query = query.replace("information", "")
            give_info()
            speak("Is there anything you want?")
            continue
        else:
            speak("Sorry, that's an unrecognized command")
            continue

if __name__ == "__main__":
    query = ""
    take_query()