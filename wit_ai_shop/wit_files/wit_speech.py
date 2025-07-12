import speech_recognition as sr
from wit_files.Recorder import record_audio  # your existing recorder

def RecognizeSpeech(filename="myspeech.wav", duration=4):
    print("🎤 Recording...")
    record_audio(duration, filename)

    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)

    print("🧠 Transcribing with Google...")
    try:
        text = recognizer.recognize_google(audio_data)
        print("📝 Transcribed Text:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Google could not understand the audio.")
        return "❌ Could not understand audio"
    except sr.RequestError as e:
        print("❌ Could not request results; check internet.")
        return "❌ API error"

if __name__ == "__main__":
    RecognizeSpeech("myspeech.wav", 4)
