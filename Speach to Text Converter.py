import speech_recognition as sr
AUDIO_FILE=('A.wav') # the name of the audio file. The extension of the file must always be WAV 

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    
try:
    print("audio file contains: " + r.recognize_google(audio))

except sr.UnknownValueError :
    print("Google Speech Recognition could not Understand audio")

except sr.RequestError :
    print("Could't get the result")
    
