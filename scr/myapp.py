from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3

app = Flask(myApp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Obtener la consulta del cliente
    query = request.form.get("query")

    # Realizar el reconocimiento de voz en la consulta
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        # Realizar la transcripción del habla a texto
        recognized_text = recognizer.recognize_google(audio, language="es")
        print("Texto reconocido:", recognized_text)
    except sr.UnknownValueError:
        recognized_text = "No se pudo reconocer el habla"
    except sr.RequestError as e:
        recognized_text = f"Error en la solicitud de reconocimiento de voz; {e}"

    # Realizar el procesamiento de la consulta y generar una respuesta
    # Aquí puedes incluir el código para realizar análisis de texto, generar respuesta, etc.

    # Sintetizar la respuesta en voz
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Ajustar la velocidad de habla según sea necesario
    engine.say(response)
    engine.runAndWait()

    return render_template("index.html", query=query, recognized_text=recognized_text, response=response)

if __name__ == "__main__":
    app.run(debug=True)
