import numpy as np
import function

percent = 10
epoch = 10
file1 = "Flood_dataset.txt"
file2 = "cross.pat"
dataset,label = function.readfile(file1)
dataset_norm = function.norm(dataset)
label_norm = function.norm(label)
train_data,test_data = function.prepare(dataset, label, percent, epoch)



