from funções import *
from tkinter import font
import tkinter as tk

interface = Tk()
interface.title("Cadastro")

# Titulo
negrito = font.Font(weight="bold")
label = tk.Label(interface, text="Informe os Dados: ", font=negrito)
label.pack(pady=20)

# IdUsuário
botão(interface, "Buscar", 10, 220, 65)
caixa(interface, 90, 70)
frase(interface, "idUsuário:", 30, 70)

# Nome
frase(interface, "Nome:", 46, 95)
caixa(interface, 90, 95)

# Telefone
frase(interface, "Telefone:", 34, 120)
caixa(interface, 90, 120)

# E-mail
frase(interface, "E-mail:", 46, 145)
caixa(interface, 90, 145)

# Usuário
frase(interface, "Usuário:", 40, 170) 
caixa(interface, 90, 170)

# Senha
frase(interface, "Senha:", 48, 195)
caixa(interface, 90, 195)

# Comandos
botão(interface, "Inserir", 15, 13, 240)
botão(interface, "Alterar", 15, 130, 240)
botão(interface, "Excluir", 15, 247, 239)

interface.geometry("370x320+200+500")
interface.mainloop()
