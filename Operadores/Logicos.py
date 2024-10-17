#And
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite #false, pq uma das afirmações é falsa.

#Or
saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <= limite #true, pq as afirmações são verdadeiras

#Not
not 1000 > 1500 #true

#Podemos ter mais de um operador na expressão, usando parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)