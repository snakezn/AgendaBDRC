#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = str(input('Digite a opcao desejada: ')).strip()
print("Selecionou a {}".format(opcao))


#Estrutura de controle
if opcao == '1':
	funcoes.adicionar()
elif opcao == '2':
	funcoes.listar()
else:
	funcoes.falha()


