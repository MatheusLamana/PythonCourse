# as expressões Lambda, são anonimas
# CTrl + / para comentar um bloco de codigo
# Sempre que for passar um funcao para outra funcao e nao tiver muito condigo vc 
# pode utilizar a funcao lambda para isto.

# a = lambda x, y: x * y
# print(a(2,2)) 


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]



# lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista)