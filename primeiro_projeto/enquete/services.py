from . import entities

pergunta1 = entities.Enquete(1, "Qual o maior ídolo da história do Vasco?")

pergunta1.set_alternativa(entities.Alternativa(0, "Dinamite"))
pergunta1.set_alternativa(entities.Alternativa(1, "Romário"))
pergunta1.set_alternativa(entities.Alternativa(2, "Edmundo"))
pergunta1.set_alternativa(entities.Alternativa(3, "Barbosa"))

def votar(op):
    pergunta1.alternativas[op].votos += 1

def resultado():
    return { "resultado": pergunta1.alternativas }