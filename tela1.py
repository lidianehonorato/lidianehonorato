from tkinter import Label
import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro  = requisicao_dic['EURBRL']['bid']
    cotacao_btc   = requisicao_dic['BTCBRL']['bid']

    texto_cotacoes["text"] = f'''
    Dolar :  {cotacao_dolar}
    Euro  :  {cotacao_euro}
    Btc   :  {cotacao_btc}'''


janela = Tk()
janela.title(" Cotação Atual ")
janela.geometry("220x220")

texto_orientacao = Label(janela,text= "Buscar Cotações das moedas")
texto_orientacao.grid(column=0, row=0, padx=8, pady= 5)

botao = Button(janela, text= " Clique aqui", command= pegar_cotacoes)
botao.grid(column=0,row=1, padx=8, pady= 5)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=8, pady= 5)

janela.mainloop()
