import os 
from natsort import natsorted 
import numpy as np

folders = ["Czech/"]
path = "Augmented_dataset/"
path2 = "images/"
Names = list()
Names2 = list()


for fold in folders:
	for fo in natsorted(os.listdir(fold+path)):
		for img in natsorted(os.listdir(fold+path+fo)):
			if img.endswith(".xml"):
				Names.append("../train/" + fold + path + fo + "/" + img)
			if img.endswith(".jpg"):
				Names2.append("../train/" + fold + path + fo + "/" + img)

for fold in folders:
	# for fo in natsorted(os.listdir(fold+path)):
	for img in natsorted(os.listdir(fold+path2)):
		if img.endswith(".xml"):
			Names.append("../train/" + fold + path2+ img)
		if img.endswith(".jpg"):
			Names2.append("../train/" + fold + path2 + img)

np.savetxt("train_aug_annotations.txt",Names,fmt = '%s')
np.savetxt("train_aug.txt",Names2,fmt = '%s')