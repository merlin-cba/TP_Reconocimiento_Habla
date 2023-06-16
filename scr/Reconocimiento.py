import speech_recognition as sr

def transcribe_speech(audio_file):
    # Crear un reconocedor de voz
    r = sr.Recognizer()

    # Abrir el archivo de audio
    with sr.AudioFile(audio_file) as source:
        # Cargar el audio en el reconocedor
        audio = r.record(source)

    try:
        # Utilizar el reconocedor para transcribir el audio
        text = r.recognize_google(audio, language='es') # Puedes ajustar el idioma según tus necesidades
        return text
    except sr.UnknownValueError:
        print("No se pudo transcribir el audio")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz; {e}")

# Ruta al archivo de audio que deseas transcribir
audio_file_path = "ruta/al/archivo.wav"

# Transcribir el audio y obtener el texto resultante
transcription = transcribe_speech(audio_file_path)

# Imprimir la transcripción
print("Transcripción:", transcription)
