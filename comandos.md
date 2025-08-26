# Comandos Básicos

## Comandos Gerais

* Criar ambiente virtual isolado -> **python -m venv ambiente_virtual**

* Para ativar no **Windows** -> **cd nome_venv/Scripts/activate**

* Para ativar no **Linux** -> **source nome_venv/bin/activate**

* Instalar o pacote do Django -> **pip install Django**

* **HttpResponse(response)** -> comando que retorna uma string para a interface, podendo misturar HTML e comandos Python

* **render(request, 'pagina.html')** -> retorna para a requisição a página HTML renderizada

* Parâmetro **context** -> Parâmetro que retorna um dicionário com dados a serem renderizados na página

* Esses dados são mapeados no template com base na chave do dicionário
* 
## Comandos Python no Template

* Os comandos Python possuem uma sintaxe específica no template

* Quando for para mostrar o valor de uma variável -> **{{ valor }}**

* Quando for para utilizar recursos do Python como o laõ -> **{% for i in range %} {% endfor %}**

* Diferente do Python convencional, é necessário fechar as estrutras com um comando de end para que o template saiba onde encerrar a aplicação do HTML

* Ao utilizar um formulário configurado com o metodo POST, é necessário utilizar **{% csrf_token %}** para proteger contra phishing mandando de um dominio para o mesmo e bloqueando caso não seja

* Se esse comando for utilizado no codespace, é necessário autorizar o codespace para que o csrf não bloquei o domínio do codespace:

```
if 'CODESPACE_NAME' in os.environ:
    codespace_name = os.getenv("CODESPACE_NAME")
    codespace_domain = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
    CSRF_TRUSTED_ORIGINS = [f'https://{codespace_name}-8000.{codespace_domain}','https://localhost:8000']
```


