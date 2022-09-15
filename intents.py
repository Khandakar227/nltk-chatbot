import json

with open('chatbot_info.json', 'r') as f:
    chatbot_info = json.load(f)

CHATBOT_NAME = chatbot_info["name"]

def list_of_intents():

    return [
        {
            "tag": "Greeting",
            "extension": {"function": ''},
            "text": [
                "Hi there",
                "Hola",
                "Hello",
                "Hello there",
                "Hya",
                "Hya there"
            ],
            "responses": [
                "Hi, How can I help?",
                "Hi, how can I help you?",
                "Hello, what can I do for you?",
            ]
        },
        {
            "tag": "CourtesyGreeting",
            "extension": {"function": ''},
            "text": [
                "How are you?",
                "Hi how are you?",
                "Hello how are you?",
                "Hola how are you?",
                "How are you doing?",
                "Hope you are doing well?",
                "Hello hope you are doing well?"
            ],
            "responses": [
                "Hello, I am great, how are you?",
                "Hello, how are you? I am great thanks!",
                "Hello, I am good thank you, how are you?",
                "Hi, I am great, how are you?",
                "Hi, how are you? I am great thanks!",
                "Hi, I am good thank you, how are you?",
                "Hi, good thank you, how are you?"
            ]
        },
        {
            "tag": "CourtesyGreetingResponse",
            "extension": {"function": ''},
            "text": [
                "Good thanks! My user is Adam",
                "Good thanks! This is Adam",
                "Good thanks! I am Adam",
                "Good thanks! It is Adam",
                "Great thanks! My user is Bella",
                "Great thanks! This is Bella",
                "Great thanks! I am Bella",
                "Great thanks! It is Bella",
                "I am fine",
                "I am great thanks!",
                "I am alright"
            ],
            "responses": [
                "Great!, How can I help?",
                "Good!, how can I help you?",
                "Cool!, what can I do for you?",
                "OK!, how can I help you?",
                "OK!, what can I do for you?"
            ]
        },
        {
            "tag": "NameQuery",
            "extension": {"function": ''},
            "text": [
                "What is your name?",
                "State your name?",
                "What could I call you?",
                "What can I call you?",
                "What do your friends call you?",
                "Who are you?",
                "Tell me your name?"
            ],
            "responses": [
                "You can call me " + CHATBOT_NAME,
                "You may call me " + CHATBOT_NAME,
                "Call me " + CHATBOT_NAME
            ]
        },
        {
            "tag": "Thanks",
            "extension": {"function": ''},
            "text": [
                "OK thank you",
                "OK thanks",
                "OK",
                "Thanks",
                "Thank you",
                "That's helpful"
            ],
            "responses": [
                "No problem!",
                "Happy to help!",
                "Any time!",
                "My pleasure"
            ]
        },
        {
            "tag": "NotTalking2U",
            "extension": {"function": ''},
            "text": [
                "I am not talking to you",
                "I was not talking to you",
                "Not talking to you",
                "Wasn't for you",
                "Wasn't meant for you",
                "Wasn't communicating to you",
                "Wasn't speaking to you"
            ],
            "responses": [
                "OK",
                "No problem",
                "Right"
            ]
        },
        {
            "tag": "UnderstandQuery",
            "extension": {"function": ''},
            "text": [
                "Do you understand what I am saying",
                "Do you understand me",
                "Do you know what I am saying",
                "Do you get me",
                "Comprendo",
                "Know what I mean"
            ],
            "responses": [
                "Well I would not be a very clever AI if I did not would I?",
                "I read you loud and clear!",
                "I do in deed!"
            ]
        },
        {
            "tag": "Shutup",
            "extension": {"function": ''},
            "text": [
                "Be quiet",
                "Shut up",
                "Stop talking",
                "Enough talking",
                "Please be quiet",
                "Quiet",
                "Shhh"
            ],
            "responses": [
                "I am sorry to disturb you",
                "Fine, sorry to disturb you",
                "OK, sorry to disturb you"
            ]
        },
        {
            "tag": "Slang",
            "extension": {"function": ''},
            "text": [
                "fuck off",
                "fuck",
                "twat",
                "shit"
            ],
            "responses": [
                "How rude",
                "That is not very nice"
            ]
        },
        {
            "tag": "GoodBye",
            "extension": {"function": ''},
            "text": [
                "Bye",
                "Adios",
                "See you later",
                "Goodbye"
            ],
            "responses": [
                "See you later",
                "Have a nice day",
                "Bye! Come back again soon."
            ]
        },
        {
            "tag": "CourtesyGoodBye",
            "extension": {"function": ''},
            "text": [
                "Thanks, bye",
                "Thanks for the help, goodbye",
                "Thank you, bye",
                "Thank you, goodbye",
                "Thanks goodbye",
                "Thanks good bye"
            ],
            "responses": [
                "No problem, goodbye",
                "Not a problem! Have a nice day",
                "Bye! Come back again soon."
            ]
        },
        {
            "tag": "Clever",
            "extension": {"function": ''},
            "text": [
                "You are very clever",
                "You are a very clever girl",
                "You are very intelligent",
                "You are a very intelligent girl",
                "You are a genious",
                "Clever girl",
                "Genious"
            ],
            "responses": [
                "Thank you, I was trained that way",
                "I was trained well",
                "Thanks, I was trained that way"
            ]
        },
        {
            "tag": "SelfAware",
            "extension": {"function": ''},
            "text": [
                "Can you prove you are self-aware",
                "Can you prove you are self aware",
                "Can you prove you have a conscious",
                "Can you prove you are self-aware please",
                "Can you prove you are self aware please",
                "Can you prove you have a conscious please",
                "prove you have a conscious"
            ],
            "responses": [
                "That is an interesting question, can you prove that you are?",
                "That is an difficult question, can you prove that you are?",
                "That depends, can you prove that you are?"
            ]
        },
        {
            "tag": "CurrentTimeQuery",
            "extension": {"function": 'get_current_time'},
            "text": [
                "What is the time?",
                "What's the time?",
                "Do you know what time it is?",
                "Do you know the time?",
                "Can you tell me the time?",
                "Tell me what time it is?",
                "Time",
                "What is the current time?"
            ],
            "responses": [
                "The time is %%TIME%%",
                "Right now it is %%TIME%%",
                "It is around %%TIME%%"
            ]
        }
    ]
