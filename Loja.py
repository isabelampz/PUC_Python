# ATP RACIOCÍNIO COMPUTACIONAL

# Importa biblioteca datetime (data e hora)
from datetime import datetime

# VARIÁVEIS GLOBAIS - há outras dentro das funções
meuNome = 'Isabela Milene Paniagua Zanardi'

# Função OBTER LIMITE - Etapas 1 e 2

def obter_limite():
    print('Bem-vindo à Loja da', meuNome)
    cargo = input('Faremos sua análise de crédito pessoal. Por favor, informe seu cargo atual:')
    salario = float(input('Informe o seu salário:'))
    dataNascimento = (input('Digite sua data de nascimento no formato dd/mm/aaaa:'))
    hoje = datetime.now()
    anoAtual = int(hoje.strftime('%Y'))
    anoNascimento = int(dataNascimento.split("/")[2])
    global idade
    idade = anoAtual - anoNascimento
    global limite
    limite  = float(salario * (idade / 1.000) + 100)
    print('Você tem {} anos, e seu cargo é {}\n Seu limite pré-aprovado é de R${}'.format(idade,cargo,limite))


# Função PERGUNTA DE CADASTRO DE PRODUTO
def cadastrar_produtos():
    global nProdutos
    nProdutos = int(input('Quantos produtos você deseja cadastrar?'))
    if nProdutos > 0:
       for i in range(0, nProdutos):
            verificar_produto()
            i += 1
    else:
        print('Não há nenhum produto a ser cadastrado. Fim da análise')
        exit()


# Função VERIFICAR PRODUTO - Guarda os produtos e os valores em uma lista.
def verificar_produto():
    global listaProdutos
    listaProdutos = []
    listaProdutos.append(input('Digite o nome do produto:'))
    global listaValores
    listaValores = []
    listaValores.append(float(input('Digite o valor do produto:')))
    global soma
    soma = sum((listaValores))


# EXECUÇÃO DO PROGRAMA
while True:
    obter_limite()
    cadastrar_produtos()

# TERMINANDO A EXECUÇÃO

    print('Você cadastrou {} produtos'.format(nProdutos))

# 1) CÁLCULO DOS DESCONTOS

    primeiroNome = (meuNome.split(" ")[0])
    if len(primeiroNome) <= soma <= idade:
        print('Parabéns! Você terá um desconto de', len(meuNome), '%!')
        print('O preço do produto com desconto é de', soma - (soma * (len(meuNome) / 100)))
    else:
        print('Infelizmente você não terá mais descontos')

# 2) CÁLCULO DO PARCELAMENTO

    if soma <= (limite * 0.6):
        print('Limite Liberado!')
    elif (limite * 0.6) < soma <= (limite * 0.9):
        print('Valor liberado para parcelar em até 2 vezes')
    elif (limite * 0.9) < soma <= limite:
        print('Valor liberado para parcelar em 3 ou mais vezes')
    else:
        print('Bloqueado parcelamento')

    terminar = str(input('Você gostaria de realizar uma nova análise? Digite "sim" para nova análise. Digite "não" para finalizar'))
    if terminar == "sim":
        continue
    else:
        exit()



'''Eu NEM ACREDITO que consegui!!! Tenho plena consciência de que tem muita coisa pra melhorar, mas a partir de agora eu entendi os fundamentos :) '''
