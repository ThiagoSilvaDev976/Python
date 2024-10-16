#Introdução ao Python:
#Função Print
print("Hello World")

#Declarando Variáveis:
x = "string"
y = 5 #tipo int
z = 1.5 #tipo float
print(x, y, z)

#Tipos de Variáveis:
x = str(3) #String - deverá ser expressa entre aspas simples ou duplas, pode ser número ou texto
y = int(3) #Int - números inteiros somente, num. fracionados não são permitidos
z = float(3) #Float - números fracionados são expressos no tipo Float
print(x)
print(y)
print(z)

#Descobrindo o tipo de um dado:
x = 'Cyberpunk 2077'
y = 5
z = 3.33
print(type(x))
print(type(y))
print(type(z))

#Variavéis Maiúsculas e minúsculas:
A = "arruumaaa a malaaaee"
a = "que a rural vai arribar !"
print(A, a)

#Variáveis podem: "Ter numéros, letras maiúsculas/minúsculas e underline"
#Variáveis NÃO PODEM: "Começar com números,ter hífen ou espaços no meio"

#Camel Case = 'primeira palavra com minúscula e restante com Maiúsculas'
tipoCamelo = 5
#Pascal Case = 'todas as palavras da variável iniciam com Letra Maiúscula'
TipoPascal = 5
#Snake Case = 'tem underline entre as palavras
Tipo_Cobra = 5
#Esses três tipos podem ser usados para tornar o código mais legível, em casos onde variáveis tem nomes compostos.
print(tipoCamelo, TipoPascal, Tipo_Cobra)

#Declarando valores para multiplas variáveis em uma linha:
vintesete, trintaedois, oitenta = "filho do Ragnar", "de Fevereiro", "seu nome tá escrito na areia da praia"
print(vintesete)
print(trintaedois)
print(oitenta)

#Multiplas variávreis podem ter o mesmo valor:
tangerina = mexerica = bergamota = "Citrus reticulata"
print(tangerina)
print(mexerica)
print(bergamota)

#Lista "Tupla":
Lifepaths = ['nômade', 'marginal', 'corporativo']
print(Lifepaths)

#Extraindo itens de listas:
Lifepaths = ['nômade', 'marginal', 'corporativo']
x, y, z = Lifepaths
print(x)
print(y)
print(z)

#Usando o sinal de + para juntar textos de variáveis:
Descrição = "As aves-do-paraíso são intimamente relacionadas aos corvídeos. As aves-do-paraíso são aves de pequeno a médio porte, medindo entre 15 a 120 cm de comprimento, incluindo a cauda. As espécies maiores têm dimensões aproximadas a um corvo."
Habitat = "A maioria das aves-do-paraíso vive em florestas tropicais, quase todas elas habitando árvores solitárias. Várias espécies foram registradas em manguezais costeiros. A espécie mais meridional, a ave-do-paraíso-meridional (Ptiloris paradiseus) da Austrália, vive em florestas subtropicais úmidas e temperadas. Como um grupo, o gênero Manucodia é o mais adaptável em termos de habitat, em particular a espécie manucódio-luzidio (Manucodia ater), que habita tanto a floresta quanto a savana aberta. Os habitats medianos são os habitats mais comumente ocupados, com trinta das quarenta espécies ocorrendo na faixa altitudinal de 1000–2000 m."
Reprodução = "A maioria das espécies tem rituais de acasalamento elaborados, com pelo menos 8 espécies usando o sistema de acasalamento lek, incluindo os pássaros do gênero Paradisaea. Outros, como as espécies Cicinnurus e Parotia, têm danças de acasalamento altamente ritualizadas."
print(Descrição+ Habitat+ Reprodução)

#Se usarmos o sinal de +, em números int e float, ele terá valor de adição:
x = 1 + 2
y = 3.333334 + 9.999999
print(x)
print(y)

#Usando def, para definir uma variavel:
x = 'olha lá'
def bunito():
  print('olha aqui,' + x)
bunito()