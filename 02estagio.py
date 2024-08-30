#Desafio 02

num0 = 0
num1 = 1
num = 0

valor = int(input("Informe um numero: "))

while valor> num:
    num = num0+num1
    num0 = num1
    num1 = num

if valor==num0 or valor==num1 or valor==num:
    print("O número informado pertence à sequancia de Fibonacci!")
else:
    print("O número informado NÃO pertence à sequancia de Fibonacci!")
    