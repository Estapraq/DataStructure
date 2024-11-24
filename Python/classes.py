class car: 
	def __init__(self, type: str, price: str) -> None:
		self.type=type
		self.price=price

	def printType(self):
		print(self.type)

	def getType(self):
		print(self.printType())


bmw: car= car("fancy", 100)

bmw.printType()
bmw.getType()