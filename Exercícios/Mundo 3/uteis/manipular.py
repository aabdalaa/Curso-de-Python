def abrir(op):
    try:
        b = open(op, 'rt')
        b.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(cr):
    try:
        a = open(cr, 'wt+')
        a.close()
    except:
        print(f'Ocorreu um erro: O arquivo {cr} não existe !')
    else:
        print(f'Arquivo {cr} criado com sucesso !')


def ler(read):
    global a
    try:
        a = open(read, 'rt')
    except:
        print('Erro ao ler o arquivo !')
    else:
        return a.read()
    finally:
        a.close()


def cadastro(arq, nome='DESCONHECIDO', idade=0):
    try:
        h = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            h.write(f'\t{nome:<30} \t{idade:>3} anos\n')
        except:
            print('HOUVE UM ERRO NA HORA DE ESCREVER OS DADOS !')
        else:
            print('NOVO REGISTRO ADICIONADO !')
            h.close()
