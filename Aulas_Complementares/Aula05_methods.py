#Strings Methods

#Letra inicial maiúscula:
txt = "arco-íris"
x = txt.capitalize()
print(x) #"Arco-íris"

#Tornando as letras da string minúsculas:
txt = "aRcO-ÍrIs"
x = txt.casefold()
print(x) #"arco-íris"

#Centraliza o Texto:
txt = "arco-íris"
x = txt.capitalize()
print(x) #                   "Arco-íris"

#Contando quantas vezes uma palavra aparece em um texto:
txt = "O arco-íris surgiu logo após a chuva, pintando o céu com suas cores vivas. Cada vez que vejo um arco-íris, sinto uma paz imensa. As crianças corriam pelo campo apontando para o arco-íris no horizonte. 'Olha, um arco-íris!', gritaram. Era o terceiro arco-íris que vi naquela semana. No fim da tarde, o último raio de sol iluminou o arco-íris uma última vez. Nunca vou esquecer esse dia repleto de arco-íris."
x = txt.count("arco-íris")
print(x)

#Codificar texto:
txt = "Olá, mundo!"
bytes_data = txt.encode('utf-8')
print(bytes_data)  #"b'Ol\xc3\xa1, mundo!'"
#Decodificar texto:
decoded_string = bytes_data.decode('utf-8')
print(decoded_string)  #"Olá, mundo!"

#Buscando o final do texto:
end1 = "Rua da Paz, Sumaré"
ar1 = end1.endswith("Sumaré")
print(ar1) #True
end2 = "Aveninda B, Sinhá Sabóia"
rl2 = end2.endswith("Sumaré")
print(rl2) #False

#Colocar um tab o texto:
txt = "H\te\tl\tl\to"
print(txt)                  #H       e       l       l       o
print(txt.expandtabs())     #H       e       l       l       o
print(txt.expandtabs(2))    #H e l l o
print(txt.expandtabs(4))    #H   e   l   l   o
print(txt.expandtabs(10))   #H         e         l         l         o

#O find() diz em qual valor da string sua palavra está.
txt = "O arco-íris surgiu após a chuva, pintando o céu com suas cores."
x = txt.find("arco-íris")
print(x) #2 - se não houver,    -1

#Formatando com format()
txt = "Custa {preço:.2f} reais!"
print(txt.format(price = 49)) #Custa 49.00 reais!

#Usando o format_map()
# Definindo um dicionário com chaves e valores
data = {'nome': 'Alice', 'idade': 25}
# Formatando a string usando format_map()
frase = "Meu nome é {nome} e tenho {idade} anos.".format_map(data)
print(frase) #Meu nome é Alice e tenho 25 anos.

#O index() diz em qual valor da string sua palavra está.
txt = "O arco-íris surgiu após a chuva, pintando o céu com suas cores."
x = txt.find("arco-íris")
print(x) #2 - se não houver, dá erro de traceback

#isalnum() "is alphaumerics ?" (a-z) (0-9)
txt = "Cyberpunk2077"
cod = "çç´´~~"
x = txt.isalnum()
y = cod.isalnum()
print(x, y) #True, False

#Variações da função anterior
'''
isalnum()	True se todos os caracteres forem alfanuméricos
isalpha()	True se todos os caracteres estiverem no alfabeto
isascii()	True se todos os caracteres forem ascii (não são ascii, acentos, cedilha, tils entre outros)
isdecimal()	True se todos os caracteres forem decimais
isdigit()	True se todos os caracteres forem dígitos
'''
#Validando se uma string pode ser um identificador:
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier()) #True
print(b.isidentifier()) #True
print(c.isidentifier()) #False
print(d.isidentifier()) #False

#Mais variações
'''
islower()       True se todos os caracteres forem minúsculos
isnumeric()     True se todos os caracteres forem numéricos
isprintable()   True se todos os caracteres forem imprimíveis
isspace()       True se todos os caracteres forem espaços em branco
istitle()       True se a string seguir as regras de um título
isupper()       True se todos os caracteres forem maiúsculos
'''