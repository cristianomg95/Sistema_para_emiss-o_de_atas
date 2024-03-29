from funcionario import Funcionario
from banco import DataBase
class Ata:
	def __init__(self):
		self.__titulo = ''
		self.__dataEmissao = ''
		self.__inicio = ''
		self.__termino = ''
		self.__pauta = ''
		self.__descricao = ''
		self.__palavraChave = []
		self.__tipo = ''
		self.__estatus = ''
		self.__funcionario = Funcionario()
		self.__participanteCadastrados = DataBase('database/participantes.pickle')
		self.__participantesAta = []
		self.__ata = {}
		self.__dbAtas = DataBase('database/atas.pickle')


	
	def emitirAta(self):
		while True:
			funcionario = self.__funcionario.selecionarParticipante()
			if isinstance(funcionario, Funcionario):
				self.__funcionario = funcionario
				break
			else:
				print('Cadastre um funcionario valido!!')
		self.__titulo = input("Titulo da Reunião: ")
		self.__pauta = input('Pauta: ')
		self.__inicio = input('Inicio da reunião: ')
		self.__termino = input('Termino da reunião: ')
		self.__descricao = input('Descreva a Reunião: ')
		while True:
			palavraChave= input('Palavra Chave [digite SAIR para finalizar as palavras chaves]:  ').lower()
			if palavraChave == 'sair':
				if len(self.__palavraChave) >= 1:
					break
				else:
					print('Cadastre pelo menos uma palavra chave')
			elif palavraChave != '':
				self.__palavraChave.append(palavraChave)
			else:
				print('Digite alguma palavra chave')

		self.__estatus = input("Estatus da reunião: ")
		varQuant = 0
		while varQuant < 10:
			varParticipante = input('Digite o nome de um participante para cadastrar na Ata [digite false para finalizar a lista de participantes]: ')
			if varParticipante == 'false':
				break
			else:
				for i in self.__participanteCadastrados.loadObject():
					if i.exibir()['nome'] == varParticipante:
						if i.exibir()['nome'] not in self.__participantesAta:
							self.__participantesAta.append(i.exibir()['nome'])
							varQuant +=1
							break
						else: 
							print("Participante já cadastrado na ata!!!")
					else:
						print('Esse nome não está na lista de participantes cadastrados, digite o nome de outro participante!!!')
			if varQuant == 10: print('Limite de participantes excedido !!!')
		self.__ata = {'funcionario': self.__funcionario.exibir()['nome'], 'titulo': self.__titulo,
					'pauta': self.__pauta,'inicio da reunião': self.__inicio,
					'termino da reunião': self.__termino, 'descrição': self.__descricao,
					'palavra chave': self.__palavraChave,'estatus': self.__estatus,
					'participantes': self.__participantesAta}
		print('Ata cadastrada!!!')


	def exibir(self):
		return self.__ata

	def atualizar(self):
		ata = input('Informe o titulo da ata que deseja atualizar: ')
		try:
			a = False
			for num, i in enumerate(self.__dbAtas.loadObject()):
				newList = self.__dbAtas.loadObject()
				if i.exibir()['titulo'] == ata:
					opc = input('O que você quer atualizar [titulo, pauta, descrição, palavra chave, estatus]: ')
					while True:
						if opc == 'titulo':
							titulo = input('Digite novo titulo: ')
							i.exibir()['titulo'] = titulo
							newList[num] = i
							self.__dbAtas.atualizar(newList)
							a = True
							break
						elif opc == 'pauta':
							pauta = input('Digite a nova pauta: ')
							i.exibir()['pauta'] = pauta
							newList[num] = i
							self.__dbAtas.atualizar(newList)
							a = True
							break
						elif opc == 'descrição':
							descricao = input('Digite a nova descrição: ')
							i.exibir()['descrição'] = descricao
							newList[num] = i
							self.__dbAtas.atualizar(newList)
							a = True
							break
						elif opc == 'palavra chave':
							palavraChave = input('Digite a nova palavra chave: ')
							i.exibir()['palavra chave'] = palavraChave
							newList[num] = i
							self.__dbAtas.atualizar(newList)
							a = True
							break
						elif opc == 'estatus':
							estatus = input('Digite o novo estatus: ')
							i.exibir()['estatus'] = estatus
							newList[num] = i
							self.__dbAtas.atualizar(newList)
							a = True
							break
						else:
							print('Opção invalida')
				else:
					continue
				if a:
					break
			if not a:
				print('nada encontrado')
		except:
			print('Nenhuma ata encontrada com esse titulo !!!')

