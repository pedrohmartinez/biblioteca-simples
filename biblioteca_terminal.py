import json
from datetime import date
from pathlib import Path
from random import choice

ARQUIVO_DADOS = Path("biblioteca.json")

OPCOES_MENU = (
    "Cadastrar livro",
    "Listar livros",
    "Buscar livro",
    "Emprestar livro",
    "Devolver livro",
    "Mostrar estatísticas",
    "Sugerir uma leitura",
    "Sair",
)

class Livro:
    """Representa um livro e as ações que podem ser feitas com ele."""
   
    def __init__(self, titulo, autor, ano):
       
       self.titulo = titulo.strip()
       
       self.autor = autor.strip()
       
       self.ano = ano
       
       self.disponivel = True
       
       self.leitor = ""
       
       self.data_emprestimo = ""
    
    def emprestar(self, leitor):
        """Empresta o livro se ele estiver disponível"""        
       
        if not self.disponivel:
            return False
    
        self.disponivel = False
        
        self.leitor = leitor.strip()
        
        self.data_emprestimo = date.today().isoformat()
        
        return True
    
    def devolver(self):
        """Registra a devolução se o livro estiver emprestado"""
        
        if self.disponivel:
            return False
        
        self.disponivel = True
        
        self.leitor = ""
        
        self.data_emprestimo = ""
        
        return True
    
    def para_dicionário(self):
        """Transforma o objeto em dicionário para salvá-lo no arquivo."""
        return{
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": self.disponivel,
            "leitor": self.leitor,
            "data_emprestimo": self.data_emprestimo,
        }
        
    @classmethod
    def de_dicionario(cls, dados):
        """Cria um Livro a partir de um dicionário lido do arquivo."""
        
        livro = cls(
            dados["titulo"],
            dados["autor"],
            dados["ano"]
        )
        
        livro.disponivel = dados["disponivel"]
        livro.leitor = dados["leitor"]
        livro.data_emprestimo = dados["data_emprestimo"]
        
        return livro