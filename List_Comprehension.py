# Ela sao utilizadas por duas coisas aqui no python uma é otimização em termos de perfomance, e escrever menos linha de codigo

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]

exemplo2 = [v * 2 for v in l1]

exemplo3 = [(v, v2) for v in l1 for v2 in range(3)]

lista2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace ('a','@').upper() for v in lista2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for x, y in tupla]
ex5 = dict(ex5)


l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else '0' for v in l3]
print(ex7)