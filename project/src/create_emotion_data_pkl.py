# from PIL import Image
from numpy import genfromtxt
import gzip, cPickle
from glob import glob
import numpy as np
import pandas as pd
import random

def dir_to_dataset(glob_files):
    print("Gonna process:\n\t %s"%glob_files)
    dataset = []
    labels = []
    reader_data = pd.read_csv(glob_files, sep=" ", header = None)
    data_old = pd.DataFrame(reader_data)
    data = np.array(data_old)
    data = random.shuffle(data)
    data = np.array(data_old)
    for row in data:
    	dataset.append(row[:21])
    	labels.append(row[21])
   
    return np.array(dataset), np.array(labels)

def create_pkl_file():
	Data, y = dir_to_dataset("thesis_data.txt")
	# Data and labels are read 

	train_set_x = Data[:2000]
	val_set_x = Data[2001:4000]
	test_set_x = Data[4001:5130]
	train_set_y = y[:2000]
	val_set_y = y[2001:4000]
	test_set_y = y[4001:5130]
	# Divided dataset into 3 parts. I had 6281 images.

	train_set = train_set_x, train_set_y
	val_set = val_set_x, val_set_y
	test_set = test_set_x, val_set_y

	dataset = [train_set, val_set, test_set]

	f = gzip.open('../data/file.pkl.gz','wb')
	cPickle.dump(dataset, f, protocol=2)
	f.close()


    