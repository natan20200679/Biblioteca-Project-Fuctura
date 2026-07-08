from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=25)
    descricao = models.CharField(max_length=100)
    ano = models.IntegerField(max_length=4)
    def __str__(self):
        return f'id(livro): {self.id}, título: {self.titulo}'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25)
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    def __str__(self):
        return f'id(usuário): {self.id}, Nome: {self.nome}'

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    def __str__(self):
        return f'{self.usuario}\n{self.livro}\ndata(empréstimo): {self.data_emprestimo}'

