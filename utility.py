from funcionario import Funcionario
from participanteExterno import ParticipanteExterno 
def exibirAtas(dbAtas): # dbAtas == lambda: dbAtas.loadobject()
	print()
	quantAtas = 1
	try:
		for i in dbAtas(): 
			print('Ata Nº ',quantAtas)
			for item, value in i.exibir().items(): 
				print(item, ': ', value)
			print()
			quantAtas += 1
	except:
		print('Nenhuma Ata cadastrada no sistema!!!')

def exibirParticipantes(dbParticipante, tipo): # dbParticipante == lambda: dbParticipante.loadobject()
	print()
	try:
		encontrado = False
		if tipo == "global":
			for i in dbParticipante():
				encontrado = True
				for item, value in i.exibir().items():
					print(item,': ', value)
				print()
			if not encontrado:
				print('Nenhum participante encontrado!!!')
		elif tipo == 'funcionario':
			for i in dbParticipante():
				if isinstance(i,Funcionario):
					encontrado = True
					for item, value in i.exibir().items():
						print(item,': ', value)
					print()
				else: continue
			if not encontrado:
				print('Nenhum Funcionario encontrado!!!')
		elif tipo == 'externo':
			for i in dbParticipante():
				if isinstance(i,ParticipanteExterno):
					encontrado = True
					for item, value in i.exibir().items():
						print(item,': ', value)
					print()
				else: continue
			if not encontrado:
				print('Nenhum participante Externo encontrado!!!')
	except:
		print('Nenhum Participante Cadastrado!!!')
