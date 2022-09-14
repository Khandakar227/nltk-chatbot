from intents import list_of_intents
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from model import NeuralNet

all_words = []
tags = []
xy = []

for intent in list_of_intents():
    tag = intent['tag']
    tags.append(tag)
    text:str
    for text in intent['text']:
        w = tokenize(text)
        all_words.extend(w)
        xy.append((w, tag))    

blacklist = ['?', ',', '.', '!']
all_words = [stem(w) for w in all_words if w not in blacklist]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for (text, tag) in xy:
    bw = bag_of_words(text, all_words)
    x_train.append(bw)
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples

# Hyper parameters
batch_size = 8
input_size = len(x_train[0])
hidden_size = 8
num_classes = len(tags)
learning_rate = 0.001
num_epochs = 1000

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)
        # forward
        outputs = model(words)
        loss = criterion(outputs, labels)
        # backward and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    if (epoch + 1)% 100 == 0:
        print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}")

print(f"final loss, loss={loss.item():.4f}")


data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": num_classes,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)
print(f"Training done. file saved to {FILE}")