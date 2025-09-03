import os

import pandas as pd

os.system('cls')
import pandas
import random
import csv
import matplotlib.pyplot as plt
import seaborn as sns
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)

listaTotal = {}

def salvarCSV(vendas, nome_arquivo="vendas.csv"):
    with open(nome_arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=vendas.keys())

        if arquivo.tell() == 0:
            writer.writeheader()

        writer.writerow(vendas)

def cadastrarVenda():
    idVenda = random.randint(1,999999)
    nomeVendedor = input('Nome do vendedor: ')
    nomeProduto = input('Nome do produto: ')
    quantVendida = int(input('Quantidade vendida: '))
    valorVenda = float(input('Digite o total da venda: '))
    valorUnitario = valorVenda / quantVendida
    dataVenda = input('Digite a data da venda (DIA/MÊS/ANO): ')
    listaTotal[idVenda] = {
        'Nome do Vendedor': nomeVendedor,
        'Nome do Produto': nomeProduto,
        'Quantidade vendida': quantVendida,
        'Valor da venda': valorVenda,
        'Valor unitário': valorUnitario,
        'Data da venda': dataVenda
    }
    salvarCSV(listaTotal[idVenda])
    print('Venda adicionada!')


    
def listarVendas():
    for i,j in listaTotal.items():
            print(f'{i} -> {j}\n')
            
def buscarVendaVendedor():

    print('Vamos listar todas as vendas do vendedor que você escolher.')
    nome = input('Digite o nome do vendendor: ')
    for idVenda, dadosVenda in listaTotal.items():
        if dadosVenda['Nome do Vendedor'] == nome:
            print(f'{idVenda} -> {dadosVenda}')
    
def buscarVendaProduto():
    print('Vamos listar todas as vendas feitas desse produto que você escolher: ')
    produto = input('Digite o nome do produto: ')
    for idVenda, dadosVenda in listaTotal.items():
        if dadosVenda['Nome do Produto'] == produto:
            print(f'{idVenda} -> {dadosVenda}')

def estatistica():
    df = pandas.read_csv('vendas.csv')
    lucroTotal = df['Valor da venda'].sum()
    total = df['Quantidade vendida'].sum()
    media = df['Quantidade vendida'].mean()
    moda = df['Quantidade vendida'].mode()
    maximo = df['Quantidade vendida'].max()
    minimo = df['Quantidade vendida'].min()
    variacao = maximo - minimo
    desvio = df['Quantidade vendida'].std()
    print(f'Lucro Total das vendas: {lucroTotal}\nTotal de vendas: {total}\nMédia de vendas: {media}\nQuantidade de vendas mais frequente: {moda}'
          f'\nQuem vendeu mais em uma única venda: {maximo}\nQuem vendeu menos em uma única venda: {minimo}\n'
          f'Diferença de quem vendeu mais pra quem vendeu menos: {variacao}\nDesvio das quantidades: {desvio}')


def relatorio():
    try:
        print(pandas.read_csv('vendas.csv'))
    except FileNotFoundError:
        print('Sem dados para relatório.\n')

def grafico():
    df = pd.read_csv('vendas.csv')
    df_year = df.groupby('Data da venda')['Valor unitário'].mean().reset_index()

    plt.figure(figsize=(6,4))
    sns.lineplot(
        data=df_year,
        x='Data da venda',
        y='Valor unitário',
        marker='o',
        color='purple'
    )
    plt.title('')
    plt.xlabel('Ano')
    plt.ylabel('Preço médio')
    plt.show()

def reset():
    try:
        os.remove('vendas.csv')
        print('Relatório excluído.')
    except FileNotFoundError:
        print('Sem dados para remoção.\n')

def funcaoPrincipal():
    while True:
        print('Escolha uma das opções: ')
        print('0 - Sair do programa')
        print('1 - Cadastrar venda')
        print('2 - Listar todas as vendas adicionadas')
        print('3 - Buscar venda por vendedor')
        print('4 - Buscar venda por produto')
        print('5 - Estatísticas de vendas')
        print('6 - Visualização das vendas por gráfico "feito apenas para prática"')
        print('7 - Gerar relatório final e salvar arquivo')
        print('999 - Resetar relatório')
        x = int(input('\n'))
        if x == 0:
            print('Saindo do programa...')
            break
        if x == 1:
            cadastrarVenda()
        if x == 2:
            listarVendas()
        if x == 3:
            buscarVendaVendedor()
        if x == 4:
            buscarVendaProduto()
        if x == 5:
            estatistica()
        if x == 6:
            grafico()
        if x == 7:
            relatorio()
        if x == 999:
            reset()

funcaoPrincipal()