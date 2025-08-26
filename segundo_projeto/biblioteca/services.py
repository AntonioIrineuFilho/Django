from .models import Autor, Livro, Leitor, Emprestimo

def cadastrar_leitor(nome, email):
    Leitor.objects.create(nome=nome, email=email)

