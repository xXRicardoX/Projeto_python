import time
'''
* Escreva um programa em Python que peça ao usuário para digitar um número inteiro positivo e, 
* em seguida, exiba uma contagem regressiva a partir desse número até zero. Por exemplo, se o usuário digitar 5, o programa deve exibir:
5
4
3
2
1
0

'''

valor = int(input('Digite um valor: '))

for contador in range(valor,-1,-1):
    print(contador)
    time.sleep(1)
    