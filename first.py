import tkinter as tk

# Dados de login fictícios
dados_de_login = {"admin11": "1234", "usuario2": "senha2", "qq": "11"}
fonte = ("Comic Sans MS", 15)

def criar_janela():
    janela2 = tk.Toplevel()
    janela2.title("O que deseja fazer?")
    janela2.geometry("400x200")
    janela2.config(bg="#898cfa")

    pergunta_label = tk.Label(janela2, text="Escolha o que deseja fazer:", font=fonte, bg="#898cfa")
    pergunta_label.pack(pady=20)

    # Adicione botões para as ações
    botao_opcao1 = tk.Button(janela2, text="Opção 1", command=acao_opcao1, font=fonte, bg="#55006f", fg="white")
    botao_opcao2 = tk.Button(janela2, text="Opção 2", command=acao_opcao2, font=fonte, bg="#55006f", fg="white")
    
    botao_opcao1.pack(pady=10)
    botao_opcao2.pack(pady=10)

def verificar_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    if usuario in dados_de_login and dados_de_login[usuario] == senha:
        resultado_label.config(text="Login bem-sucedido!", foreground="green")
        criar_janela()
    else:
        resultado_label.config(text="Verifique seu usuário e senha.", foreground="red")

# Funções para ação dos botões na janela secundária
def acao_opcao1():
    print("Opção 1 selecionada")
    

def acao_opcao2():
    print("Opção 2 selecionada")

# Cria uma janela principal
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("500x500")
janela.config(bg="#898cfa")

# Cria rótulos
usuario_label = tk.Label(janela, text="Usuário:", font=fonte, bg="#898cfa")
senha_label = tk.Label(janela, text="Senha:", font=fonte, bg="#898cfa")
resultado_label = tk.Label(janela, text="", font=fonte, bg="#898cfa")

# Cria campos de entrada
usuario_entry = tk.Entry(janela)
senha_entry = tk.Entry(janela, show="*")

# Cria botões
login_button = tk.Button(janela, text="Acessar!", command=verificar_login, font=fonte, bg="#55006f", foreground="white")
botao = tk.Button(janela, text="Clique em Mim", command=criar_janela, font=fonte, bg="#55006f", foreground="white")

# Organiza os widgets na janela
usuario_label.place(x=100, y=100)
senha_label.place(x=100, y=140)
usuario_entry.place(x=220, y=100)
senha_entry.place(x=220, y=140)
login_button.place(x=220, y=180)
resultado_label.place(x=180, y=240)
botao.place(x=50, y=400)

# Inicializa a janela
janela.mainloop()
