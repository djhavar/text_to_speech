from tkinter import*
import speed_recognition as sr
import webbrowser
import pyttsx3
from datetime import datwtime
import subprocess

root =Tk() 
root.geometry("500x500")
root.configure(bg="Light Blue")

label=Label(root,text="Welcome To Your Personal Desktop Assistant",
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("How can i help you..")
    with sr.Microphone() as source:
        audio= speech recognizer.listen(source)
        voice_data=''
        
    try:
        voice_data = speech_recognisor.recognize_google(audio,)
    except sr.UnknownValueError:
        print('PLease repeat i did not get that')
        print('PLease repeat i did not get that')
        r_audio()
        respond(voice_data)
        
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("my name is jarvis")
        print("my name is jarvis")
        
    if "time" in voice_data:
        speak("Current time is")
        now = datetime.now()
        current_time=n.strftime("%H:%M:%S")
        speak("current_time")
        print("current_time")
        
        
    if "search" in voice_data:
            speak("opening_google")
            print("opening_google")
            webbrowser.get().open("https://www.google.com/")
            
    if "videos" in voice_data:
        speak("opening_youtube")
        print("opening_youtube")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "text editor" in voice_data:
            speak("opening_notpad")
            print("opening_notpad")
          subprocess.Popen("notpad.exe")
    
btn= Button(command=r_audio,bg="red3",fg="white,padx=10,pady=1",font=("Arial",11,"bold"))
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()




