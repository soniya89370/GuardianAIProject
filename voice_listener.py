# import whisper
# import sounddevice as sd
# import soundfile as sf
# import os

# model = whisper.load_model("base")

# SECRET_CODE = "help me"

# def listen_secret_code():

#     duration = 5
#     samplerate = 16000

#     print("🎤 Speak your secret code...")

#     audio = sd.rec(
#         int(duration * samplerate),
#         samplerate=samplerate,
#         channels=1,
#         dtype="float32"
#     )

#     sd.wait()

#     audio_file = "secret.wav"
#     sf.write(audio_file, audio, samplerate)

#     try:
#         result = model.transcribe(audio_file)
#         text = result["text"].strip().lower()

#         print("You Said:", text)

#         if SECRET_CODE in text:
#             print("🚨 EMERGENCY ACTIVATED 🚨")
#             return True
#         else:
#             return False

#     except Exception as e:
#         print(e)
#         return False

#     finally:
#         if os.path.exists(audio_file):
#             os.remove(audio_file)


import os

try:
    import whisper
    model = whisper.load_model("base")
except Exception as e:
    model = None
    print("Whisper loading error:", e)


try:
    import sounddevice as sd
    import soundfile as sf
    AUDIO_AVAILABLE = True
except Exception as e:
    sd = None
    sf = None
    AUDIO_AVAILABLE = False
    print("Audio unavailable:", e)


SECRET_CODE = "help me"


def listen_secret_code():

    # Render/cloud server does not support microphone
    if not AUDIO_AVAILABLE:
        print("⚠️ Voice input is not available on server")
        return False


    duration = 5
    samplerate = 16000

    audio_file = "secret.wav"

    try:
        print("🎤 Speak your secret code...")

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(
            audio_file,
            audio,
            samplerate
        )


        if model is None:
            print("Whisper model not loaded")
            return False


        result = model.transcribe(audio_file)

        text = result["text"].strip().lower()

        print("You Said:", text)


        if SECRET_CODE in text:
            print("🚨 EMERGENCY ACTIVATED 🚨")
            return True
        else:
            return False


    except Exception as e:
        print("Voice error:", e)
        return False


    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)