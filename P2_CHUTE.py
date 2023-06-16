# Chute um Número

'''
Escreva um programa que ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número
até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início
do programa

Metodo 5Q's:
1. Quais são os dados de entrada necessário?
Valor aleatório de 1 a 10
Chute do usuário
2. O que devo fazer com estes dados?
Comparar o chute do usuário com o valor aleatório gerado pelo programa e dizer se o chute foi
maior, menor ou igual ao valor gerado no início do programa
3. Quais são as restrições deste problema?
Um valor aleatório de 1 a 10
4. Qual é o resultado esperado?
O resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início
do programa
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio:
    print("Chute foi maior que o valor gerado")
elif chute < valor_aleatorio:
    print("Chute foi menor que o valor gerado")
else chute = valor_aleatorio:
    print("Você acertou!")

'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input("Chute um valor de 1 a 10: "))
    if chute > valor_aleatorio:
        print("Chute foi maior que o valor gerado")
    elif chute < valor_aleatorio:
        print("Chute foi menor que o valor gerado")
    elif chute == valor_aleatorio:
        acertou = True
        print("Você acertou!")
