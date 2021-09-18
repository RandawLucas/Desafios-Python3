import requests;
from datetime import date;
import sqlite3;
import matplotlib as grafico;

connect = sqlite3.connect('D:\projetos_estudos\Desafios-Python\Desafios-Python3\sqlite3\SQLiteDados.db')
command = connect.cursor()


request = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=bbd4b1d1')
resposta = request.json()
data_requsicao = date.today()
data_format = '{}/{}/{}'.format(data_requsicao.day, data_requsicao.month, data_requsicao.year)
dolar = resposta['results']['currencies']['USD']['buy']
euro = resposta['results']['currencies']['EUR']['buy']

if request.status_code == 200:
    print('\n',data_format,'\n',dolar,'\n', euro)
    print('\n',)
    print('\n', )
else:
    print('erro de requisição')