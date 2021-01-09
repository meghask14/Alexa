import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time right now is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'sad' in command:
        talk('Everything will be fine')
    elif 'bored' in command:
        talk('You can ask me to say some Jokes, Sir')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am very happy and glad to help you')
    elif 'happy' in command:
        talk('I am happy because you are happy')
    elif 'funny' in command:
        talk('Oh nice, may i tell you another joke?')
    elif 'who are you' in command:
        talk('I am Jarvis your personal assistant and always at you service')
    elif 'who is your developer' in command:
        talk('Mehul Totala made me and gave me this life. I am thankful to him for making me.')
    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)
    elif 'message' in command:
        talk('please type the message')
        number = input('Number: ')
        message = input('message: ')
        hrs = int(input('Hours: '))
        min = int(input('Min: '))
        pywhatkit.sendwhatmsg(number, message, hrs, min)
    elif 'shutdown' in command:
        talk('OK, Closing pc down in 50 seconds')
        pywhatkit.shutdown(50)
    elif 'cancel' in command:
        talk('OK')
        pywhatkit.cancelShutdown()
    else:
        talk('Please ask Mehul to add answer to your command')


while True:
    run_alexa()


