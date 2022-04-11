"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count
# count é simplesmente um contador
# Zip_longest - ele ser porque a lista de estados e menor que o de cidades entao ele elimina 'Monte Santo', ai para consertar isso utilizamos o zip_longest

indice = count()
###vou ter um bloco de codigo aqui e suponhas que eu quera saber a cidade
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

###vou ter um bloco de codigo aqui e suponhas que eu quera saber os estados da cidades
estados = ['SP', 'MG', 'BA']

#cidades_estados = zip(estados, cidades)
cidades_estados = zip(
    indice,
    estados,
    cidades,
) 
for valor in cidades_estados:
    print(valor)

#print(cidades_estados) #vai retornar o valor na memoria, caso eu queira tratar isso de uma maneira visual
#print(list(cidades_estados))

#for valor in cidades_estados:
    #print(valor) so para gente ver o valor, OUTPUNT:('Sao Paulo', 'SP') onde São paulo = valor[0]  e 'SP' = valor[1]
    #print(valor[0], valor[1])

# print(next(cidades_estados)) #cada print vai interagindo na lista so que nao e a melhor maneira ne, a gente sabe que é o for
# print(next(cidades_estados))
# print(next(cidades_estados))