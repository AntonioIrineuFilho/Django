from . import entities

def calcular_imc(altura, peso):
    imc = entities.IMC(altura, peso).get_imc()
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade' 
    return {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso, 
    }

