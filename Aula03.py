#Strings de uma linha:
a = "eu sou uma string"
print(a)

#Strings de várias linhas:
b = """Usando três aspas duplas seguidas,
podemos definir strings de mais de uma linha.

mesmo pulando uma linha, o resultado se manterá correto, com o uso de três aspas duplas seguidas"""
print(b)

#Strings como Matrizes[arrays]:
c = "Cyberpunk"
print(a[1]) #o resultado será "y", por que no python o 1º número é 0(zero)

#Soletrando Strings:
for x in "Cyberpunk":
    print(x) #o resultado será uma letra por linha.