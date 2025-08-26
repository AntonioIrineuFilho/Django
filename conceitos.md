# Conceitos

* Migração -> Migrar da mémoria para o banco de dados, de uma classe para uma tabela

* Toda função que vai lidar com requisições HTTP tem que ter o parâmetro request

* É possível passar parâmetros para uma variável atráves da URL:

    * Ex: calcular/<altura>/<peso>
    
    * O parâmetro deve ser passado através de <>

    * Os valores passados vão ser atribuidos aos parâmetros da view

    * Ex: def calcular_imc(request, altura, peso)

    * No momento de escrever na URL, você coloca os valores que vão ser atribuidos à variável

    * URL/imc/calcular/14/56

* O conteúdo do HTML que será lido na view por meio do método request.POST.get / request.GET.get será identificado pelo atributo name e o valor atribuido virá do atributo value

* **REGRA DE NEGÓCIO (CONDIÇÕES DO PROGRAMA) NÃO FICA NA VIEW, SE TORNA UM SERVIÇO**

* As variáveis do javascript são passadas com "", enquanto no HTML não precisa (no caso de strings)

 * JS = "{{ x }}" HTML = {{ x }}