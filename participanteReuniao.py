from banco import DataBase

class ParticipanteReuniao:
	def __init__(self):
		self._ParticipanteReuniao = {}
		self._db = DataBase('database/participantes.pickle')

	def incluir(self):
		pass
		
	def exibir(self):
		return self._ParticipanteReuniao

	def carregar(self):
		return self._db.loadObject()
	
	def selecionarParticipante(self):
		participante = input('Qual o nome do participante: ')
		try:
			for i in self.carregar():
				if i.exibir()['nome'] == participante:
					return i
				else: continue
			print('nada encontrado')
			return None
		except:
			print('Nenhum participante cadastrado!!!')
			return None