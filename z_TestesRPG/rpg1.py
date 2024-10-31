import random

# Classe Mestre - define a narrativa e controla os eventos
class Mestre:
    def __init__(self, nome):
        self.nome = nome

    def narrar_evento(self, evento):
        print(f"{self.nome} (Mestre): {evento}")

    def decidir_consequencia(self, sucesso=True):
        if sucesso:
            return "foi bem-sucedido!"
        else:
            return "falhou."

# Classe Personagem - representa o jogador
class Personagem:
    def __init__(self, nome, forca, agilidade, inteligencia, vida=100):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.inteligencia = inteligencia
        self.vida = vida

    def atacar(self, inimigo):
        dano = self.forca + random.randint(1, 10)
        inimigo.receber_dano(dano)
        print(f"{self.nome} ataca {inimigo.nome} causando {dano} de dano!")

    def defender(self, dano):
        defesa = self.agilidade + random.randint(1, 5)
        dano_recebido = max(dano - defesa, 0)
        self.vida -= dano_recebido
        print(f"{self.nome} se defende e recebe {dano_recebido} de dano. Vida restante: {self.vida}")

# Classe Inimigo - representa uma entidade antagonista
class Inimigo:
    def __init__(self, nome, forca, vida):
        self.nome = nome
        self.forca = forca
        self.vida = vida

    def atacar(self, personagem):
        dano = self.forca + random.randint(1, 8)
        personagem.defender(dano)
        print(f"{self.nome} ataca {personagem.nome} causando {dano} de dano!")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida > 0:
            print(f"{self.nome} tem {self.vida} de vida restante.")
        else:
            print(f"{self.nome} foi derrotado!")

# Exemplo de Jogo
mestre = Mestre("Gandalf")
jogador = Personagem("Aragorn", forca=10, agilidade=8, inteligencia=6)
orc = Inimigo("Orc", forca=7, vida=30)

# Narrativa do Mestre
mestre.narrar_evento("Você avança pela floresta e se depara com um Orc ameaçador!")
jogador.atacar(orc)
orc.atacar(jogador)

# Decisão do mestre após o ataque
resultado = mestre.decidir_consequencia(sucesso=(orc.vida <= 0))
print(f"{jogador.nome} {resultado}")
