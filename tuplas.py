# a diferença da tupla da lista, e que você nao pode adicionar, remover e nao pode mudar os indices da tupla.
# se for pra modificar os valores e melhor utilizar lsita, mais nesta aula vamos fazer a migraçao de uma tupla para lista


# t1 = (1,2,3, 'a', 'Matheus Henrique')

# print(t1[1:4])

# t1 = 1,2,'Matheus',4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2


# n1, n2, n3, *_ = t3

# print(n3)


t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)
print(t1)
