#Manipulando Strings 

#Strings de uma linha:
a = "eu sou uma string"
print(a)

#Strings de várias linhas:
b = """Usando três aspas seguidas,
podemos definir strings de mais de uma linha.

mesmo pulando uma linha, o resultado se manterá correto, com o uso de três aspas seguidas"""
print(b)

#Strings como Matrizes[arrays]:
c = "Cyberpunk"
print(a[1]) #o resultado será "y", por que no python o 1º número é 0(zero)

#Soletrando Strings:
for d in "Cyberpunk":
    print(d) #o resultado será uma letra por linha.

#Contandos quantas letras tem um String:
e = "Hello, World!"
print(len(a)) #o resultado será 13, pois conta o espaço, vírgula e exclamação.

#Podemos verificar se há uma determinada palavra em uma variável:
Crisálida = "Estágio de pupa de insetos da ordem lepidoptera, como borboletas e mariposas. A palavra vem do grego chrysallis, que significa 'dourado'. Durante a fase de crisálida, os insetos crescem e se diferenciam sexualmente."
print("borboletas" in Crisálida) #resultado será: True, pois a palavra borboletas está na variável Crisálida

#Podemos usar a condicional "if" para a mesma função acima.
Crisálida = "Estágio de pupa de insetos da ordem lepidoptera, como borboletas e mariposas. A palavra vem do grego chrysallis, que significa 'dourado'. Durante a fase de crisálida, os insetos crescem e se diferenciam sexualmente."
if "borboletas" in Crisálida:
    print("Sim, 'borboletas' está no texto") #resultará na frase dentro do print.
#Também existe a condição "not in" para verificar a negativa da afirmação, nos dois exemplos.

#Fatiando Strings.

#No meio do texto:
f = "abcdef"
print(f[2:5]) #resultará em 'cde', o 2º,3º,4º entram mas o 5º não entra. lembre que a primeira letra tem valor 0.

#Do início até a posição escolhida:
f = "abcdef"
print(f[:3]) #resultará em 'abc'

#Do ponto escolhido até o final:
f = "abcdef"
print(f[3:]) #resultará em 'def'

#Valores negativos "coisa de corno, mas vai que..."
f = "abcdef ghijkl"
print() #lembrar de ver vídeo

#Modificando Strings

#Torna o texto Maiúsculo:
a = "Hello, World!"
print(a.upper())

#Torna o texto minúsculo
a = "Hello, World!"
print(a.lower())

#Removendo espaços: ínicio e final do texto
a = " borboleta "
print(a.strip())

#Realocação de texto:
a = "Trocadilho"
print(a.replace("ilho", "alho")) #troca o 1º termo pelo 2º

#Separando/dividindo textos:
a = "Hello, World!"
print(a.split(",")) #resultará em ['Hello', ' World!']

#Associando/Ligando Strings sem espaço entre elas:
a = "alho"
b = "poró"
c = a + b
print(c) #"c" será = "alhoporó"

#Com espaço ou hífen, seria:
a = "alho"
b = "poró"
c = a + "-" + b
print(c) #daí resultará em "alho-poró"