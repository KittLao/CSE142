from DataInstance.Date import Date

class DataInstance():

	def __init__(self, values):
		self.stars = values[0]
		self.useful = values[1]
		self.funny = values[2]
		self.cool = values[3]
		self.text = values[4]
		self.date = Date(values[5])
		# print("stars: ", self.stars)
		# print("useful: ", self.useful)
		# print("funny: ", self.funny)
		# print("cool: ", self.cool)
		# print("text: " + self.text)