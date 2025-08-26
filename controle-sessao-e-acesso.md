# Controle de Sessão

## Autenticação

```from django.contrib.auth import authenticate, login, logout```-> Header para importar as funções necessárias.

* Função ```àuthenticate(username=username, password=password)``` -> Faz a autenticação do usuário para liberar o acesso.

* Função ```login(request, user)``` -> Cria a sessão e o controle de cookies para manter o usuário logado.

* Função ```logout(request)```-> Encerra a sessão.
