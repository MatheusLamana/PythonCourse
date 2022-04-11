"""
Como agrupar elementos em um dicionario 
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Omero', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'C'},
    {'nome': 'Luisa', 'nota': 'C'},
    {'nome': 'Roberto', 'nota': 'A'},
    {'nome': 'Antonio', 'nota': 'B'},
    {'nome': 'Isis', 'nota': 'D'},
    {'nome': 'Julio', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'B'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)


'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Notas: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

