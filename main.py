import requests;
from datetime import date;
import sqlite3;
import matplotlib.pyplot as grafico;

connect = sqlite3.connect('D:\projetos_estudos\Desafios-Python\Desafios-Python3\sqlite3\SQLiteDados.db')
command = connect.cursor()

request = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=bbd4b1d1')
resposta = request.json()
data_requsicao = date.today()
data_format = '{}-{}-{}'.format(data_requsicao.day, data_requsicao.month, data_requsicao.year)
dolar = resposta['results']['currencies']['USD']['buy']
euro = resposta['results']['currencies']['EUR']['buy']
def inserir():
    command.execute("""INSERT INTO moedas (Data, Dolar, Euro) VALUES(?,?,?)""", (data_format,dolar, euro))
    connect.commit()
    print('Dados inseridos com sucesso!')

tempo = []
valorDolar = []
valorEuro = []
def exibir():

    command.execute("""SELECT * FROM moedas""")
    for linha in command.fetchall():
        tempo.append(linha[0])
        valorDolar.append(linha[1])
        valorEuro.append(linha[2])
        #print(linha)
        connect.close()

    print()
#Adicionando grafico Visual da blibioteca matplotlib (mas utilizei somente o py plot, ficou: "matplotlib.pyplot")
def graficos():
    grafico.ylabel("Valor em Reais (R$) ", color='green') #adiciona texto ao eixo Y
    grafico.xlabel("Tempo",color="blue") #adiciona texto ao eixo X
    grafico.axis(ymin=0, ymax=10) #adiciona limite de valores nos eixos (ex: ymin/ ymax), é possivel adicionar colocação as linhas
    # .plot() = Cria um Gráfico de linhas
    # .bar() =  Cria um Gráfico de barras
    grafico.plot(tempo, valorDolar,label='Dolar',marker='s') #adicionei a linha do grafico referente a Dolar (label = texto da legenda/ e marker = marcação dos valores da linha)
    grafico.plot(tempo, valorEuro, label='Euro', marker='s') #adicionei a linha do grafico refente a Euro
    grafico.grid(True) #Adiciona a tabelação
    grafico.title('Cotação em Reais') # Adiciona o Titulo do Grafico
    grafico.legend() #adiciona aa labels dos grafico.plot como legendas

    grafico.show() #Exibe o gráfico

if request.status_code == 200:
    print('\nValores da cotação de hoje: ',data_format,'\nDolar: {:.2f}'.format(dolar),'\nEuro: {:.2f}'.format(euro))
    print('')
    #inserir()
    exibir()
    graficos()
else:
    print('erro de requisição')