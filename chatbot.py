import random
from intents import list_of_intents, CHATBOT_NAME
import torch
from model import NeuralNet
from nltk_utils import bag_of_words,tokenize
from extensions import get_current_time
import pyttsx3
import subprocess

def speak(text:str):
    subprocess.call(['./speech.sh', text])

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
num_classes = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, num_classes).to(device)
model.load_state_dict(model_state)
model.eval()

print("Chatbot initialized!")

while (True):
    sentence = input('User: ')
    if (sentence == "exit"): break

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob > 0.75:
        for intent in list_of_intents():
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                if (intent["extension"]["function"]):
                    if intent["extension"]["function"] == "get_current_time":
                        print(f"{CHATBOT_NAME}: {response.replace('%%TIME%%', get_current_time())}")
                        speak(response.replace('%%TIME%%', get_current_time()))
                else:
                    print(f"{CHATBOT_NAME}: {response}")
                    speak(response)
    else:
        print(f"{CHATBOT_NAME}: I do not understand. My responses are limited.")
        speak("I do not understand. My responses are limited.")

    
    # print(prob, prob >0.75)
