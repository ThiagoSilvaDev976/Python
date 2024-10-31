#Sistema Bancário com Funções

saldo_inicial = 0
saldo = saldo_inicial
extrato = []

def mostrar_menu():  
  return ''' 
  O QUE DESEJA?
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [x] Sair

  Digite a inicial da função desejada: 
  '''

def depositar(saldo):
  deposito = float(input('Digite o valor desejado para o depósito: R$ '))
  if deposito > 0:
    saldo += deposito
    extrato.append(f'Depósito: R$ {deposito:.2f}')
    print('Depósito realizado com sucesso!')
  else: 
    print('Não foi possível realizar o depósito!')
  return saldo  # Atualiza o saldo no retorno

def sacar(saldo):
  saque = float(input('Digite o valor que deseja sacar: R$ ')) 
  if saque > 0 and saque <= saldo: 
    saldo -= saque
    extrato.append(f'Saque: R$ {saque:.2f}')
    print('Saque realizado com sucesso!')
  else: 
    print('Saldo insuficiente ou valor inválido!')
  return saldo  # Atualiza o saldo no retorno

def mostrar_extrato(saldo):
  print('Extrato da sua conta:')
  if extrato:
    for operacao in extrato:
      print(operacao)
  else:
    print('Nenhuma movimentação registrada.')
  print(f'Saldo final: R$ {saldo:.2f}\n')

while True:
    selecionado = input(mostrar_menu())
    if selecionado == 'd':  # depósito
        saldo = depositar(saldo)
    elif selecionado == 's':  # saque
        saldo = sacar(saldo)
    elif selecionado == 'e':  # extrato
        mostrar_extrato(saldo)
    elif selecionado == 'x':  # sair
        break    
    else:
        print('Opção inválida! Por favor, tente novamente.')