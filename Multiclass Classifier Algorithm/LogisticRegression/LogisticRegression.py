from LogisticRegression.LRInstance import LRInstance
from LogisticRegression.LRPerformance import LRPerformance
from math import pow, log

class LogisticRegression():

	def __init__(self, n):
		self.ITERATIONS = 50
		self.rate = 0.01
		self.weights = [0 for i in range(0, n)]
		self.likelihood = [0 for i in range(0, self.ITERATIONS)]

	def dotProduct(self, x, y):
		return sum([x_ * y_ for x_, y_ in list(zip(x, y))])

	def weightsL2Norm(self):
		return self.dotProduct(self.weights, self.weights)

	def sigmoid(self, z):
		e = 2.718281828
		return 1 / (1 + pow(e, -z))

	def probPredict1(self, x):
		return self.sigmoid(self.dotProduct(self.weights, x))

	def predict(self, x):
		# changed from >= 1 to 0.5
		return 1 if self.probPredict1(x) >= 0.5 else 0

	def getPerformance(self, instances):
		acc = 0
		p_pos, r_pos, f_pos = 0, 0, 0
		p_neg, r_neg, f_neg = 0, 0, 0
		TP, FP, FN, TN = 0, 0, 0, 0
		for instance in instances:
			predictLabel = self.predict(instance.data)
			actualLabel = instance.label
			if actualLabel == 1 and predictLabel == 1:
				TP += 1
			elif actualLabel == 1 and predictLabel == 0:
				FN += 1
			elif actualLabel == 0 and predictLabel == 1:
				FP += 1
			else:
				TN += 1
		return LRPerformance(TP, FP, FN, TN)


	def train(self, instances):
		"""
		instances is list of LRInstances
		"""
		for k in range(0, self.ITERATIONS):
			lik = 0
			for instance in instances:
				actualLabel = instance.label
				data = instance.data
				predictLabel = self.probPredict1(data)
				error = actualLabel - predictLabel
				for i in range(0, len(self.weights)):
					x_i = data[i]
					update = self.rate * x_i * error
					self.weights[i] += update
				e = 2.718281828
				dotProd = self.dotProduct(self.weights, data)
				lik_l = actualLabel * dotProd - log(1 + pow(e, dotProd)) / log(e)
				lik += lik_l
				self.likelihood[k] = lik


















