# Requisição Assíncrona Django

## Ferramentas

* **Django**

* **Javascript(Fetch API)**

## Papel do Django

* Processar o json de entrega com as informações para o JS na view

## Papel do Javascript

* Se comunicar com o HTML(esperar o evento que inicia a requisição)

* Diante desse evento, preparar os dados a serem enviados

* Enviar a requisição assíncrona com Fetch API:
  * Método de envio: POST, GET
  * Corpo do envio: preparado na etapa anterior
  * Cabeçalho: basicamente o CSRF em um POST

* .then(1º): receber o json de resposta da view

* .then(2º): retornar no HTML o resultado da requisição

