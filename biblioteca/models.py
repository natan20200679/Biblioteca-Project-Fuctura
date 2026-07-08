from django.db import models

class Livro(models.Model):
    id = models.CharField()
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=25)
    descricao = models.CharField(max_length=100)
    ano = models.IntegerField(max_length=4)
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25)
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.usuario = None
    usuario_id = models.ForeignKey(Usuario.id, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    def __str__(self):
        return f'{self.usuario.nome} -> empréstimo em {self.data_emprestimo}'

