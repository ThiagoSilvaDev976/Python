#for
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

#se colocarmos um "else", sua condição será ativada após o término da lista
lista = ["o", "que", "você", "quiser", "adicionar"]
for qualquercoisa in lista:
    print(qualquercoisa)
else:
    print('a condição else foi aplicada no final')

boletim = {'por':9, 'mat':8, 'hst':9, 'geo':8}
for chave, valor in boletim.items():
    print(f'{chave}:{valor}')