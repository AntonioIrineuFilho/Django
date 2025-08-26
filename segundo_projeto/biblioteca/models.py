from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.nacionalidade} - {self.data_nascimento}'

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.descricao} - {self.ano_publicacao} - {self.autor}'

class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.data_cadastro}'

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=timezone.now)
    data_devolucao = models.DateField()

    def __str__(self):
        return f'{self.livro} - {self.leitor} - {self.data_emprestimo} - {self.data_devolucao}'


