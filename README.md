# 🎙️ Jisan's Personal Voice Assistant

> A simple Python-based personal voice assistant that listens to your voice, understands basic commands, responds using speech, and performs useful tasks such as opening websites, telling the time/date, and searching Google.

---

## ✨ Features

* 🎤 **Voice Recognition** — Understands commands through your microphone
* 🔊 **Voice Response** — Responds using text-to-speech
* 🕐 **Time Information** — Tells the current time
* 📅 **Date Information** — Tells today's date
* 🌐 **Open Google** — Opens Google directly
* ▶️ **Open YouTube** — Opens YouTube directly
* 🔎 **Google Search** — Searches Google using a voice command
* 👋 **Greeting Support** — Responds to "Hello"
* 🛑 **Stop Command** — Safely exits the assistant
* ⚠️ **Error Handling** — Handles unclear speech and speech-recognition errors

---

## 🛠️ Technologies Used

| Technology           | Purpose                            |
| -------------------- | ---------------------------------- |
| 🐍 Python            | Main programming language          |
| 🎤 SpeechRecognition | Converts speech into text          |
| 🔊 Pyttsx3           | Converts text into speech          |
| 🕐 Datetime          | Gets current date and time         |
| 🌐 Webbrowser        | Opens websites and Google searches |

---

## 📁 Project Structure

```text
Jisan-Voice-Assistant/
│
├── voice_assistant.py
├── README.md
└── requirements.txt
```

> You can change `voice_assistant.py` to whatever filename you use for your Python program.

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x
* Working microphone
* Internet connection
* A web browser
* Required Python libraries

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Jisan-Voice-Assistant.git
```

Move into the project folder:

```bash
cd Jisan-Voice-Assistant
```

---

### 2. Install Required Libraries

Run:

```bash
pip install SpeechRecognition pyttsx3
```

For microphone support, you may also need:

```bash
pip install PyAudio
```

---

## ▶️ How to Run

Open the project in **VS Code**.

Then open the VS Code terminal and run:

```bash
python voice_assistant.py
```

The assistant will initialize your microphone and say:

> "Hello! Welcome to Jisan's personal Voice Assistant. How can I help you today..."

Now speak a command.

---

# 🎤 Voice Commands

### 🕐 Ask for the Time

Say:

```text
What is the time
```

Example response:

```text
The time is 12:30:45 AM
```

---

### 📅 Ask for the Date

Say:

```text
What is the date
```

Example response:

```text
Today's date is 08-10-2026
```

---

### 👋 Say Hello

Say:

```text
Hello
```

The assistant will respond with a greeting.

---

### 🌐 Open Google

Say:

```text
Open Google
```

The assistant will open Google in your default browser.

---

### ▶️ Open YouTube

Say:

```text
Open YouTube
```

The assistant will open YouTube in your default browser.

---

### 🔎 Search Google

Say:

```text
Search for Python tutorials
```

The assistant will open Google and search for:

```text
Python tutorials
```

Other examples:

```text
Search for machine learning
```

```text
Search for Java tutorials
```

```text
Search for Python projects
```

---

### 🛑 Stop the Assistant

Say:

```text
Stop
```

The assistant will say goodbye and terminate the program.

---

# 🔄 How It Works

The basic workflow of the assistant is:

```text
        🎤 Microphone
             │
             ▼
     Speech Recognition
             │
             ▼
      Convert Speech
        → Text
             │
             ▼
       Check Command
             │
      ┌──────┼─────────┐
      ▼      ▼         ▼
     Time   Date    Web Search
      │      │         │
      └──────┼─────────┘
             ▼
       Generate Response
             │
             ▼
       Text-to-Speech
             │
             ▼
          🔊 Voice
```

---

# 🧠 Main Python Concepts Used

This project demonstrates several Python concepts:

* Variables
* Functions
* `if / elif / else`
* `while` loops
* `try / except`
* String methods
* String formatting
* External libraries
* Microphone input
* Text-to-speech
* Web browser automation
* Date and time handling

---

# 📌 Main Code Components

### Initialize Speech Recognizer

```python
recognizer = speech_recognition.Recognizer()
```

Creates the object responsible for processing speech.

### Capture Microphone Input

```python
with speech_recognition.Microphone() as mic:
```

Accesses the microphone.

### Convert Speech to Text

```python
audio = recognizer.listen(mic, timeout=15)
text = recognizer.recognize_google(audio)
```

Captures the voice and converts it into text.

### Text-to-Speech

```python
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
```

Converts the assistant's response into spoken audio.

### Open a Website

```python
webbrowser.open("https://www.google.com")
```

Opens the specified website in the default browser.

---

# 🚧 Current Limitations

* Requires an internet connection for Google Speech Recognition.
* Commands need to be spoken in a recognizable way.
* It currently supports predefined commands.
* It does not yet have a conversational AI model.
* It does not maintain conversation history.
* It cannot perform complex tasks.

---

# 📸 Project Demo

> Add screenshots or a demo GIF here after uploading them to your repository.

Example:

```markdown
![Voice Assistant Demo](images/demo.png)
```

You can also add a demonstration video:

```markdown
## 🎥 Demo

[Watch the Project Demo](YOUR_VIDEO_LINK)
```

---

# 📚 Learning Purpose

This project was created as a practical Python project to understand how different Python libraries can work together to create a real-world application.

It combines:

```text
Python
   +
Speech Recognition
   +
Text-to-Speech
   +
Web Browser Automation
   +
Date & Time
   =
🎙️ Personal Voice Assistant
```

---

# 👨‍💻 Author

## Jisan Ali

🎓 B.Tech — Computer Science & Engineering (AI & ML)

This project is part of my journey of learning Python and building practical projects.

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is open-source and available for learning and educational purposes.
