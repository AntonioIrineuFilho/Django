from .models import Carona, SolicitacaoCarona
from django.contrib.auth.models import User

def cadastrar_usuario(username, email, password):
    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        User.objects.create_user(username=username, email=email, password=password)
    else:
        raise ValueError("Usuário ou email já cadastrados")

def atualizar_usuario(username_atual, username_novo=None, email_novo=None, senha_nova=None):
    user = User.objects.get(username=username_atual)

    if (username_novo):
        user.username = username_novo
    if (email_novo):
        user.email = email_novo
    if (senha_nova):
        user.set_password(senha_nova)
    
    user.save()
