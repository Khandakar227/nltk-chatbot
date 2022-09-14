def list_of_intents():
    CHATBOT_NAME = "Evy"
    return [
        {
            "tag": "Greeting",
            "text": [
                "Hi",
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
                "Hola!, how can I help you?"
            ]
        },
        {
            "tag": "CourtesyGreeting",
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
            "text": [
                "Good thanks! My user is Adam",
                "Good thanks! This is Adam",
                "Good thanks! I am Adam",
                "Good thanks! It is Adam",
                "Great thanks! My user is Bella",
                "Great thanks! This is Bella",
                "Great thanks! I am Bella",
                "Great thanks! It is Bella"
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
            "text": [
                "What is your name?",
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
        }
    ]
