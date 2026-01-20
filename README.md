# 🎤 Voice to Text Conversion using Python & Machine Learning

This project converts **human voice into text** using **Python libraries** and **Machine Learning / Deep Learning models**.  
It supports **real-time microphone input** and demonstrates how AI understands spoken language.

---

## 🚀 Features
- 🎙️ Real-time speech recognition
- 🧠 Machine Learning based conversion
- 🌐 Online & Offline support
- 🐍 Simple Python implementation
- 🎓 Beginner-friendly project

---

## 🛠️ Technologies Used
- Python 3.x  
- SpeechRecognition  
- PyAudio  
- Vosk (Offline ML Model)  
- Whisper (Deep Learning – optional)

---

## 📦 Installation

```bash
pip install SpeechRecognition pyaudio vosk
If PyAudio fails on Windows:

bash
Copy code
pip install pipwin
pipwin install pyaudio
🎙️ How It Works
Captures audio from microphone

Preprocesses voice signal

ML model converts speech → text

Displays recognized text

🧪 Sample Code
python
Copy code
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

try:
    print("You said:", r.recognize_google(audio))
except:
    print("Could not recognize")
📊 Output Example
css
Copy code
Speak now...
You said: hello how are you
📌 Use Cases
Voice Assistants

AI Chatbots

Accessibility Tools

Smart Applications

👩‍💻 Author
Tejaswini Chavan