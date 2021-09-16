import requests
from tkinter import *

class application:
    def __init__(self, master=None):
        self.verificaSenha = None
        self.fontePadrao = ("arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do Usuario")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senha = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer )
        self.autenticar["text"] = "Confirmar"
        self.autenticar["width"] = 12
        self.autenticar["font"] = ("Arial", "10")
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


def verificaSenha(self):
    usuario = self.nome.get()
    senha   = self.senha.get()
    if usuario != "lili" or senha != "3030":
        self.mensagem["text"] = "Erro na autenticação!"
    else:
        self.mensagem["text"] = "Autenticado!"


root = Tk()
root.title("Tela de login")
application(root)
root.mainloop()