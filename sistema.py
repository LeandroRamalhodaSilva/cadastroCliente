from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['VER CLIENTES CADASTRADOS', 'CADASTRAR NOVO CLIENTE', 'SAIR DO PROGRAMA'])
    if resposta == 1:
        lerArquivo(arq)
        sleep(1.5)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        linha()
        print('Finalizando.', end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        print(' Volte sempre!')
        break

