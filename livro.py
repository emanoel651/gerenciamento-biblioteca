# Na classe Livro, solicitei as principais informações que o livro precisa.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.num_copias = num_copias
