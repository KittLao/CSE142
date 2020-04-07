from LogisticRegression.LogisticRegression import LogisticRegression
from LogisticRegression.LRInstance import LRInstance
from LogisticRegression.LRPerformance import LRPerformance
from DataInstance.DataList import DataList
from DataInstance.DataInstance import DataInstance
from utility import argmax, printPerformance, getTermFrequency

from textblob import TextBlob
from random import shuffle

import json

class AVA():

	def __init__(self, numFeatures, classes):
		self.numFeatures = numFeatures
		self.classes = classes
		self.numClasses = len(classes)

		self.matches = {}
		self.predictions = []

	def convertToLRInstance(self, instances, isPos):
		LRData = []
		label = 1 if isPos else 0
		for instance in instances:
			"""
			Build data using attributes in DataInstance
			"""
			data = [instance.useful, \
					instance.funny, \
					instance.cool]
			"""
			Get the value of text
			"""
			blob = TextBlob(instance.text)
			polarity = blob.sentiment.polarity
			subjectivity = blob.sentiment.subjectivity

			data += [polarity, subjectivity]

			"""
			Bias for logistic regression
			"""
			data += [1]
			"""
			Convert data and label from DataInstance format to
			LRInstance format.
			"""
			LRData.append(LRInstance(label, data))
		"""
		LRData is a list of LRInstance's
		"""
		return LRData

	def AVAPredict(self, LRMatch, LR_test_instance):
		predict = 1 if self.matches[LRMatch].predict(LR_test_instance.data) == 1 else -1
		return predict

	def train(self, train_data):
		"""
		Classes is list of labels
		data is DataList
		"""
		print("AVA training")
		numClasses = self.numClasses
		# ************************************************************************
		LRInstances = []
		count = 0
		# ************************************************************************
		for i in range(0, numClasses - 1):
			"""
			Player 1 is positive lable
			"""
			if len(LRInstances) == 0:
				p1 = train_data.dataSetAtClass[i]
				p1_ = self.convertToLRInstance(p1, True)
			else:
				p1_ = LRInstances[i]
			if count < 6:
				LRInstances.append(p1_)
				count += 1
			for j in range(i + 1, numClasses):
				print("Match: ", i + 1, " vs ", j + 1)
				"""
				Player 2 is negative label
				"""
				if len(LRInstances) < 6:
					p2 = train_data.dataSetAtClass[j]
					p2_ = self.convertToLRInstance(p2, False)
				else:
					p2_ = LRInstances[j]
				if count < 6:
					LRInstances.append(p2_)
					count += 1
				"""
				Use binary classifier to train data
				"""
				LRMatch = LogisticRegression(self.numFeatures)
				# ************************************************************************
				# basically just overwriting, since label might not be correct from
				# this basic caching method.
				self.gimmeALabel(p1_, 1)
				self.gimmeALabel(p2_, 0)
				# ************************************************************************
				match = p1_ + p2_
				shuffle(match)
				LRMatch.train(match)
				# printPerformance(LRMatch.getPerformance(match))
				self.matches[(i, j)] = LRMatch

	def test_helper(self, test_data):
		k = self.numClasses
		scores = [0 for i in range(k)]
		for i in range(k):
			for j in range(i + 1, k):
				predict = self.AVAPredict((i, j), test_data)
				scores[i] += predict
				scores[j] -= predict
		return argmax(self.classes, scores)

	def test(self, test_data):
		LR_test_data = self.convertToLRInstance(test_data.dataSet, True)
		for instance in LR_test_data:
			prediction = self.test_helper(instance)
			self.predictions.append(prediction)

# ************************************************************************
	def gimmeALabel(self, instances, label):
		for instance in instances:
			instance.label = label













