# Modelos

* O Django possui o próprio ORM para mapeamento de classes no banco de dados.

* O banco deve estar configurado no settings.py, caso contrário usará sqlite por padrão.

## MIGRAÇÃO DAS CLASSES PARA O BANCO

```python manage.py makemigrations nome``` -> prepara o arquivo para a migração

```python manage.py migrate``` -> realiza a migração conforme as alterações presentes no arquivo criado para o banco de dados real

```python manage.py createsuperuser``` -> cria os dados do admin

## COMANDOS PARA O MODELS

```class Tabela(Model.models)``` -> cria uma tabela

### DENTRO DA CLASS	

```campo = models.CharField(max_length=x)``` -> campo do BD do tipo varchar

```campo = models.TextField()``` -> campo do BD do tipo string longa

```campo = models.IntegerField()``` -> campo do BD do tipo num inteiro

```campo = models.FloatField()``` -> campo do BD do tipo decimal

```campo = models.DecimalField(max_digits=x, decimal_places=y)``` -> campo do BD do tipo decimal, com especificação do total de digitos e do total de digitos após a virgula

```campo = models.BooleanField()``` -> campo do BD do tipo true ou false

```campo = models.DateField()``` -> campo do BD do tipo data

```campo = models.DateTimeField()``` -> campo do BD do tipo data + horas, caso queira preencher com o datetime do momento da adição de algo no BD, basta passar como parametro "auto_now_add=True"

```campo = models.EmailField()``` -> campo do BD do tipo email

```campo = models.URLField()``` -> campo do BD dque armazena uma URL

```campo = models.FileField(upload_to='documentos/')``` -> campo do BD que armazena o link de um arquivo, deve ser especificado o diretorio

```campo = models.ImageField(upload_to='documentos/')``` -> campo do BD que armazena o link de uma imagem, deve ser especificado o diretorio

```campo = models.ForeignKey(Modelo, on_delete=models.CASCADE/NULL/PROTECT/etc)``` -> define o id de uma instância de outra tabela como chave estrangeira, definindo, em caso de exclusão da instância, o que fazer com os objetos da tabela filha.

### TAGS 

```blank``` -> se for True permite campo vazio, se não, não permite. O default é False.

```null``` -> True permite valores nulos, False não permite. O default é False.

```unique``` -> campo que o valor não pode se repetir. Default é False.

```choices``` -> define-se uma lista de tuplas com as possibilidades de valores para aquele campo, depois atribui essa lista ao parâmetro choices dentro do atributo.

```
TAMANHOS = [
  ('P', 'PEQUEN0'),
  ('M', 'MÉDIO'),
  ('G', 'GRANDE')
]

tamanho = models.CharField(choices=TAMANHOS)
```

* Outra abordagem para o choices é em forma de **enum**

```
class Tamanho(models.TextChoices):
    PEQUENO = 'P', 'PEQUENO'
    MEDIO = 'M', 'MÉDIO'
    GRANDE = 'G', 'GRANDE'


class Roupa(models.Model):
    tamanho = models.CharField(choices=Tamanho.choices)
```

### COMANDOS PARA MANIPULAÇÃO DOS MODELOS

```python manage.py shell``` -> abre o shell do Django para permitir as consultas ao banco de dados

```Modelo.objects.filter(campo=valor)``` -> retorna os objetos que tiverem o campo com o valor especificado

```Modelo.objects.create(campo1=valor, campo2=valor, ...)``` -> cria um novo objeto na tabela

* precisa primeiro realizar uma queryset de filtragem, e ai chama o método update para atualizar o campo desejado, caso queria atualizar um objeto especifico deve-se utilizar o save
```
Modelo.objects.filter(campo=valor).update(campo=valor)

Objeto = Modelo.objects.get(id=valor)
Objeto.save()
```

```Modelo.objects.all()``` -> retorna uma lista com todas as instâncias do modelo

```Modelo.objects.get(id=valor)``` -> retorna um objeto especifico

* a deleção pode ser feita direto no objeto ou na queryset(que pode ser um get de um objeto especifico ou um filter de vários objetos)
```
Modelo.objects.filter(campo=valor).delete()

Modelo.objects.get(id=valor).delete()

Objeto = Modelo.objects.get(id=valor)

Objeto.delete()
```

```Objeto.modeloFilho_set.all()``` -> retorna uma lista com os objetos de uma tabela filha do objeto em questão(relação de chave estrangeira)

## VALIDAÇÃO A NÍVEL DE MODELO

* Para validar instâncias de um modelo dentro da classe, pode-se utilizar um método **clean** que retorna um **ValidationError**

* Quando for criar um objeto específico(no services, por exemplo) pode-se chamar essa validação a nível de modelo com o método **full_clean()**

* O full clean chama o método clean criado dentro da classe além de outras vaildações(como de parâmetros do objeto, por exemplo)

```
from django.core.exceptions import ValidationError
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def clean(self):
        if (self.desconto > self.preco):
           raise return ValidationError("DESCONTO MAIOR QUE O PREÇO")
 ``` 

```
produto = Produto(nome="TV", preco=1000, desconto=1200)
produto.full_clean() // chama o clean e realiza validações próprias
produto.save() // se não houver ValidationError, salva no banco
```
