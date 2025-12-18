import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("audio/sample.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text:")
    print(text)

    with open("text/output.txt", "w", encoding="utf-8") as f:
        f.write(text)

except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError:
    print("ASR service error")
