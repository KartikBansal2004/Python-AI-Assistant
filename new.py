import random
import datetime

# Define intents and responses
intents = {
    'greeting': ['hello', 'hi', 'hey'],                # Intents for greetings
    'farewell': ['bye', 'goodbye'],                    # Intents for farewells
    'gratitude': ['thank you', 'thanks'],              # Intents for expressing gratitude
    'query': ['how are you', 'what are you doing'],    # Intents for asking about the assistant's status
    'weather': ['weather', 'temperature', 'forecast'], # Intents for weather queries
    'time': ['time', 'current time'],                  # Intents for time queries
    'reminder': ['reminder', 'remind me'],             # Intents for setting reminders
    'joke': ['joke', 'tell me a joke'],                # Intents for jokes
    'fact': ['fact', 'interesting fact'],              # Intents for sharing facts
    'meaning': ['meaning of']                          # Intents for querying word meanings
}

responses = {
    'greeting': ['Hi there!', 'Hello!', 'Hey!'],  # Responses for greetings
    'farewell': ['Goodbye!', 'See you later!', 'Bye!'],  # Responses for farewells
    'gratitude': ['You\'re welcome!', 'No problem!', 'My pleasure!'],  # Responses for gratitude
    'query': ['I\'m doing well, thank you!', 'Just assisting you!', 'Feeling great, thank you for asking!'],  # Responses for status queries
    'weather': ['The weather is sunny today.', 'It\'s cloudy with a chance of rain.'],  # Responses for weather queries
    'time': ['The current time is ' + datetime.datetime.now().strftime("%I:%M %p")],  # Response for time queries
    'reminder': ['Sure, I will remind you.', 'Reminder set successfully.'],  # Responses for setting reminders
    'joke': ['Why don\'t scientists trust atoms? Because they make up everything!', 'I\'m reading a book on anti-gravity. It\'s impossible to put down!'],  # Responses for jokes
    'fact': ['Did you know that the shortest war in history was between Britain and Zanzibar on August 27, 1896? It lasted only 38 minutes!']  # Response for sharing facts
}

def process_command(command):
    found_intent=False

    for intent, keywords in intents.items():
        if any(keyword in command.lower() for keyword in keywords):
            found_intent = True

            response = random.choice(responses[intent])
            print(f"User: {command}\nAssistant: {response}\n")
            return
    if not found_intent:
        print("Sorry, idk")

if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye")
            break
        process_command(user_input)