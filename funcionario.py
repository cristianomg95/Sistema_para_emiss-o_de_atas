from participanteReuniao import ParticipanteReuniao

class Funcionario(ParticipanteReuniao):

	def __init__(self):
		self._nome = ''
		self._matricula = ''
		self._sexo = ''
		self._nascimento = ''
		self._email = ''
		super().__init__()

	def incluir(self):
		self._nome = input('Qual nome do participante: ')
		self._matricula = input('Qual a matricula do participante: ')
		self._sexo = input('Qual o sexo do participante: ')
		self._nascimento = input('Qual a data de nascimento do participante [DD/MM/YYYY]:')
		self._email = input('Qual email do participante: ')
		self._ParticipanteReuniao = {'nome': self._nome,'matricula': self._matricula,
									 'sexo': self._sexo, 'nascimento': self._nascimento, 'email': self._email}
		print('Cadastro realizado com sucesso!!!')

	def selecionarParticipante(self):
		participante = input('Qual o nome do Funcionario: ')
		try:
			for i in self.carregar():
				if i.exibir()['nome'] == participante:
					return i
				else: continue
			print('nada encontrado!!!')
		except:
			print('Nenhum funcionario cadastrado!!!')
