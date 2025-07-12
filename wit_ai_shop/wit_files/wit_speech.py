import whisper
from wit_files.Recorder import record_audio

def RecognizeSpeech(AUDIO_FILENAME, num_seconds=5):
    print("🎤 Recording audio...")
    record_audio(num_seconds, AUDIO_FILENAME)

    print("📥 Loading Whisper model...")
    model = whisper.load_model("base")  # use "tiny" for fastest, "small"/"medium"/"large" for more accuracy

    print("🧠 Transcribing audio...")
    result = model.transcribe(AUDIO_FILENAME)

    text = result['text'].strip()
    return text if text else "⚠️ No speech recognized."

if __name__ == "__main__":
    text = RecognizeSpeech("myspeech.wav", 4)
    print("\n✅ You said:", text)
