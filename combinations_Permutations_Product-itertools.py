"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem nao importa
Permutação - Ordem importa
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Gio', 'Pam', 'Lai', 'Matheus', 'Antonio']

for grupo in product(pessoas, repeat=2):
    print(grupo)

print("\U0001F600")