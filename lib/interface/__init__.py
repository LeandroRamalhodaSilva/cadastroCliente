def linha():
    lin = ('-' * 35)
    print(f'{amarelo(lin)}')


def cabeçalho(txt):
    linha()
    print(f'{amarelo(txt)}'.center(45))
    linha()


def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except ValueError:
            vermelho(f'Valor inválido. Por favor, tente novamente.')
        else:
            return i


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'   {c} - {item}')
        c += 1
    linha()
    while True:
        opc = leiaInt(f'Digite sua opção: ')
        if opc > len(lista):
            vermelho(f'Valor inválido. Por favor, tente novamente.')
        else:
            return opc


def vermelho(txt):
    print(f'\033[1;31m{txt}\033[m')


def verde(txt):
    print(f'\033[1;92m{txt}\033[m')



def amarelo(txt):
    return f'\033[1;93m{txt}\033[m'
