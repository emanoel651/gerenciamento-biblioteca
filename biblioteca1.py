"""
Tkinter é uma biblioteca em Python utilizada para criar interfaces gráficas de usuário (GUI). 
Ela fornece uma série de widgets, como botões, caixas de texto e listas, 
que podem ser organizados em janelas e frames para criar aplicações interativas. 
Tkinter é fácil de aprender e amplamente utilizada devido à sua integração nativa com Python. 
Com ela, é possível criar interfaces simples ou complexas, controlar eventos do usuário e realizar operações de forma visual.
 Sua simplicidade e robustez a tornam uma escolha popular para o desenvolvimento de aplicações desktop em Python.
"""

# importando a biblioteca tkinter e apelidando (as) como tk
import tkinter as tk

# importando uma funcionalidade da biblioteca chamado messagebox. Cria um alerta para que o usuário possa entender.
from tkinter import messagebox

from usuario import Usuario
from livro import Livro
"""
Criando classe livro, Usuario e BibliotecaApp ( Nesta classe, faz todo o processo de cadastro de livro e usuario, emprestar livro,
                                                devolver livro, ver se está dispinível.). Assim também já criando a interface com usuário.

"""






#Criando a interface
class BibliotecaApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("Sistema de Biblioteca")

        # Foi criado listas para armazenar os dados cadastrados e fazer consulta.
        self.livros = []
        self.usuarios = []
        self.livros_emprestados = []

        # Um frame em Tkinter é um contêiner retangular que pode conter outros widgets, como botões, caixas de texto, labels, entre outros. 
        # Ele é usado principalmente para organizar e agrupar widgets relacionados dentro de uma janela ou outra área de interface gráfica.
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Adicionando texto e butões
        tk.Label(self.frame, text="Cadastro de Livros", font=('Helvetica', 16, 'bold')).grid(row=0, columnspan=2, pady=5) #Titulo
        # Entry - recebe o que usuário digitar
        # row - linha
        # column - Coluna
        # Em Tkinter, grid é um método utilizado para organizar os widgets (como botões, caixas de texto, etc.)
        # em uma janela ou frame, de forma que eles sejam dispostos em uma grade (ou matriz) bidimensional.
        tk.Label(self.frame, text="Título:").grid(row=1, column=0, sticky='e')
    
        # Em Tkinter, columnspan é uma opção que você pode passar ao método grid() 
        # ao posicionar um widget em uma grade. Esta opção especifica o número de colunas que o widget deve ocupar na grade.

        """
        Em Tkinter, sticky é uma opção que você pode passar ao método grid() ao posicionar um widget em uma grade. 
        Esta opção especifica como o widget deve se comportar dentro da célula em que está sendo colocado, em relação às bordas dessa célula.

        O valor de sticky pode ser uma string composta de zero ou mais dos seguintes caracteres: 'n', 's', 'e', 'w', 
        representando os pontos cardeais (norte, sul, leste, oeste) respectivamente.

        Se 'n' estiver presente, o widget será colado à borda superior da célula.
        Se 's' estiver presente, o widget será colado à borda inferior da célula.
        Se 'e' estiver presente, o widget será colado à borda direita da célula.
        Se 'w' estiver presente, o widget será colado à borda esquerda da célula.
        """

        self.titulo_entry = tk.Entry(self.frame)
        self.titulo_entry.grid(row=1, column=1)
        tk.Label(self.frame, text="Autor:").grid(row=2, column=0, sticky='e')
        self.autor_entry = tk.Entry(self.frame)
        self.autor_entry.grid(row=2, column=1)
        tk.Label(self.frame, text="Ano de Publicação:").grid(row=3, column=0, sticky='e')
        self.ano_entry = tk.Entry(self.frame)
        self.ano_entry.grid(row=3, column=1)
        tk.Label(self.frame, text="Número de Cópias:").grid(row=4, column=0, sticky='e')
        self.copias_entry = tk.Entry(self.frame)
        self.copias_entry.grid(row=4, column=1)

        #Criando botão para cadastrar livro
        self.cadastrar_livro_button = tk.Button(self.frame, text="Cadastrar Livro", command=self.cadastrar_livro)
        self.cadastrar_livro_button.grid(row=5, columnspan=2, pady=5)

        # Cadastro de Usuários
        tk.Label(self.frame, text="Cadastro de Usuários", font=('Helvetica', 16, 'bold')).grid(row=6, columnspan=2, pady=5) #Titulo
        tk.Label(self.frame, text="Nome:").grid(row=7, column=0, sticky='e')
        self.nome_usuario_entry = tk.Entry(self.frame)
        self.nome_usuario_entry.grid(row=7, column=1)
        tk.Label(self.frame, text="Identificação:").grid(row=8, column=0, sticky='e')
        self.identificacao_entry = tk.Entry(self.frame)
        self.identificacao_entry.grid(row=8, column=1)
        tk.Label(self.frame, text="Contato:").grid(row=9, column=0, sticky='e')
        self.contato_entry = tk.Entry(self.frame)
        self.contato_entry.grid(row=9, column=1)
        self.cadastrar_usuario_button = tk.Button(self.frame, text="Cadastrar Usuário", command=self.cadastrar_usuario)
        self.cadastrar_usuario_button.grid(row=10, columnspan=2, pady=5)

        # Empréstimo de Livros
        tk.Label(self.frame, text="Empréstimo de Livros", font=('Helvetica', 16, 'bold')).grid(row=11, columnspan=2, pady=5)
        tk.Label(self.frame, text="Título do Livro:").grid(row=12, column=0, sticky='e')
        self.titulo_emprestimo_entry = tk.Entry(self.frame)
        self.titulo_emprestimo_entry.grid(row=12, column=1)
        tk.Label(self.frame, text="Identificação do Usuário:").grid(row=13, column=0, sticky='e')
        self.identificacao_emprestimo_entry = tk.Entry(self.frame)
        self.identificacao_emprestimo_entry.grid(row=13, column=1)
        self.emprestar_livro_button = tk.Button(self.frame, text="Empréstimo", command=self.emprestar_livro)
        self.emprestar_livro_button.grid(row=14, columnspan=2, pady=5)

        # Devolução de Livros
        tk.Label(self.frame, text="Devolução de Livros", font=('Helvetica', 16, 'bold')).grid(row=15, columnspan=2, pady=5)
        tk.Label(self.frame, text="Título do Livro:").grid(row=16, column=0, sticky='e')
        self.titulo_devolucao_entry = tk.Entry(self.frame)
        self.titulo_devolucao_entry.grid(row=16, column=1)
        tk.Label(self.frame, text="Identificação do Usuário:").grid(row=17, column=0, sticky='e')
        self.identificacao_devolucao_entry = tk.Entry(self.frame)
        self.identificacao_devolucao_entry.grid(row=17, column=1)
        self.devolver_livro_button = tk.Button(self.frame, text="Devolução", command=self.devolver_livro)
        self.devolver_livro_button.grid(row=18, columnspan=2, pady=5)

        # Consulta de Livros
        tk.Label(self.frame, text="Consulta de Livros", font=('Helvetica', 16, 'bold')).grid(row=19, columnspan=2, pady=5)
        tk.Label(self.frame, text="Título/Autor/Ano:").grid(row=20, column=0, sticky='e')
        self.consulta_entry = tk.Entry(self.frame)
        self.consulta_entry.grid(row=20, column=1)
        self.consultar_button = tk.Button(self.frame, text="Consultar", command=self.consultar_livros)
        self.consultar_button.grid(row=21, columnspan=2, pady=5)

    def cadastrar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()
        copias = int(self.copias_entry.get())
        self.livros.append(Livro(titulo, autor, ano, copias))
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

    def cadastrar_usuario(self):
        nome = self.nome_usuario_entry.get()
        identificacao = self.identificacao_entry.get()
        contato = self.contato_entry.get()
        self.usuarios.append(Usuario(nome, identificacao, contato))
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

    def emprestar_livro(self):
        titulo = self.titulo_emprestimo_entry.get()
        identificacao = self.identificacao_emprestimo_entry.get()
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.num_copias > 1:
                    livro.num_copias -= 1
                    self.livros_emprestados.append((livro, identificacao))
                    messagebox.showinfo("Sucesso", "Livro emprestado com sucesso!")
                    return
                else:
                    messagebox.showwarning("Aviso", "Não há cópias disponíveis deste livro!")
                    return
        messagebox.showerror("Erro", "Livro não encontrado!")

    def devolver_livro(self):
        titulo = self.titulo_devolucao_entry.get()
        identificacao = self.identificacao_devolucao_entry.get()
        for emprestado in self.livros_emprestados:
            livro, user_id = emprestado
            if livro.titulo == titulo and user_id == identificacao:
                livro.num_copias += 1
                self.livros_emprestados.remove(emprestado)
                messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
                return
        messagebox.showerror("Erro", "Livro não encontrado ou não está emprestado para este usuário!")

    def consultar_livros(self):
        termo = self.consulta_entry.get().lower()
        resultados = []
        for livro in self.livros:
            if termo in livro.titulo.lower() or termo in livro.autor.lower() or termo == livro.ano_publicacao:
                resultados.append(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
        if not resultados:
            messagebox.showinfo("Consulta", "Nenhum livro encontrado com este termo.")
        else:
            messagebox.showinfo("Consulta", "\n".join(resultados))


"""
Depois de fazer todas as verificações, colocar pra rodar

BibliotecaApp, recebe root que executa todas a configuração da classe.
"""

root = tk.Tk()
app = BibliotecaApp(root)

root.mainloop()



