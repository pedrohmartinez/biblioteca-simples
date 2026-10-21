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