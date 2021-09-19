import requests;
from datetime import date;
import sqlite3;
import matplotlib as grafico;

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

def exibir():
    command.execute("""SELECT * FROM moedas""")
    for linha in command.fetchall():
        print(linha)
        connect.close()

if request.status_code == 200:
    print('\n',data_format,'\n {:.2f}'.format(dolar),'\n {:.2f}'.format(euro))
    print('')
    inserir()
    exibir()
else:
    print('erro de requisição')