# Lists, tuples, str -> Sequences -> iteravel
# No interador a partir do momento que consumiu os valores dele acabou. você não consegue acessar novamente
# interadores e geradores sao feitos para voce consumir os valores deles, eai acabou. Nao tem mais valores para consumir
nome = 'Luis otavio'
iterador = iter(nome)

print(next(iterador))
print(next(iterador))
print(next(iterador))

# for letra in nome:
#     print(letra)

# print('#' * 80)
    
# # for letra in nome:
# #     print(letra)