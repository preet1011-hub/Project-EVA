import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
from pyscreenshot.check import speedtest

from config import apikey
import datetime
import random
import numpy as np
import pyautogui
import cv2
# ...
def open_camera():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

    if __name__ == '__main__':
        print('Welcome Sir, I am EVA')
        say("Welcome Sir, I am EVA")
        while True:
            print("Listening...")
            query = takeCommand()
            # ...

            # Add a condition to open the camera
            if "open camera" in query.lower():
                say("Opening camera...")
                open_camera()




# todo: Add your api key here
apikey = "ENTER YOUR API KEY"
chatStr = ""

# Jokes data
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "I used to be a baker, but I couldn't make enough dough.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What's the difference between a snowman and a snowwoman? Snowballs!",
    "Why don't eggs tell jokes? Because they might crack up!",
    "Why don't scientists trust atoms? Because they make up everything!",
]


# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Preet: {query}\n EVA: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if response.choices and len(response.choices) > 0:
        reply = response.choices[0].text.strip()
        if reply:
            say(reply)
            chatStr += f"{reply}\n"
            return reply
    say("I apologize, but I couldn't generate a response.")
    chatStr += "I apologize, but I couldn't generate a response.\n"
    return ""


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][1]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)  # Adjust speech rate as desired
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from EVA"


# TElls jokes
def tell_joke():
    joke = random.choice(jokes)
    say(joke)
    return joke

def wake_up():
    print("Wake-up mode activated.")
    say("Hello! How can I assist you today?")

def  sleep_mode():
    print("Sleep mode activated.")
    say("Goodbye! Have a nice day.")
    exit()


def speak():
    pass

def open_application(app_name):
    app_list = {
        "notepad": "notepad.exe",
        "visual studio code": "Code.exe"
        # Add more applications and their corresponding executable file names
    }

    if app_name.lower() in app_list:
        os.startfile(app_list[app_name.lower()])
    else:
        print("Application not found!")


if __name__ == '__main__':
    print('Welcome Sir , I am EVA')
    say("Welcome Sir , I am EVA")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [
            ["facebook", "https://www.facebook.com"],
            ["instagram", "https://www.instagram.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["twitter", "https://twitter.com"],
            ["github", "https://github.com"],
            ["reddit", "https://www.reddit.com"],
            ["amazon", "https://www.amazon.com"],
            ["ebay", "https://www.ebay.com"],
            ["netflix", "https://www.netflix.com"],
            ["spotify", "https://www.spotify.com"],
            ["pinterest", "https://www.pinterest.com"],
            ["stackoverflow", "https://stackoverflow.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["google", "https://www.google.com"],
            ["youtube", "https://www.youtube.com"],
            ["twitch", "https://www.twitch.tv"],
            ["hulu", "https://www.hulu.com"],
            ["yahoo", "https://www.yahoo.com"],
            ["bing", "https://www.bing.com"],
            ["aliexpress", "https://www.aliexpress.com"],
            ["groupon", "https://www.groupon.com"],
            ["craigslist", "https://www.craigslist.org"],
            ["quora", "https://www.quora.com"],
            ["imdb", "https://www.imdb.com"],
            ["bbc", "https://www.bbc.co.uk"],
            ["cnn", "https://www.cnn.com"],
            ["nytimes", "https://www.nytimes.com"],
            ["walmart", "https://www.walmart.com"],
            ["target", "https://www.target.com"],
            ["bestbuy", "https://www.bestbuy.com"],
            ["apple", "https://www.apple.com"],
            ["youtube studio", "https://studio.youtube.com/channel/UCG88baEP-G1ngMOUB-0yFDA"]

        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} and {min} minutes")


            def set_alarm(time_str):
                current_time = datetime.datetime.now()
                alarm_time = datetime.datetime.strptime(time_str, "%H:%M")
                alarm_time = alarm_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)

                time_diff = alarm_time - current_time
                total_seconds = time_diff.total_seconds()

                if total_seconds <= 0:
                    print("Invalid alarm time. Please specify a future time.")
                    say("Invalid alarm time. Please specify a future time.")
                    return

                print(f"Alarm set for {time_str}.")
                say(f"Alarm set for {time_str}.")
                time.sleep(total_seconds)
                print("Alarm!")
                say("Alarm!")


            if __name__ == '__main__':
                print('Welcome Sir, I am EVA')
                say("Welcome Sir, I am EVA")
                while True:
                    print("Listening...")

                    query = takeCommand()

                    if "stop" in query:
                        say("Stopping. Listening again.")
                        continue

                    # Add a condition for waking up EVA
                    if "wake up" in query.lower():
                        wake_up()

                    # Add a condition for putting EVA to sleep
                    if "sleep mode" in query.lower():
                        sleep_mode()

                    # Add a condition to open any application
                    if "open" in query.lower() and "application" in query.lower():
                        app_name = query.lower().replace("open", "").replace("application", "").strip()
                        os.startfile(app_name)

                    # Add a condition to perform actions on the PC
                    if "do" in query.lower() and "pc" in query.lower():
                        action = query.lower().replace("do", "").replace("pc", "").strip()

                        # Add your own actions based on the voice command
                        if "shut down" in action:
                            os.system("shutdown /s /t 0")
                        elif "restart" in action:
                            os.system("shutdown /r /t 0")
                        elif "minimize window" in action:
                            os.system(
                                "osascript -e 'tell application \"System Events\" to keystroke \"m\" using command down'")
                        elif "close window" in action:
                            os.system(
                                "osascript -e 'tell application \"System Events\" to keystroke \"w\" using command down'")
                        elif "close chrome tabs" in action:
                            os.system("osascript -e 'tell application \"Google Chrome\" to close tabs of window 1'")
                        elif "open file" in action:
                            file_name = action.replace("open file", "").strip()
                            os.system(f"open {file_name}")
                        elif "access my data" in action:
                            os.system("explorer")
                        else:
                            print("Action not recognized")

                            #For opening application
                    if "open paint" in query.lower():
                        os.system("mspaint.exe")

                    if "open clock" in query.lower():
                        os.system("start ms-clock:")

                    if "open calendar" in query.lower():
                      os.system("start Calender.exe:")

                    if "open notepad" in query.lower():
                        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories.exe")
                    if "open visual studio code" in query.lower():
                        os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")






                    # Add a condition to open the camera
                    if "open camera" in query.lower():
                        say("Opening camera...")
                        open_camera()

                    # Add a condition to set up an alarm
                    if "set alarm for" in query.lower():
                        time_str = query.lower().replace("set alarm for", "").strip()
                        set_alarm(time_str)

                    # Add more conditions and actions as needed
                    # ...

                    # Add a condition to exit the program
                    if "exit" in query.lower():
                        sleep_mode()
        elif " my  setup" in query:
            obspath = (f" open C:\Program Files\obs-studio\bin\64bit.exe")

        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ", download_net)
            pyttsx3.speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")


        elif "open Notepad".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")



        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "EVA Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # say(query)
