# -*- coding: utf-8 -*-
"""hw2_cnn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/lcqsigi/my-notebooks/blob/main/hw2_cnn7.ipynb

# Homework 2 - Convolutional Neural Nets

In this homework, we will be working with google [colab](https://colab.research.google.com/). Google colab allows you to run a jupyter notebook on google servers using a GPU or TPU. To enable GPU support, make sure to press Runtime -> Change Runtime Type -> GPU.
"""
import os

os.system('mkdir cats_and_dogs_filtered/')

os.system('mkdir cats_and_dogs_filtered/validation/')

os.system('mkdir cats_and_dogs_filtered/validation/cats')

os.system('mkdir cats_and_dogs_filtered/validation/dogs')

os.system('cp ../dog.tar cats_and_dogs_filtered/validation/dogs/')
os.system('cp ../cat.tar cats_and_dogs_filtered/validation/cats/')

os.system('tar -xvf cats_and_dogs_filtered/validation/dogs/dog.tar')
os.system('tar -xvf cats_and_dogs_filtered/validation/cats/cat.tar')

os.system('mv cat*.jpg cats_and_dogs_filtered/validation/cats/')
os.system('mv dog*.jpg cats_and_dogs_filtered/validation/dogs/')

import torch
torch.cuda.empty_cache()
import torchvision
from torchvision import transforms
from PIL import Image # PIL is a library to process images

# These numbers are mean and std values for channels of natural images. 
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

# Inverse transformation: needed for plotting.
unnormalize = transforms.Normalize(
   mean=[-0.485/0.229, -0.456/0.224, -0.406/0.225],
   std=[1/0.229, 1/0.224, 1/0.225]
)

train_transforms = transforms.Compose([
                                    transforms.Resize((256, 256)),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.ColorJitter(hue=.1, saturation=.1, contrast=.1),
                                    transforms.RandomRotation(20, resample=Image.BILINEAR),
                                    transforms.GaussianBlur(7, sigma=(0.1, 1.0)),
                                    transforms.ToTensor(),  # convert PIL to Pytorch Tensor
                                    normalize,
                                ])

validation_transforms = transforms.Compose([
                                    transforms.Resize((256, 256)),
                                    transforms.ToTensor(), 
                                    normalize,
                                ])

#train_dataset = torchvision.datasets.ImageFolder('./cats_and_dogs_filtered/train', transform=train_transforms)
validation_dataset, test_dataset = torch.utils.data.random_split(torchvision.datasets.ImageFolder('./cats_and_dogs_filtered/validation', transform=validation_transforms), [10, 10], generator=torch.Generator().manual_seed(42))

from torch import nn
import torch.nn.functional as F

class CNN(torch.nn.Module):

  def __init__(self):
    super().__init__()
    # Image shape (3,256,256)

    self.down1 = torch.nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=64, stride=2, kernel_size=7), # 64*125*125
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=3, stride=2))  # 64*62*62                
    self.conv1_1_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=64, out_channels=64, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.Conv2d(in_channels=64, out_channels=64, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU())  # 64*62*62 
    self.conv1_2_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=64, out_channels=64, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.Conv2d(in_channels=64, out_channels=64, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU())  # 64*62*62
    self.down2 = torch.nn.Sequential(
        nn.Conv2d(in_channels=64, out_channels=128, stride=2, kernel_size=3), #128*30*30
        nn.BatchNorm2d(128),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU())  #128*30*30
    self.conv2_1_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=128, out_channels=128, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU())  #128*30*30 
    self.conv2_2_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=128, out_channels=128, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU())  #128*30*30 
    self.down3 = torch.nn.Sequential(
        nn.Conv2d(in_channels=128, out_channels=256, stride=2, kernel_size=3,padding=1), #256*15*15
        nn.BatchNorm2d(256),
        nn.ReLU(),
        nn.Conv2d(in_channels=256, out_channels=256, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(256),
        nn.ReLU())  #256*15*15
    self.conv3_1_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=256, out_channels=256, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(256),
        nn.ReLU(),
        nn.Conv2d(in_channels=256, out_channels=256, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(256),
        nn.ReLU())  #256*15*15
    self.conv3_2_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=256, out_channels=256, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(256),
        nn.ReLU(),
        nn.Conv2d(in_channels=256, out_channels=256, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(256),
        nn.ReLU())  #256*15*15
    self.down4 = torch.nn.Sequential(
        nn.Conv2d(in_channels=256, out_channels=512, stride=2, kernel_size=3,padding=1), #512*8*8
        nn.BatchNorm2d(512),
        nn.ReLU(),
        nn.Conv2d(in_channels=512, out_channels=512, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU())  #512*8*8    
    self.conv4_1_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=512, out_channels=512, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU(),
        nn.Conv2d(in_channels=512, out_channels=512, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU())  #512*8*8
    self.conv4_2_x = torch.nn.Sequential(
        nn.Conv2d(in_channels=512, out_channels=512, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU(),
        nn.Conv2d(in_channels=512, out_channels=512, stride=1, kernel_size=3, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU())  #512*8*8
    self.pool = nn.AdaptiveAvgPool2d((1,1))
    self.fc = nn.Linear(512, 2)

    
  def forward(self, x):
    x = self.down1(x)
    x = self.conv1_1_x(x)+x
    x = self.conv1_2_x(x)+x
    x = self.down2(x)
    x = self.conv2_1_x(x)+x
    x = self.conv2_2_x(x)+x
    x = self.down3(x)
    x = self.conv3_1_x(x)+x
    x = self.conv3_2_x(x)+x
    x = self.down4(x)
    x = self.conv4_1_x(x)+x
    x = self.conv4_2_x(x)+x
    x = self.pool(x)
    x = torch.flatten(x, 1)
    x = self.fc(x)
    out = F.log_softmax(x, dim=1)
    return out

#!cp frcnn.pth drive/MyDrive/frcnn0906.pth
model = torch.load('../frcnn0906.pth',map_location=torch.device('cpu'))

from tqdm.notebook import tqdm

def get_loss_and_correct(model, batch, criterion, device):
  # Implement forward pass and loss calculation for one batch.
  # Remember to move the batch to device.
  # 
  # Return a tuple:
  # - loss for the batch (Tensor)
  # - number of correctly classified examples in the batch (Tensor)
  (data, target) = batch
  data, target = data.to(device), target.to(device)
  data = data.view(-1, 3, 256, 256)
  output = model(data)
  loss = criterion(output, target)
  pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability    
  correct = pred.eq(target.data.view_as(pred)).cpu().sum()
  #print(loss,pred.shape,pred,target.shape,target,correct.shape,correct)
  return loss,correct

# TODO
# 1. Calculate and show the test_dataset accuracy of your model.
# 2. Visualize some correctly and incorrectly classified examples.
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=8, num_workers=4)

model.eval()

if torch.cuda.is_available():
  model = model.cuda()
  criterion = nn.NLLLoss().cuda()
  device = torch.device("cuda:0")
else:
  criterion = nn.NLLLoss()
  device = torch.device("cpu")

pbar = tqdm(range(1))

for i in pbar:
  total_test_loss = 0.0
  total_test_correct = 0.0

  model.eval()

  with torch.no_grad():
    for batch in test_dataloader:
      loss, correct = get_loss_and_correct(model, batch, criterion, device)
      total_test_correct += correct.item()
      test_accuracy = ((total_test_correct) / len(test_dataset))*100
    print(f'Test accuracy: {test_accuracy:.2f}%')

# TODO
# 1. Calculate and show the test_dataset accuracy of your model.
# 2. Visualize some correctly and incorrectly classified examples.
from matplotlib import pyplot as plt

with torch.no_grad():
  test_loss = 0
  correct = 0
  test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=500, num_workers=4)
  for data, target in test_loader:
    data, target = data.to(device), target.to(device)
    data = data.view(-1, 3, 256, 256)
    model.to(device)
    output = model(data)                                                          
    pred = output.data.max(1, keepdim=True)[1].data.view_as(target)   # get the index of the max log-probability                                                             
    correct += pred.eq(target.data).cpu().sum().item()

  test_loss /= len(test_loader.dataset)
  accuracy = 100. * correct / len(test_loader.dataset)
  print('\nTest set: Accuracy: {}/{} ({:.0f}%)\n'.format(correct, len(test_loader.dataset),
          accuracy))
  cor = (pred==target).int().nonzero().view(correct).tolist()[0:4]
  incor = (pred!=target).int().nonzero().view(10-correct).tolist()[0:4]

  plt.figure()
  for i in range(len(cor)):
    c_data, _ = test_loader.dataset.__getitem__(cor[i])
    c_data = unnormalize(c_data)
    plt.subplot(2,2,i+1)
    img = c_data.view(3,256,256).cpu().swapaxes(0,1)
    img = img.swapaxes(1,2)
    plt.imshow(img)
    plt.axis('off')
    plt.title('Correct')
    print('Correct prefiction:',cor[i],'Prediction is: ',pred[cor[i]],'True label is: ',target[cor[i]])

  plt.figure()
  for i in range(len(incor)):
    inc_data, _ = test_loader.dataset.__getitem__(incor[i])
    inc_data = unnormalize(inc_data)
    plt.subplot(2,2,i+1)
    img = inc_data.view(3,256,256).cpu().swapaxes(0,1)
    img = img.swapaxes(1,2)
    plt.imshow(img)
    plt.axis('off')
    plt.title('Incorrect')
    print('Incorrect prefiction:',incor[i],'Prediction is: ',pred[incor[i]],'True label is: ',target[incor[i]])
