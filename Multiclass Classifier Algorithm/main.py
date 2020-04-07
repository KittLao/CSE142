from AVA import AVA
from utility import readDataSplit80_20, readDataNoSplit, CLASSES, NUM_FEATURES

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def printPerformance(test_labels, predictions):
	print("----------------------------------------------------------------")
	print("Accuracy:", accuracy_score(test_labels, predictions))
	print("Classification Report:")
	print(classification_report(test_labels, predictions))
	print("Confusion Matrix:")
	print(confusion_matrix(test_labels, predictions))
	print("----------------------------------------------------------------")


def split80_20():
	train_data, test_data = readDataSplit80_20("data_train.json")
	truth = []
	for instance in test_data.dataSet:
		truth.append(instance.stars)
	classification = AVA(NUM_FEATURES, CLASSES)
	classification.train(train_data)
	classification.test(test_data)

	printPerformance(truth, classification.predictions)

def split100_0():
	train_data, test_data = readDataNoSplit("data_train.json")
	truth = []
	for instance in test_data.dataSet:
		truth.append(instance.stars)
	classification = AVA(NUM_FEATURES, CLASSES)
	classification.train(train_data)
	classification.test(test_data)

	printPerformance(truth, classification.predictions)

def main():
	# split80_20()
	split100_0()

main()








