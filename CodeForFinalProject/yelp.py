from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import json
import csv
import time

def readTrainData(filename):
	instances = {float(i) : [] for i in range(1, 6)}
	with open(filename) as json_file:
		data = json.load(json_file)
		for review in data:
			stars = review['stars']
			text = review['text']
			instances[stars].append(text)
	print("Train data successfully read")
	return instances

def readTestData(filename):
	instances = []
	with open(filename) as json_file:
		data = json.load(json_file)
		for review in data:
			instances.append(review['text'])
	print("Test data successfully read")
	return instances

def writeData(filename, predictions):
	with open(filename, 'w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['Predictions'])
		for pred in predictions:
			writer.writerow([pred])


def subSampleData(data):
	leastCommonLabel = min([len(texts) for texts in list(data.values())])
	for label in data:
		data[label] = data[label][0:leastCommonLabel]
	print("Sub sampling successfull.")
	print("leastCommonLabel: ", leastCommonLabel)
	return data

def getText(data):
	texts = []
	for text in data.values():
		texts += text
	return texts

def getStars(data, label = 1.0):
	return [] if label > 5.0 else [label for text in data[label]] + getStars(data, label + 1.0)


"""
In the vectorizer, stopwords (the, as, like, ... etc).
"""
def getTFIDFVector(train_data, test_data):
	texts = getText(train_data)
	train_len = len(texts)
	texts += test_data
	start = time.time()
	vectorizer = TfidfVectorizer(ngram_range = (1, 2))
	TFIDVectors = vectorizer.fit_transform(texts)
	end = time.time()
	print("Vectorization successfull.")
	print("Time taken: ", end - start)
	return TFIDVectors[:train_len], TFIDVectors[train_len:]

def getTrainingData(TFIDVectors, labels):
	print("Training and testing data successfull.")
	return train_test_split(TFIDVectors, labels, test_size = 0.0, random_state = 42)

def classify(train_data, train_label, test_data):
	# classifier = LinearSVC()
	# classifier = DecisionTreeClassifier()
	classifier = LogisticRegression()
	start = time.time()
	classifier.fit(train_data, train_label)
	predictions = classifier.predict(test_data)
	end = time.time()
	print("Classification successfull")
	print("Time taken: ", end - start)
	return predictions


"""
Precision: Out of all the instances that was predicted positive, which ones
were actually positive.

Recall: Out of all the instances that were actually positive, which ones
were actually predicted positive.

F1-Measure: 

Confusion Matrix:
(<actual>, <predicted>)

(1.0, 1.0) | (2.0, 1.0) | (3.0, 1.0) | (4.0, 1.0) | (5.0, 1.0)
----------------------------------------------------------------
(1.0, 2.0) | (2.0, 2.0) | (3.0, 2.0) | (4.0, 2.0) | (5.0, 2.0)
----------------------------------------------------------------
(1.0, 3.0) | (2.0, 3.0) | (3.0, 3.0) | (4.0, 3.0) | (5.0, 3.0)
----------------------------------------------------------------
(1.0, 4.0) | (2.0, 4.0) | (3.0, 4.0) | (4.0, 4.0) | (5.0, 4.0)
----------------------------------------------------------------
(1.0, 5.0) | (2.0, 5.0) | (3.0, 5.0) | (4.0, 5.0) | (5.0, 5.0)

"""
def displayPerformance(test_label, predictions):
	print("--------------------------------------------------------------------------------------------------------------------------------")
	accuracy = accuracy_score(test_label, predictions)
	print("Accuracy: ", accuracy)
	print("Classification report: ")
	print(classification_report(test_label, predictions))
	print("Confusion matrix: ")
	print(confusion_matrix(test_label, predictions))
	print("--------------------------------------------------------------------------------------------------------------------------------")

def main():
	trainData = readTrainData("data_train.json")
	testData = readTestData("data_test_wo_label.json")
	trainData = subSampleData(trainData)
	train_data, test_data = getTFIDFVector(trainData, testData)
	labels = getStars(trainData)
	# train_data, test_data, train_label, test_label = getTrainingData(TFIDVectors, labels)
	train_label = labels
	"""
	80 - 20 split
	predictions = classify(train_data, train_label, test_data)
	displayPerformance(test_label, predictions)
	"""
	"""
	Train accuracy.
	predictions = classify(train_data, train_label, train_data)
	displayPerformance(train_label, predictions)
	"""
	"""
	Making predictions. Labels for test file not given.
	"""
	predictions = classify(train_data, train_label, test_data)
	writeData("predictions.csv", predictions)

main()
