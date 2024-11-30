#A sintaxe básica do for como estrutura de repetição é a seguinte:
#for variavel in range(inicio, fim, passo):

#range() - Cria uma sequência numérica 
for i in range(5):
 print(i)
#Resultado: 0, 1, 2, 3, 4

#Break no for - Interrompe uma sequência
numero_procurado = 7
for i in range(1, 11):
    if i == numero_procurado:
        print(f"Número {numero_procurado} encontrado!")
        break
    print(i)
#Resultado: 0, 1, 2, 3, 4, 5, 6, Número 7 encontrado!

#Continue no for - É utilizado para pular partes do código de acordo com a condição do "if"
for i in range(1,6):
    if i == 3:
        continue
    print(i)
#Resultado: 0, 1, 2, 4, 5
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
#Resultado: 2, 4, 6, 8, 10

#Break e continue - o break é utilizado para interromper o loop interno, porem o loop externo continua e começa um novo loop interno
for num in range(1,20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f"{num} é um numero primo!")
#Resultado: 1 é um numero primo!;  2 é um numero primo!;  3 é um numero primo!;  5 é um numero primo!;  7 é um numero primo!;  11 é um numero primo!;  13 é um numero primo!;  17 é um numero primo!;  19 é um numero primo!