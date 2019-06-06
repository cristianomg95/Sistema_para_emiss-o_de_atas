from banco import DataBase
from ata import Ata
from funcionario import Funcionario
from participanteExterno import ParticipanteExterno
from sugestao import Sugestao
import utility as ut


class Menu:

	def __init__(self):
		self.__ata = Ata()
		self.__funcionario = Funcionario()
		self.__participanteExterno = ParticipanteExterno()
		self.__sugestao = Sugestao()
		self.__dbAta = DataBase('database/atas.pickle')
		self.__dbSugestao = DataBase('database/sugestoes.pickle')
		self.__dbParticipanteReuniao = DataBase('database/participantes.pickle')

	def menuInicial(self):
		print(("""1 - Cadastrar Participante Funcionario
2 - Cadastrar Participante Externo
3 - Emitir Ata
4 - Fazer Sugestão
5 - Exibir Atas
6 - Exibir Participantes
7 - Exibir Funcionarios
8 - Exibir Participantes Externos
9 - Exibir Sugestões"""))
		while True:
			opc = input("""Escolha uma opção: """)
			if opc == '1':
				self.__funcionario.incluir()
				self.__dbParticipanteReuniao.saveObject(self.__funcionario)
				break
			elif opc == '2':
				self.__participanteExterno.incluir()
				self.__dbParticipanteReuniao.saveObject(self.__participanteExterno)
				break
			elif opc == '3':
				self.__ata.emitirAta()
				self.__dbAta.saveObject(self.__ata)
				break
			elif opc == '4':
				self.__sugestao.emitirSugestao()
				self.__dbSugestao.saveObject(self.__sugestao)
				break
			elif opc == '5':
				ut.exibirAtas(lambda: self.__dbAta.loadObject())
				break
			elif opc == '6':
				ut.exibirParticipantes(lambda: self.__dbParticipanteReuniao.loadObject(), 'global')
				break
			elif opc == '7':
				ut.exibirParticipantes(lambda: self.__dbParticipanteReuniao.loadObject(), 'funcionario')
				break
			elif opc == '8':
				ut.exibirParticipantes(lambda: self.__dbParticipanteReuniao.loadObject(), 'externo')
				break
			elif opc == '9':
				self.__sugestao.selecionarSugestao()
				break			
			else: print("Escolha uma opção Valida !!!")	
