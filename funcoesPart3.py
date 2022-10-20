"""
Funções (def) em Python - *args **kwargs - Parte 3
"""
# *args é quando a gente não sabe quais argumentos passar dentro da funcao,
# os args estão empacotados em uma Tupla, se eu exec minha funcao vai aparecer entre parentese
# *n tem o valor do restante da minha lista 
# sep e um separador de valores no print
# kwargs = keywords arguments.
def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade nao existe!')

lista = [1,2,3,4,5]
lista2= [10,20,30]
func(*lista, *lista2, nome='Matheus', sobrenome='Henrique', idade='26')






# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print(*lista, sep='-')
