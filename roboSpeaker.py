# Text to Speech

import win32com.client as wincom

if __name__ == '__main__':
    
    speak = wincom.Dispatch("SAPI.SpVoice")
    
    print("***Welcome to RoboSpeaker***")
    
    while True:
        x = input("What do you want me to pronounce/speak? ")
        x = x.lower()
        if (x == "exit"):
            speak.Speak("Okay, Ta ta, Bye Bye")
            break
        speak.Speak(x)

    
    
    
