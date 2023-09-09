import speech_recognition as speechRecognition
import pyttsx3
import pywhatkit 
import datetime
import wikipedia

listener = speechRecognition.Recognizer()


machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with speechRecognition.Microphone() as origin:
            talk("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction=instruction.lower()
            if "Sam" in instruction:
                instruction = instruction.replace('sam','')
                print(instruction)
    except:
        pass
    return instruction

def play_sam():
    global instruction
    instruction=''
    while(instruction != 'quit'):
        instruction = input_instruction()
        print(instruction)
        if "play" in instruction:
            song = instruction.replace('play','')
            print('Playing' + song)
            talk("playing" + song)
            pywhatkit.playonyt(song)
            
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            talk('Current time '+ time)
            
        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d /%m /%Y')
            print(date)
            talk("Today's date is " + date)
            
        elif 'who is' in instruction:
            human = instruction.replace('who is','')
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
            
        elif 'quit' in instruction:
            talk('Goodbye')
            break
                
        else:
            talk("Please repeat")
    
play_sam()