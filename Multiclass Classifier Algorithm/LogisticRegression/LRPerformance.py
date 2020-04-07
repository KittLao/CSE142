class LRPerformance():

	def __init__(self, TP, FP, FN, TN):

		self.TP = TP
		self.FP = FP
		self.FN = FN
		self.TN = TN

		self.accuracy = (TP + TN) / (TP + FP + FN + TN)

		self.p_precision = TP / (FP + TP)
		self.p_recall = TP / (FP + FN)
		self.p_f_measure = (2 * self.p_precision * self.p_recall) / (self.p_precision + self.p_recall)

		self.n_precision = TN / (FN + TN)
		self.n_recall = TN / (FP + TN)
		self.n_f_measure = (2 * self.n_precision * self.n_recall) / (self.n_precision + self.n_recall)