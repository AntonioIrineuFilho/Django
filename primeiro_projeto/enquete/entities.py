class Alternativa():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.votos = 0
    
    def __str__(self):
        return self.nome
    

class Enquete():
    def __init__(self, id, pergunta):
        self.id = id
        self.pergunta = pergunta
        self.alternativas = []
    
    def get_alternativas(self):
        return self.alternativas
    
    def set_alternativa(self, alternativa):
        self.alternativas.append(alternativa)

    def __str__(self):
        return self.pergunta