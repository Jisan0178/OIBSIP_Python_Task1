# 🎙️ Jisan's Personal Voice Assistant

> A Python-based personal voice assistant that listens to voice commands, understands spoken instructions, responds using speech, and performs useful tasks such as telling the time and date, opening websites, and searching Google.

---

## ✨ Features

- 🎤 **Voice Recognition** — Recognizes voice commands through the microphone.
- 🔊 **Voice Response** — Responds to the user using text-to-speech.
- 🕐 **Time Information** — Tells the current time.
- 📅 **Date Information** — Provides the current date.
- 🌐 **Open Google** — Opens Google in the default browser.
- ▶️ **Open YouTube** — Opens YouTube in the default browser.
- 🔎 **Google Search** — Searches Google using a voice command.
- 👋 **Greeting Support** — Responds to greetings such as "Hello".
- 🛑 **Stop Command** — Exits the assistant with a closing message.
- ⚠️ **Error Handling** — Handles unclear speech and speech-recognition errors.

---

## 🛠️ Technologies Used

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
| 🐍 Python            | Main programming language           |
| 🎤 SpeechRecognition | Converts spoken commands into text  |
| 🔊 pyttsx3           | Converts text into speech           |
| 🕐 datetime          | Retrieves the current date and time |
| 🌐 webbrowser        | Opens websites and Google searches  |

---

## 📁 Project Structure

```text
OIBSIP_Python_Task1/
│
├── voice_assistant.py
├── README.md
└── requirements.txt
```

> **Note:** Replace `voice_assistant.py` with the actual name of your Python file if it is different.

---

## ⚙️ Requirements

Before running the project, make sure you have:

- Python 3.x
- A working microphone
- An internet connection for online speech recognition
- A web browser
- The required Python libraries

---

## 📦 Installation

### 1. Install Python

Download Python from the official website:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation on Windows, enable **Add Python to PATH** if the installer provides that option.

### 2. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Jisan0178/OIBSIP_Python_Task1.git
```

### 3. Open the Project Folder

```bash
cd OIBSIP_Python_Task1
```

### 4. Install Required Libraries

Install the main dependencies using:

```bash
pip install SpeechRecognition pyttsx3
```

For microphone support, install PyAudio if required:

```bash
pip install PyAudio
```

> **Note:** PyAudio installation can depend on your Python version and operating system. If your project already has a `requirements.txt` file, you can install its dependencies with `pip install -r requirements.txt`.

---

## ▶️ How to Run

1. Open the project folder in **Visual Studio Code**.
2. Open the integrated terminal.
3. Make sure the required libraries are installed.
4. Run your Python file:

```bash
python voice_ass.py
```

5. Allow microphone access if prompted.
6. Wait for the assistant's greeting and speak a supported command clearly.

The assistant starts with a welcome message similar to:

> "Hello! Welcome to Jisan's personal Voice Assistant. How can I help you today..."

The exact message depends on your Python code.

---

## 🎤 Voice Commands

The following examples describe the intended commands. Use only those that are implemented in your current version of the program.

### 🕐 Ask for the Time

**Say:**

```text
What is the time
```

**Example response:**

```text
The time is 12:30:45 AM
```

### 📅 Ask for the Date

**Say:**

```text
What is the date
```

**Example response:**

```text
Today's date is 14-10-2026
```

### 👋 Say Hello

**Say:**

```text
Hello
```

The assistant responds with a greeting.

### 🌐 Open Google

**Say:**

```text
Open Google
```

The assistant opens Google in your default web browser.

### ▶️ Open YouTube

**Say:**

```text
Open YouTube
```

The assistant opens YouTube in your default web browser.

### 🔎 Search Google

**Say:**

```text
Search for Python tutorials
```

The assistant opens Google and searches for Python tutorials.

**Other examples:**

```text
Search for machine learning
```

```text
Search for Java tutorials
```

```text
Search for Python projects
```

### 🛑 Stop the Assistant

**Say:**

```text
give up
```

If your program supports this command, the assistant says goodbye and terminates.

---

## 🔄 How It Works

The assistant follows a simple voice-processing workflow:

```text
          🎤 Microphone
               │
               ▼
      Speech Recognition
               │
               ▼
       Convert Speech
          into Text
               │
               ▼
        Identify Command
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
      Time    Date   Web Commands
                       │
                       ▼
                 Open or Search
                   Websites
       └───────┬────────┘
               ▼
       Generate Response
               │
               ▼
        Text-to-Speech
               │
               ▼
           🔊 Voice
```

### Workflow Explanation

1. The microphone captures the user's voice.
2. SpeechRecognition processes the recorded audio and converts it into text.
3. The program checks the recognized text to identify the requested command.
4. Python executes the corresponding action, such as providing the time or opening a website.
5. The assistant responds through pyttsx3.

---

## 🧠 Main Python Concepts Used

This project demonstrates practical use of:

- Variables and strings
- Functions
- Conditional statements (`if`, `elif`, `else`)
- Loops
- Exception handling (`try` and `except`)
- Python modules and external libraries
- Microphone input
- Speech recognition
- Text-to-speech conversion
- Date and time handling
- Web browser automation

---

## 📌 Main Code Components

The following snippets illustrate the key operations used in a typical implementation of this project. Your actual code may differ.

### 1. Initialize the Speech Recognizer

```python
recognizer = speech_recognition.Recognizer()
```

Creates a recognizer object that processes audio for speech recognition.

### 2. Capture Microphone Input

```python
with speech_recognition.Microphone() as mic:
    audio = recognizer.listen(mic, timeout=15)
```

Accesses the microphone and listens for audio input.

### 3. Convert Speech to Text

```python
text = recognizer.recognize_google(audio)
```

Uses Google's speech recognition service to convert captured audio into text. Internet access is generally required.

### 4. Convert Text to Speech

```python
engine = pyttsx3.init()
engine.say("Hello! How can I help you?")
engine.runAndWait()
```

Initializes the text-to-speech engine and speaks the provided message.

### 5. Open a Website

```python
webbrowser.open("https://www.google.com")
```

Opens Google in the default web browser.

### 6. Get the Current Date and Time

```python
import datetime

current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
```

Uses the `datetime` module to retrieve and format the current time and date.

---

## 📸 Project Screenshots

You can add screenshots of your project here after uploading the image files to your GitHub repository.

For example:

```markdown
![Voice Assistant Screenshot](screenshots/voice-assistant.png)
```

Replace the image path with the actual location of your screenshot.

---

## 🎥 Project Demo

Watch the project demonstration on LinkedIn:

**[Watch the Voice Assistant Demo](https://lnkd.in/p/dqW5FbJU)**


---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Building a voice-based application using Python
- Integrating speech recognition and text-to-speech libraries
- Handling microphone input and spoken commands
- Working with date and time functions
- Opening websites and performing web searches
- Practicing functions, conditional statements, loops, and exception handling
- Organizing and documenting a Python project using GitHub

---

## 👨‍💻 Author

**Jisan Ali**

🎓 B.Tech — Computer Science and Engineering (AI & ML)

Python Programming Intern — Oasis Infobyte (OIBSIP)

This project was developed as part of my Python programming learning journey and internship experience at Oasis Infobyte.

---

## 🔗 Links

- **GitHub Repository:** [OIBSIP Python Task 1](https://github.com/Jisan0178/OIBSIP_Python_Task1)
- **Oasis Infobyte Website:** [https://oasisinfobyte.com/](https://oasisinfobyte.com/)

---

