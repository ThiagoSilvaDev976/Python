#Sistema de Cadastro de Cadastro
'''O sistema deve permitir a inserção, consulta e exclusão de dados dos Cadastro.'''
Cadastro = {}
while True:
    print('\nMenu Principal:')
    print('1. Cadastrar Estudante')
    print('2. Consultar Estudantes')
    print('3. Excluir Estudante')
    print('4. Sair')

    digite = input('Digite sua opção: ')
    if digite == "1":
        Estudante = input('Estudante: ')
        matricula = input('Matrícula: ')
        curso = input('Curso: ')
        nascimento = input('Nascimento (dd/mm/aa):')
        print(f'Estudante "{Estudante}" fez a matrícula!')
        Cadastro[matricula] = {'nome': Estudante, 'curso':curso, 'nascimento': nascimento}
    elif digite == "2":
        buscar_matricula = input("Digite a matrícula do Estudante que deseja consultar: ")
        if buscar_matricula in Cadastro:
            Estudante_encontrado = Cadastro[buscar_matricula]
            print(f"Estudante encontrado: {Estudante_encontrado['nome']}")
            print(f"Matrícula: {buscar_matricula}")
        else :
            print("Estudante não encontrado!")
            
    elif digite == "3":
        pass
    elif digite == "4":
        break
    else:
        print("Opção inválida!")

print(Cadastro.items())