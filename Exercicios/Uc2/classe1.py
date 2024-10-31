#Adaptação do exemplo da Aula: "Dialógo Amigo"

class Pessoa:
    def __init__(self, nome, idade, sentimento):
        self.nome = nome
        self.idade = idade
        self.sentimento = sentimento

    def falar(self):
        return f"Olá meu nome é {self.nome} tenho {self.idade}. Estou me sentindo {self.sentimento} hoje."

pessoa1 = Pessoa("Alice", 30, "feliz")
pessoa2 = Pessoa("Bruno", 25, "ansioso")
pessoa3 = Pessoa("Carla", 28, "curiosa")

def dialogo(*pessoas):
    for pessoa in pessoas:
        print(pessoa.falar())

dialogo(pessoa1, pessoa2, pessoa3)