# Jarvis-AI-
JARVIS AI is a Python-based, voice-activated personal assistant designed to perform basic tasks like opening websites, playing local music, providing the current time, and launching system applications based on your spoken commands.


# JARVIS AI - Your Personal Voice Assistant

JARVIS AI is a simple, voice-controlled personal assistant designed to perform basic tasks based on your spoken commands. It can open websites, play local music, tell you the current time, and open your camera application.

## Features

* **Voice-Activated Commands:** Interact with JARVIS using your voice.
* **Web Browser Integration:** Open popular websites like YouTube, Wikipedia, and Google with a simple command.
* **Local Music Playback:** Play a specified local music file.
* **Time Inquiry:** Ask JARVIS for the current time.
* **Camera Access:** Open your system's camera application (FaceTime on macOS).
* **Basic Acknowledgment:** JARVIS will repeat your recognized command back to you.

## Tech Stack

* **Python 3.x:** The core programming language.
* **`speech_recognition`:** For converting spoken audio into text commands.
* **`os` module:** Used for interacting with the operating system, such as executing shell commands (e.g., `say` for text-to-speech on macOS, `open` for applications).
* **`webbrowser`:** For opening specified URLs in your default web browser.
* **`datetime`:** For retrieving and formatting the current date and time.
* **`subprocess`:** Used for cross-platform execution of commands, specifically for opening music files.
* **`openai` (Imported, but not actively used in provided code):** Indicates potential for future integration with advanced AI models for more complex conversational capabilities.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Jarvis-AI.git](https://github.com/your-username/Jarvis-AI.git)
    cd Jarvis-AI
    ```

2.  **Install the required Python library:**
    ```bash
    pip install SpeechRecognition
    ```

3.  **Microphone Setup:**
    * Ensure your microphone is properly connected and configured on your system.
    * Grant microphone access permissions to your terminal or IDE if prompted by your operating system.

4.  **Platform-Specific Notes:**
    * **Text-to-Speech (`say` command):** The current implementation uses the `say` command, which is native to macOS. If you are on Windows or Linux, you will need to replace `os.system(f"say {text}")` with a text-to-speech library compatible with your OS (e.g., `pyttsx3`, `gTTS`).
    * **Music File Path:** The `musicPath` variable is currently hardcoded to `/Users/abhijithmr/Downloads/Old Money AP Dhillon.mp3`. **You must change this path** to an existing MP3 file on your system for the "play music" command to work.
    * **Camera Command:** The `open camera` command uses `open /System/Applications/FaceTime.app`, which is specific to macOS. For Windows or Linux, you'll need to adjust this command to launch your preferred camera application.

## How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the Python script:
    ```bash
    python jarvis_ai.py
    ```

## Usage

Once JARVIS is running, you will see "Listening......." in your console. Speak the following commands clearly:

* "Open YouTube"
* "Open Wikipedia"
* "Open Google"
* "Open anime" (This will open the specific anime URL provided in the code)
* "Play music"
* "What is the time" or "Tell me the time"
* "Open camera"

JARVIS will respond by saying "Opening [website name] sir ......" or "Sir the time is [current time]", and will repeat your recognized query.

## Limitations and Future Improvements

* **Platform Dependency:** The `say` command and camera opening command are macOS specific.
* **Hardcoded Commands:** The list of websites and music file paths are hardcoded.
* **Limited Functionality:** The current version supports a very basic set of commands.
* **Error Handling:** More robust error handling for speech recognition and command execution could be implemented.
* **Advanced AI Integration:** The `openai` import suggests the possibility of integrating with large language models for more dynamic and complex conversational abilities.
* **Customizable Commands:** Allow users to define their own commands and associated actions.

## Contributing

Feel free to fork this repository, suggest improvements, or submit pull requests.

## License

Abhijijth MR
