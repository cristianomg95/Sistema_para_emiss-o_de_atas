import pickle as pk

class DataBase:
	
	def __init__(self, archive):
		self.archive = archive

	def loadObject(self):
		try:
			obj = pk.load(open(self.archive, 'rb'))
		except:
			obj = []
			pk.dump(obj, open(self.archive, 'wb'))
		return obj
			
	def saveObject(self, obj):
		listObj = self.loadObject()
		listObj.append(obj)
		pk.dump(listObj, open(self.archive, "wb"))

	def atualizar(self,newlist):
		pk.dump(newlist, open(self.archive, 'wb'))




