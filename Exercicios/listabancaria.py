nome = input('Digite o Nome: ')
cpf =  input('Digite seu CPF: ')

cliente = [nome, cpf]
clientes = [cliente]

print(f'Cadastrado o nome: {nome} e CPF: {cpf}')

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')

print(f'Cadastrado o nome: {nome} e CPF: {cpf}')

cliente = [nome, cpf]
clientes.append(cliente)

print('-----------------')

print("Clientes Cadastrados")
print(f"Nome: {clientes[0][0]}")
print(f"Cpf: {clientes[0][1]}")
print(f"Nome: {clientes[1][0]}")
print(f"Cpf: {clientes[1][1]}")

print('-----------------')