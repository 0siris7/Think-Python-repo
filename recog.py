import speech_recognition as sr
AUDIO_FILE = 'sample.wav'
#Use audio as source

r = sr.Recognizer() #Initialize recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    #Read audio file

try:
    print(f"Audio file contains : {r.recognize_google(audio)}")

except sr.UnknownValueError:
    print("Failed")

except sr.RequestError:
    print("Google not available.")
