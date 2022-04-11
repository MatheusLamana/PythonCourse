"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""
def func1():
    return 'Hello World!'

def func2(func1):
    return func1()

executando = func2(func1)
print(executando)
print()

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a funçao1 executar duas funções que recebam um número diferente de argumentos
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Matheus', saudacao='Bom Dia!')
print(executando)
print(executando2)
