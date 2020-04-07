import sys, getopt, csv, math

"""
Open csvfile and read all label and features into the data list.
Converts all the data into int type while ignoring the 0th
element because it is the header for the data.

Data structure for data: [(label, [f1, f2, f3, f4])]
"""
def getData(filename):
	data = []
	with open (filename) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		data = [(row[0], [row[i] for i in range(1, 5)]) for row in readCSV]
	return [(int(label), [int(feat[i]) for i in range(4)]) for label, feat in data[1::]]

"""
sum(|x_i - y|) for i in features.
"""
def L1Distance(features, test_instance, n):
	return sum([abs(features[i] - test_instance[i]) for i in range(n)])

"""
sqrt(sum(|x_i - y|)) for i in features.
Basically euclidian distance for n-dimension
"""
def L2Distance(features, test_instance, n):
	return math.sqrt(sum([math.pow(features[i] - test_instance[i], 2) for i in range(n)]))

"""
max(|x_i - y|) for i in features.
"""
def maxNorm(features, test_instance, n):
	return max([abs(features[i] - test_instance[i]) for i in range(n)])

"""
Given the training data, k-value, test instnace, distance measure used, 
compute the k closest points from the test intance in the training data.

The function computes all the distance from all possible points to the
test instance, and sorts them by he distance

Data structure for distances: [[distance, label]]

After sorting them, copmute the summation of the first k labels. If the
get_sign option is true, then it returns just the sign. Otherwise, returns
the list of k labels.
"""
def predictKNN(data, k, test_instance, method, get_sign):
	distances = [[method(features, test_instance, 4), label] for label, features in data]
	distances.sort()
	if get_sign: return (lambda x : int(x / abs(x)))(sum([distances[i][1] for i in range(k)]))
	return [distances[i][1] for i in range(k)]


"""
The following funcitons below are for parts 2 to 7 of the problem.
"""
def problem2(test_file, train_file):
	print("Problem 2")
	test_instance = test_file[0][1]
	train_instance = train_file[0][1]
	label = L1Distance(train_instance, test_instance, 4)
	print(label)

def problem3(test_file, train_file):
	print("Problem 3")
	test_instance = test_file[0][1]
	train_instance = train_file[0][1]
	label = L2Distance(train_instance, test_instance, 4)
	print(label)

def problem4(test_file, train_file):
	print("Problem 4")
	test_instance = test_file[0][1]
	train_instance = train_file[0][1]
	label = maxNorm(train_instance, test_instance, 4)
	print(label)

def problem5(test_file, train_file):
	print("Problem 5")
	test_instance = test_file[0][1]
	label = predictKNN(train_file, 5, test_instance, L2Distance, False)
	print(label)

def problem6(test_file, train_file):
	print("Problem 6")
	k_values = [1, 3, 5, 720]
	for k in k_values:
		print("K value: ", k)
		labels = [(i + 1, predictKNN(train_file, k, test_file[i][1], L2Distance, True)) for i in range(10)]
		print(labels)

def problem7(test_file, train_file):
	print("Problem 7")
	for i in range(10):
		print("Instance: ", i + 1)
		label = predictKNN(train_file, 9, test_file[i][1], L1Distance, True)
		print("L1: ", label)
		label = predictKNN(train_file, 9, test_file[i][1], L2Distance, True)
		print("L2: ", label)
		label = predictKNN(train_file, 9, test_file[i][1], maxNorm, True)
		print("Linf: ", label)


if __name__ == "__main__":
	test_file = getData("knn_test.csv")
	train_file = getData("knn_train.csv")

	methods = {"L1" : L1Distance, "L2" : L2Distance, "Linf" : maxNorm}
	k, method, method_ = 0, None, ""

	opts, args = getopt.getopt(sys.argv[1::], "", ["method=", "K="])
	for opt, arg in opts:
		if opt == ("--K"):
			k = int(arg)
		elif opt == ("--method"):
			method_ = arg
			method = methods[method_]

	print("K value: ", k, "method: ", method_)
	for i in range(10):
		label = predictKNN(train_file, k, test_file[i][1], method, True)
		print("Instance: ", i + 1, "Label: ", label)

	problem2(test_file, train_file)
	problem3(test_file, train_file)
	problem4(test_file, train_file)
	problem5(test_file, train_file)
	problem6(test_file, train_file)
	problem7(test_file, train_file)












