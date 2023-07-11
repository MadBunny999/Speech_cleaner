import torch
import torch.nn as nn
import torch.optim as optim


class MyModel2D(nn.Module):
    def __init__(self):
        super(MyModel2D, self).__init__()
        self.pad = nn.ZeroPad2d((0, 0, 3, 4))
        self.conv1 = nn.Conv2d(1, 16, kernel_size=(9, 16), stride=(1, 1), padding=(0, 0), bias=False)
        self.relu = nn.PReLU()
        self.batchnorm1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm3 = nn.BatchNorm2d(64)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm4 = nn.BatchNorm2d(128)
        self.conv5 = nn.Conv2d(128, 256, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm5 = nn.BatchNorm2d(256)
        
        self.conv5_1 = nn.Conv2d(256, 512, kernel_size=(3, 1), stride=(8, 1), padding=(1, 0), bias=False)
        self.batchnorm5_1 = nn.BatchNorm2d(512)
        self.conv6_1 = nn.ConvTranspose2d(512, 256, kernel_size=(3, 1), stride=(8, 1), padding=(1, 0), bias=False)
        self.batchnorm6_1 = nn.BatchNorm2d(256)
        
        self.conv6 = nn.ConvTranspose2d(256, 128, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm6 = nn.BatchNorm2d(128)
        self.conv7 = nn.ConvTranspose2d(128, 64, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm7 = nn.BatchNorm2d(64)
        self.conv8 = nn.ConvTranspose2d(64, 32, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm8 = nn.BatchNorm2d(32)
        self.conv9 = nn.ConvTranspose2d(32, 16, kernel_size=(3, 1), stride=(2, 1), padding=(1, 0), bias=False)
        self.batchnorm9 = nn.BatchNorm2d(16)
        self.spatialdropout = nn.Dropout2d(0.2)
        self.conv10 = nn.Conv2d(16, 1, kernel_size=(3, 1), stride=(1, 1), padding=(1, 0))

        self.pad2 = nn.ZeroPad2d((0, 0, 2, 1))
        self.pad3 = nn.ZeroPad2d((0, 0, 1, 2))
        self.pad4 = nn.ZeroPad2d((0, 0, 0, 1))
    def forward(self, x):
        #print(x.size())
        x = self.pad(x)
        #print(x.size())
        #x = self.conv1(x)
        skip9 = self.conv1(x)
        x = self.relu(skip9)
        #print(x.size())
        x = self.batchnorm1(x)
        skip8 = self.conv2(x)
        x = self.relu(skip8)
        #print(x.size())
        x = self.batchnorm2(x)
        skip7 = self.conv3(x)
        x = self.relu(skip7)
        #print(x.size())
        x = self.batchnorm3(x)
        skip6 = self.conv4(x)
        x = self.relu(skip6)
        #print(x.size())
        x = self.batchnorm4(x)
        skip6_1 = self.conv5(x)
        #x = self.pad3(x)
        #print(x.size())
        x = self.relu(skip6_1)
        #print(x.size())
        #x = self.batchnorm5(x)
        
        x = self.conv5_1(x)
        #x = self.pad3(x)
        #print(x.size())
        x = self.relu(x)
        #print(x.size())
        x = self.batchnorm5_1(x)
        #x = self.upsample2(x)
        x = self.conv6_1(x)
        #print(x.size())
        x = x + skip6_1
        
        
        
        #x = self.upsample(x)
        x = self.conv6(x)
        #print(x.size())
        #x = x + skip6
        x = self.relu(x)
        #print(x.size())
        x = self.batchnorm6(x)
        #x = self.upsample(x)
        #x = self.pad4(x)
        x = self.conv7(x)
        x = self.pad2(x)
        x = x + skip7
        x = self.relu(x)
        #print(x.size())
        x = self.batchnorm7(x)
        #x = self.upsample(x)
        x = self.conv8(x)
        #x = self.pad3(x)
        #x = x + skip8
        x = self.relu(x)
        #print(x.size())
        x = self.batchnorm8(x)
        #x = self.upsample(x)
        #x = self.pad4(x)
        x = self.conv9(x)
        x = self.pad3(x)
        x = x + skip9
        x = self.relu(x)
        #print(x.size())
        x = self.batchnorm9(x)
        x = self.spatialdropout(x)
        x = self.conv10(x)
        
        x = self.pad4(x)
        #print(x.size())
        return x

