class Date():

	def __init__(self, date):
		day, time = date.split(" ")
		year, month, day = day.split("-")
		self.year, self.month, self.day = int(year), int(month), int(day)
		hour, minute, second = time.split(":")
		self.hour, self.minute, self.second = int(hour), int(minute), int(second)
		# print("year: ", self.year)
		# print("month: ", self.month)
		# print("day: ", self.day)
		# print("hour: ", self.hour)
		# print("minute: ", self.minute)
		# print("second: ", self.second)