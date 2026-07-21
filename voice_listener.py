# import whisper
# import sounddevice as sd
# import soundfile as sf
# import os

# # -----------------------------
# # Secret Code
# # -----------------------------
# SECRET_CODE = "help me"

# # -----------------------------
# # Load Whisper Model
# # -----------------------------
# print("Loading Whisper Model...")
# model = whisper.load_model("base")
# print("Whisper Loaded Successfully!")

# # -----------------------------
# # Record Audio
# # -----------------------------
# duration = 5          # seconds
# samplerate = 16000

# print("\n🎤 Speak your secret code now...")

# audio = sd.rec(
#     int(duration * samplerate),
#     samplerate=samplerate,
#     channels=1,
#     dtype="float32"
# )

# sd.wait()

# audio_file = "secret.wav"
# sf.write(audio_file, audio, samplerate)

# print("Audio Recorded Successfully!")

# # -----------------------------
# # Convert Speech to Text
# # -----------------------------
# try:
#     result = model.transcribe(audio_file)

#     text = result["text"].strip().lower()

#     print("\nYou Said :", text)

#     if SECRET_CODE.lower() in text:
#         print("\n🚨 EMERGENCY ACTIVATED 🚨")
#         print("Secret Code Matched!")

#         # Yahan future me SMS / Email / SOS function call kar sakte ho

#     else:
#         print("\n❌ Secret Code Not Detected")

# except Exception as e:
#     print("\nError :", e)

# # -----------------------------
# # Delete Audio File
# # -----------------------------
# if os.path.exists(audio_file):
#     os.remove(audio_file)


import whisper
import sounddevice as sd
import soundfile as sf
import os

model = whisper.load_model("base")

SECRET_CODE = "help me"

def listen_secret_code():

    duration = 5
    samplerate = 16000

    print("🎤 Speak your secret code...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    audio_file = "secret.wav"
    sf.write(audio_file, audio, samplerate)

    try:
        result = model.transcribe(audio_file)
        text = result["text"].strip().lower()

        print("You Said:", text)

        if SECRET_CODE in text:
            print("🚨 EMERGENCY ACTIVATED 🚨")
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)