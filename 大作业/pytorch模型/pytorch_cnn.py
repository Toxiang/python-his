#about torch...
import torch
import torch.nn as nn
import torch
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import zipfile

lr = 0.001 # l学习率
batch_size = 100 # 一般情况下，一个训练集中会有大量的样本，为了提高训练速度，会将整个training set分为n_batch组，每组包含batch_size个samples
# 即：整个数据集samples个数 = batch_size * n_batch
epochs = 20 # 每一个epoch，所有的训练集被使用一次

device = 'cuda' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(1234)
if device =='cuda':
    torch.cuda.manual_seed_all(1234)

# os.listdir('../input/face-pic')

# os.makedirs('../data', exist_ok=True)

base_dir = '../input/face-pic'
train_dir = '../input/face-pic/data/train'
test_dir =  '../input/face-pic/data/test'

# os.listdir(train_dir)[:5]
# os.listdir(test_dir)

import glob

train_list = glob.glob(os.path.join(train_dir,'*.jpg'))
test_list = glob.glob(os.path.join(test_dir, '*.jpg'))

# train_list

# 检查数据集
from PIL import Image
random_idx = np.random.randint(1,18000,size=10)

fig = plt.figure()
i=1
for idx in random_idx:
    ax = fig.add_subplot(2,5,i)
    img = Image.open(train_list[idx])
    plt.imshow(img)
    i+=1

plt.axis('off')
plt.show()

print(train_list[0].split('/')[-1].split('.')[0])
print(train_list[0].split('/')[-1].split('.'))

from sklearn.model_selection import train_test_split
train_list, val_list = train_test_split(train_list, test_size=0.2)

#data Augumentation
train_transforms =  transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ])

val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ])


test_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
     transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
    ])


class dataset(torch.utils.data.Dataset):
    # 가져와서 처리
    def __init__(self, file_list, transform=None):
        self.file_list = file_list
        self.transform = transform

    # dataset length
    def __len__(self):
        self.filelength = len(self.file_list)
        return self.filelength

    # load an one of images
    def __getitem__(self, idx):
        img_path = self.file_list[idx]
        img = Image.open(img_path)
        img_transformed = self.transform(img)

        label = img_path.split('/')[-1].split('.')[0]
        if label == 'female':
            label = 1
        elif label == 'male':
            label = 0

        return img_transformed, label

train_data = dataset(train_list, transform=train_transforms)
test_data = dataset(test_list, transform=test_transforms)
val_data = dataset(val_list, transform=test_transforms)

train_loader = torch.utils.data.DataLoader(dataset = train_data, batch_size=batch_size, shuffle=True )
test_loader = torch.utils.data.DataLoader(dataset = test_data, batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(dataset = val_data, batch_size=batch_size, shuffle=True)

print(len(train_data), len(train_loader))
print(len(val_data), len(val_loader))
#check our images shape
print(train_data[0][0].shape)


class Cnn(nn.Module):
    def __init__(self):
        super(Cnn, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc1 = nn.Linear(3 * 3 * 64, 10)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(10, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.view(out.size(0), -1)
        out = self.relu(self.fc1(out))
        out = self.fc2(out)
        return out

def get_model():
    model = models.resnet34(pretrained=False)
    model.fc = nn.Linear(512, 2)
    return model

# model = Cnn().to(device)
model = get_model().to(device)
model.train()

optimizer = optim.Adam(params = model.parameters(),lr=0.001)
criterion = nn.CrossEntropyLoss()

epochs = 80

for epoch in range(epochs):
    epoch_loss = 0
    epoch_accuracy = 0

    for data, label in train_loader:
        data = data.to(device)
        label = label.to(device)

        output = model(data)
        loss = criterion(output, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        acc = ((output.argmax(dim=1) == label).float().mean())
        epoch_accuracy += acc / len(train_loader)
        epoch_loss += loss / len(train_loader)

    print('Epoch : {}, train accuracy : {}, train loss : {}'.format(epoch + 1, epoch_accuracy, epoch_loss))

    with torch.no_grad():
        epoch_val_accuracy = 0
        epoch_val_loss = 0
        for data, label in val_loader:
            data = data.to(device)
            label = label.to(device)

            val_output = model(data)
            val_loss = criterion(val_output, label)

            acc = ((val_output.argmax(dim=1) == label).float().mean())
            epoch_val_accuracy += acc / len(val_loader)
            epoch_val_loss += val_loss / len(val_loader)

        print('Epoch : {}, val_accuracy : {}, val_loss : {}'.format(epoch + 1, epoch_val_accuracy, epoch_val_loss))

torch.save(model,'./file/pytorch_model.pkl')

torch.save(model.state_dict(),'./file/parameter.pkl')

sex_probs = []
model.eval()
with torch.no_grad():
    for data, fileid in test_loader:
        data = data.to(device)
        preds = model(data)
        preds_list = F.softmax(preds, dim=1)[:, 1].tolist()
        sex_probs += list(zip(list(fileid), preds_list))
sex_probs.sort(key = lambda x : int(x[0]))
sex_probs

idx = list(map(lambda x: x[0],sex_probs))
prob = list(map(lambda x: x[1],sex_probs))

submission = pd.DataFrame({'id':idx,'label':prob})
submission

# sample = submission
for i in range(len(submission['label'])):
    if(submission['label'][i]>0.5):
        submission['label'][i] = 1
    else:
        submission['label'][i] = 0


submission.label = submission.label.astype(int)

submission.to_csv('result.csv',index=False)
