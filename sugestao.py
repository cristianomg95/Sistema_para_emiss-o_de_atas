from participanteReuniao import ParticipanteReuniao
from banco import DataBase
from ata import Ata

class Sugestao:

	def __init__(self):
		self.sugestao = {}
		self.data = ''
		self.descricao = ''
		self.dbSugestoes = DataBase('database/sugestoes.pickle')
		self.participanteReuniao = ParticipanteReuniao()
		self.atas = DataBase('database/atas.pickle')
		self.ata = Ata()


	def emitirSugestao(self):
		while True:
			participante = self.participanteReuniao.selecionarParticipante()
			if isinstance(participante, ParticipanteReuniao):
				self.participanteReuniao = participante
				break
			else:
				print('digite um participante cadastrado!!!')
		while True:
			varAta = input('Digite o titulo da Ata em que deseja fazer sugetão: ')
			try:
				for i in self.atas.loadObject():
					if varAta == i.exibir()['titulo']:
						self.ata = i.exibir()['titulo']
						a = True
						break
					else: continue
				if a == True:
					break
				else: print('Nenhuma ata cadastrada!!!')
			except:
				print('Nenhuma ata com esse titulo existe digite outro Titulo!!!')
		self.data = input("Data da sugestão: ")
		self.descricao = input("Digite sua sugestão: ")
		self.sugestao = {'participante que sugeriu': self.participanteReuniao.exibir()['nome'], 'titulo da ata':self.ata, 'data de sugestão': self.data, 'descrição': self.descricao}
		print('Sugestão Cadastrada!!!')
	

	def selecionarSugestao(self):
		num = 1
		titulo = input('Digite o Titulo da Ata que deseja selecionar as Sugestões: ')
		print()
		try:
			for i in self.dbSugestoes.loadObject():
				if titulo == i.sugestao['titulo da ata']:
					print(f'Sugestão {num}')
					num += 1
					for j,k in i.sugestao.items():
						print('{}: {}'.format(j, k))
					print()
				else: continue
		except:
			print('Nenhuma sugestão para essa data encontrada!!!')

		
