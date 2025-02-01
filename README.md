# nlp-project
This program is a speech-to-speech interactive system that continuously listens to the user’s voice, converts it to text, and then speaks it back using text-to-speech (TTS). The program runs in a loop until the user says "exit".
1. Importing Required Libraries
The program imports necessary libraries:
•	speech_recognition for speech input and conversion to text.
•	os for handling files.
•	time for introducing delays.
•	gtts for text-to-speech conversion.
•	pygame for playing the generated speech audio.
2. Speech Recognition Function (recognize_speech())
This function captures audio from the microphone, processes it, and converts it to text using Google’s Speech Recognition API.
•	It listens for the user’s voice while adjusting for background noise.
•	If the speech is successfully recognized, it returns the text.
•	If recognition fails due to unclear speech or internet issues, it handles errors gracefully.
3. Text-to-Speech Function (text_to_speech(text))
This function converts recognized text into speech and plays it.
•	The gTTS library converts the text into an MP3 file.
•	The pygame.mixer module plays the generated speech file.
•	After playback, the temporary MP3 file is deleted to free storage.
•	If the file cannot be deleted (due to permission issues), an error message is displayed.
4. Main Function (main())
This function runs the program in a loop.
•	It continuously listens for user input.
•	If the user says "exit", the program stops.
•	Otherwise, the recognized speech is converted to text and spoken back using TTS.
5. Program Execution
The script runs when executed directly. It continuously listens and responds to user speech, enabling hands-free interaction. The system ensures smooth operation by handling errors effectively.
