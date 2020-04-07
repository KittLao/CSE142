from DataInstance.DataList import DataList
from DataInstance.DataInstance import DataInstance
from LogisticRegression import LRPerformance
from random import shuffle

from sklearn.feature_extraction.text import TfidfVectorizer

import json

"""
utility.py contains tools like reading training data from a json file,
redaing testing data from json file, argmax, etc...
"""

DATA_SIZE = 334295
NUM_FEATURES = 6
NUM_CLASSES = 5
ONE_STAR = 49031
TWO_STAR = 27028
THREE_STAR = 36987
FOUR_STAR = 73604
FIVE_STAR = 147645
CLASSES = [1.0, 2.0, 3.0, 4.0, 5.0]

"""
Reads data from a json file and returns is in a list of type DataInstance.
DataInstance is particular to the features in the files only for this
project, which is a yelp review
"""

"""
80/20
Train range: [1, 267436]
Test range: [267437, 334295]
"""

def readDataSplit80_20(filename):
	data = {}
	train_instances = DataList(NUM_CLASSES)
	test_instances = DataList(NUM_CLASSES)
	with open(filename) as json_file:
		data = json.load(json_file)
		x = 0
		for instance in data:
			if x <= 267436:
				train_instances.append(DataInstance(list(instance.values())))
			else:
				test_instances.append(DataInstance(list(instance.values())))
			x = x + 1
	return (train_instances, test_instances)

def readDataNoSplit(filename):
	data = {}
	train_instances = DataList(NUM_CLASSES)
	with open(filename) as json_file:
		data = json.load(json_file)
		x = 0
		for instance in data:
			train_instances.append(DataInstance(list(instance.values())))
	return (train_instances, train_instances)

def readTainData(filename):
	data = {}
	instances = DataList(NUM_CLASSES)
	with open(filename) as json_file:
		data = json.load(json_file)
		x = 0
		for instance in data:
			if x != 267436:
				instances.append(DataInstance(list(instance.values())))
			else:
				break
			x = x + 1
	return instances

def readTestData(filename):
	data = {}
	instances = DataList(NUM_CLASSES)
	# with open(filename) as json_file:
	# 	data = json.load(json_file)
	# 	for instance in data:
	# 		instances.append(DataInstance([0.0] + list(instance.values())))
	# return instances
	with open(filename) as json_file:
		data = json.load(json_file)
		x = 0
		for instance in data:
			if x < 267436:
				pass
			elif x <= 334295:
				instances.append(DataInstance(list(instance.values())))
			else:
				break
			x = x + 1
	return instances

def argmax(l1, l2):
	l3 = list(zip(l1, l2))
	best = (-1, -99999)
	for t in l3:
		if t[1] > best[1]:
			best = t
	return best[0]

def printPerformance(performance):
	print("--------------------------------")
	print("Accuracy: ", performance.accuracy)
	print("TP: ", performance.TP)
	print("FP: ", performance.FP)
	print("FN: ", performance.FN)
	print("TN: ", performance.TN)
	print("--------------------------------")


WORD_BANK = ["delicious", "excellent", "terrible", "disgusting"]
SIZE_OF_WB = len(WORD_BANK)

def getTermFrequency(text):
	text = text.lower()
	tokenized_text = text.split()
	feature_frequency = {word : 0 for word in WORD_BANK}
	for word in tokenized_text:
		if word in WORD_BANK:
			feature_frequency[word] += 1
	return list(feature_frequency.values())


def subSampleData(data):
	"""
	Input is a DataLists
	"""
	numleastCommonClass = min([len(dataSet) for dataSet in data.dataSetAtClass])
	newDataSet = []
	for i in range(0, len(data.dataSetAtClass)):
		data.dataSetAtClass[i] = data.dataSetAtClass[i][0:numleastCommonClass]
		newDataSet += data.dataSetAtClass[i]
	data.dataSet = shuffle(newDataSet)
	return data
















