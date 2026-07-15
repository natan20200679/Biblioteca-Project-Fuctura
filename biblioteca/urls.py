from django.urls import path
from biblioteca.views import (login_view, register_view, dashboard, visualizar_livros,
                              cadastrar_livro, descadastrar_livro, visualizar_emprestimos,
                              registrar_emprestimo, visualizar_usuarios, criar_usuario,
                              visualizar_relatorios, excluir_usuario, descadastrar_livros_lote)
urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('login/', login_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('livros/', visualizar_livros, name='livros'),
    path('livros/cadastrar/', cadastrar_livro, name='cadastrar_livro'),
    path('livros/descadastrar/<int:id>', descadastrar_livro, name='descadastrar_livro'),
    path("livros/descadastrar-lote/", descadastrar_livros_lote,name="descadastrar_livros_lote"),
    path('emprestimos/', visualizar_emprestimos, name='emprestimos'),
    path('emprestimos/registrar/', registrar_emprestimo, name='registrar_emprestimo'),
    path('usuarios/', visualizar_usuarios, name='usuarios'),
    path('usuarios/criar/', criar_usuario, name='criar_usuario'),
    path('usuarios/excluir', excluir_usuario, name='excluir_usuario'),
    path('relatorios/', visualizar_relatorios, name='relatorios'),
]