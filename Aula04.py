#Formatando Strings

#f'strings
idade = 29
texto = "Sou o Thiago, e tenho" + idade
print(texto) #Dará erro, pois há "str' e "int"

#Forma Correta do exemplo acima:
idd = 29
txt = f"Sou o Thiago, e tenho {idd} anos"
print(txt) # --> "Sou o Thiago, e tenho 29 anos"

#Modificador de Formato ":"
prç = 500 #está em "int"
txt = f'Custa {prç:2f} conto' #'f' de float, e 2 de qts casas decimais serão mostradas.
print(prç) #--> 'Custa 500.00 conto'

#Operações Matemáticas dentro de uma String:
txt = f'trabalhei {8+7} anos naquela empresa, diminuíram {3-1} anos por causa das férias, por fgts recebi {2*1500} reais, porem foi dividiram {3/4} disso'
print(txt)

#Caracteres de Escape
'''são inseridos por um \ "contra-barra", seguida do caracter de escape'''

''' \' ou \" Citação única	
    \\	Barra invertida	
    \n	Nova linha	
    \r	Carriage Return	
    \t	Adiciona 1 tab(4 espaços)
    \b	Apaga a letra anterior a ela, pode ser usada mais de uma vez	
    \f	Form Feed	
    \ooo	Octal value	
    \xhh	Hex value '''