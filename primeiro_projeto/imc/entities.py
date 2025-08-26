class IMC:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
        self.imc = self.peso / (self.altura**2)

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura
    
    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso
    
    def get_imc(self):
        return self.imc
    
    def __str__(self):
        return f'Altura = {self.get_altura} Peso = {self.get_peso} IMC = {self.get_imc():.2f}'