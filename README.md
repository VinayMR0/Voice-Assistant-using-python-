# Voice-Assistant-using-python-
this is basic voice assistant created using python and api where it has features of greeting accoding to time, wikipedia functions,currency connversions , artihmatic function etc 


Jarvis: Personal Assistant Program
Overview
Jarvis is a personal assistant program designed to perform various tasks such as fetching the current time and date, providing weather updates, converting currencies, giving Wikipedia summaries, and more. It interacts with the user through voice commands and responses.

Features
Wake-up Command: Activates the assistant with the phrase "wake up Jarvis."
Time and Date: Provides the current time and date.
Weather Updates: Gives the current weather information for a specified city.
Currency Conversion: Converts a specified amount from one currency to another.
Wikipedia Summaries: Fetches a brief summary from Wikipedia for a given query.
Conversational Responses: Handles various questions and provides appropriate responses.
Jokes: Tells random jokes from a predefined list.
Offline Mode: Deactivates the assistant.
Requirements
Python 3.6 or higher
Required libraries:
datetime
re
random
speech_recognition
wikipedia
webbrowser
os
threading
requests
gtts
subprocess

Say "wake up Jarvis" to activate the assistant. It will greet you according to the time of day and be ready to take commands.

Give commands:

You can now ask Jarvis to perform various tasks, such as:

"What is the time?"
"What is the date?"
"What is the weather in [city]?"
"Convert [amount] [from_currency] to [to_currency]."
"Tell me about [topic]."
"Who are you?"
"Who created you?"
"What is your purpose?"
"Which language is used to build Jarvis?"
"How are you?"
"Tell me a joke."
"Do you dream?"
"What's your favorite food?"
"Are you friends with Siri?"
"What do you think about Alexa?"
Deactivate the assistant:

Say "go offline" to deactivate the assistant.

Example Commands
Time and Date:

"What is the time?"
"What is the date?"
Weather:

"What is the weather in London?"
Currency Conversion:

"Convert 100 USD to EUR."
Wikipedia Summary:

"Tell me about Python programming."
Conversational Responses:

"Who are you?"
"Who created you?"
"What is your purpose?"
"Which language is used to build Jarvis?"
"How are you?"
Jokes:

"Tell me a joke."
Note
Ensure that your microphone is properly set up and configured for the speech recognition to work.
The program currently uses gTTS for text-to-speech and afplay for playing audio files on macOS. Modify the speak function if you're using a different operating system.
