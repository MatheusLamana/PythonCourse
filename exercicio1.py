"""
1 = Crie uma funçao que exibe uma saudação com os parâmetros saudacao e nome
"""
def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'Matheus')
saudacao('Hello', 'Matthews')
saudacao('Hi', 'Mat.')
print("============================================")
"""
2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""
def numeros(n1, n2, n3):
    print(n1 + n2 + n3)

numeros(10, 30, 10)
numeros(2, 30, 10)
numeros(1, 1, 1)
print("============================================")
"""
3 - Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne  (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def aumeto_porcento(valor, porcentual):
    return valor + (valor * porcentual / 100)

teste = aumeto_porcento(50, 10)
print(teste)

teste = aumeto_porcento(100, 10)
print(teste)

teste = aumeto_porcento(10, 10)
print(teste)

teste = aumeto_porcento(15, 100)
print(teste)
print("============================================")
"""
4 - Fizz buzz - Se o Parametro da função for divisivel por 2, retorne fizz,
se o parametro da funcao fo divisivel por 5, retorne buzz. Se o parametro da funcao for
divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o número enviado.
"""

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisivel por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisivel por  5'
    if n % 3 == 0:
        return f'fizz, {n} é divisivel por 3'
    return n

from random import randint

for i in range (100):
    aleatorio = randint (0, 100)
    print(fb(aleatorio))

