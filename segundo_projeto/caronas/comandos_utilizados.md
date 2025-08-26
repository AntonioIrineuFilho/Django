```User.objects.create_user(username=username, email=email, password=password)``` **criar usuário, método específico para o User do Django, uma vez que já criptografa a senha**

```User.objects.filter(username=username).exists() // User.objects.filter(email=email).exists()``` **Faz um select e retorna True se o user ou o email forem encontrados**