class uber_cab:
	def __init__(self,cabType,isShared,cabDescription,capacity):
		self.cabType = cabType
		self.isShared = isShared
		self.cabDescription = cabDescription
		self.capacity = capacity

	def getDetails(self):
		return "cab type: "+ self.cabType + " Shared: "+ self.isShared + " capacity: "+str(self.capacity)