from participanteReuniao import ParticipanteReuniao

class ParticipanteExterno(ParticipanteReuniao):
	
	def __init__(self):
		self.nome = ''
		self.empresa = ''
		self.email = ''
		super().__init__()

	def incluir(self):
		self.nome = input('Qual nome do participante: ')
		self.empresa = input('Qual nome da empresa que o participante trabalha: ')
		self.email = input('Qual email do participante: ')
		self._ParticipanteReuniao = {'nome':self.nome, 'empresa': self.empresa, 'email':self.email}
		print('Cadastro realizado com sucesso!!!')

