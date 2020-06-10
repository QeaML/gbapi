from gbapi.api.stats import Stats
from gbapi.api.structured_data import StructuredData

class Question(StructuredData):
	def __init__(self, stats, sdata):
		super(Question, self).__init__(sdata)
		self.stats = Stats(stats)