# Dora-The-Voice-Assistant


Dora is an intelligent voice assistant web application designed to interact with users through voice and text. Built using modern web technologies, it allows users to perform various tasks like answering questions, play games, fetching information, and more – all through a friendly interface.
## 🧠 Features

- Speech recognition and response
- Friendly chatbot interface
- Integration with knowledge sources (like Wikipedia, web search)
- play game


## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python 
- Voice Recognition: SpeechRecognition, pyttsx3 any more. etc.
- Database: SQLite3
 
## ⚙️ Requirements

- **Windows 10 / 11** (uses Windows speech and `os.startfile`)
- **Python 3.12 only** (recommended: 3.12.10). Newer versions such as 3.13 / 3.14 are **not supported**, because `PyAudio` has no prebuilt package for them.
- A working microphone and an internet connection (for speech recognition and the web UI libraries)
- Microsoft Edge or Google Chrome


## 🚀 How to Run the Project

**1. Open a terminal (PowerShell) in the project folder** (the folder that contains `run.py`).

**2. Create a virtual environment with Python 3.12:**

```powershell
py -3.12 -m venv venv
```

**3. Activate the virtual environment:**

```powershell
venv\Scripts\activate
```

Check the version. It must print `Python 3.12.x`:

```powershell
python --version
```

**4. Install the required packages:**

```powershell
python -m pip install --upgrade pip
pip install eel pyttsx3 SpeechRecognition playsound==1.2.2 pywhatkit pyautogui pvporcupine wikipedia pyaudio
```

**5. Start the assistant:**

```powershell
python run.py
```

**6. Open the app in your browser** (if it does not open automatically):

```
http://localhost:8000/dorahome.html
```

> Every time you open a new terminal, activate the environment again with `venv\Scripts\activate` before running `python run.py`.


## 🎤 Example Commands

| Say / Type | What happens |
|---|---|
| `hii`, `how are you` | Friendly reply |
| `what is your name` | Dora introduces herself |
| `what time is it` | Tells the current time |
| `open youtube` | Opens YouTube |
| `play believer` | Plays the song on YouTube |
| `who is Albert Einstein` | Wikipedia summary |
| `send message to <contact>` | Sends a WhatsApp message (contact must be in the database) |


## 🔧 Troubleshooting

- **`No module named 'eel'`**: the virtual environment is not active or the packages are not installed. Repeat steps 3 and 4.
- **PyAudio fails to install**: you are not on Python 3.12. Delete the `venv` folder and repeat from step 2.
- **`WinError 10048` (port already in use)**: another program is using port 8000. Close it, or change the port in `main.py`.
- **No voice output**: check your speaker volume and that a Windows voice is installed (Settings → Time & Language → Speech).
- **Hotword ("jarvis") not working**: add a free access key from [console.picovoice.ai](https://console.picovoice.ai) to `PORCUPINE_ACCESS_KEY` in `engine/features.py`.

## output


![image](https://github.com/user-attachments/assets/7012a39f-7006-485b-92b6-2a8e2cf78f31)

![image](https://github.com/user-attachments/assets/49297d09-56e7-43b4-b541-bfa90f416ea1) 

![image](https://github.com/user-attachments/assets/528944a6-588a-4887-8db9-aaeaace402e6)

![image](https://github.com/user-attachments/assets/e482914f-e18d-4bb5-98ad-03ce9a7e261f)

![image](https://github.com/user-attachments/assets/ba8bb9ef-d5ba-430b-9539-741d2f690e43)



  
