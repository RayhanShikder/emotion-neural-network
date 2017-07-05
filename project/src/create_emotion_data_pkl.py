from PIL import Image
from numpy import genfromtxt
import gzip, cPickle
from glob import glob
import numpy as np
import pandas as pd
Data, y = dir_to_dataset("thesis_data.txt","trainLabels.csv")
# Data and labels are read 

train_set_x = Data[:2093]
val_set_x = Data[2094:4187]
test_set_x = Data[4188:6281]
train_set_y = y[:2093]
val_set_y = y[2094:4187]
test_set_y = y[4188:6281]
# Divided dataset into 3 parts. I had 6281 images.

train_set = train_set_x, train_set_y
val_set = val_set_x, val_set_y
test_set = test_set_x, val_set_y

dataset = [train_set, val_set, test_set]

f = gzip.open('file.pkl.gz','wb')
cPickle.dump(dataset, f, protocol=2)
f.close()

def dir_to_dataset(glob_files, loc_train_labels=""):
    print("Gonna process:\n\t %s"%glob_files)
    dataset = []
    labels = []
    reader_data = pd.read_csv(glob_files, sep=" ", header = None)
    data = pd.DataFrame(reader_data)
    for row in data.iterrows()
    	dataset.append(row[1])
    	lables.append(row[1][21])
   
    return np.array(dataset), np.array(lables)
    