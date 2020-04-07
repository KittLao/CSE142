from DataInstance import DataInstance

class DataList():

	def __init__(self, classes):
		self.dataSet = []
		self.dataSetAtClass = [[] for i in range(classes)]


	def append(self, instance):
		self.dataSet.append(instance)
		class_ = instance.stars
		if class_ == 1.0: 
			self.dataSetAtClass[0].append(instance)
		elif class_ == 2.0:
			self.dataSetAtClass[1].append(instance)
		elif class_ == 3.0:
			self.dataSetAtClass[2].append(instance)
		elif class_ == 4.0:
			self.dataSetAtClass[3].append(instance)
		else:
			self.dataSetAtClass[4].append(instance)




















