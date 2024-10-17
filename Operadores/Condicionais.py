#if - executa um bloco de código se sua condição for atendida
valor = 10
if valor > 5:
    print('O valor é maior que 5.')

#else - executa um bloco de código se a condição de if não for atendida
idade = 20
if idade < 17:
    print('A idade é MENOR que 17')
else:
    print('A idade é MAIOR que 17')

#elif - é utilizando quando mais de uma condição if precisa ser testada.
linguagem = "Python"
if linguagem == "C++":
    print('C++ é uma linguagem de programação compilada.')
elif linguagem == "Python":
    print("Python é uma linguagem de programação de alto nível")
elif linguagem == "Java":
    print("Java é uma linguagem de programação amplamante utilizada no mercado")
else:
    print('Não é nenhuma das duas opções')