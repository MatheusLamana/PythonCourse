# O interavel e algo que você pode se interar sobre ele mais ele nao e necessariamente um interador
# o interador ele vai ter dar 1 valor de cada vez sempre que você precisa deste valor.
# Geradores geralmente sao utilizados quando a gente precisa de valores que vao utilizar muita memoria ou algo grande de ser feito

import sys
import time

l1 = [x for x in range (1000000)]
print(type(l1))
l2 = (x for x in range (1000000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))