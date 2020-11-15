import numpy as np
import random

def readfile(file):
    f = open(file, "r")
    if(file[-3:] == 'txt'):
        data = f.readlines()
        dataset = np.zeros((len(data)-2, len(data[2].split('\t'))-1))
        label = np.zeros((len(data)-2))

        for i in range(len(data)-2):
            x = data[i+2].split("\t")
            for j in range(len(x)):
                if j != len(x) - 1:
                    dataset[i][j] = float(x[j])
                else:
                    label[i] = float(x[j][:-1])
    else:
        data = f.readlines()
        n_data = int(len(data)/3)
        dataset = np.zeros((n_data, 2))
        label = np.zeros((n_data, 2))
        j = 0
        count = 0
        for i in range(len(data)):
            if(j == 1):
                dataset[count][0] = float(data[i].split()[0])
                dataset[count][1] = float(data[i].split()[1])
            if(j == 2):
                label[count][0] = int(data[i].split()[0])
                label[count][1] = int(data[i].split()[1])
                count = count + 1
                j = -1
            j += 1
    return dataset, label

def norm(input_mathix):
    data = input_mathix.copy()
    return ( data-data.min() )/( data.max()-data.min())

def prepare(dataset,label ,percent, epoch):
    data = dataset.copy()
    la = label.copy()
    train_data = []
    test_data = []
    data_with_label =[]
    for i in range(len(data)):
        dataTemp=[]
        dataTemp.append(data[i])
        dataTemp.append(la[i])
        data_with_label.append(dataTemp)
    random.shuffle(data_with_label)
    for i in range(len(data_with_label)):
        if((i%percent) == ((epoch-1)%percent)):
            test_data.append(data_with_label[i])
        else:
            train_data.append(data_with_label[i])
    return train_data,test_data

# def makeNN(input, output, hidden):



