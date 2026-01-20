from flask import Flask, jsonify
import speech_recognition as sr

app = Flask(__name__)
recognizer = sr.Recognizer()

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI & ML Voice to Text</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 100px; }
            button { padding: 15px 30px; font-size: 18px; cursor: pointer; }
            p { font-size: 20px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h2>🎤 AI & Machine Learning Voice to Text</h2>
        <button onclick="start()">Start Speaking</button>
        <p id="output"></p>

        <script>
            function start() {
                document.getElementById("output").innerText = "Listening...";
                fetch("/voice", { method: "POST" })
                .then(res => res.json())
                .then(data => {
                    document.getElementById("output").innerText = data.text;
                });
            }
        </script>
    </body>
    </html>
    """

@app.route("/voice", methods=["POST"])
def voice_to_text():
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            return jsonify({"text": text})

        except sr.UnknownValueError:
            return jsonify({"text": "❌ Could not understand the audio"})

        except sr.RequestError:
            return jsonify({"text": "❌ Speech recognition service error"})

if __name__ == "__main__":
    app.run(debug=True)
