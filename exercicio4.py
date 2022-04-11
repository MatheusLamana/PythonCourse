carrinho = []

carrinho.append(('Produto 1', 40))
carrinho.append(('Produto 2', '50')) #deixei como string para fazer a conversao
carrinho.append(('Produto 3', 20))
# produto, preco = carrinho[0]
# print(produto, preco)

# utilizando list comprehension no (x,y) utilizei os parenteses para virar uma tupla certo
total = [(x,y) for x, y in carrinho]
print(carrinho)
print(total)
print('#' * 100)
# posso ta eliminando o x porque, faz referencia ao nome do 'Produto', como so quero o total ai utiliza o 'y'
total = [y for x, y in carrinho]
print(carrinho)
print(total)
print('#' * 100)
# transformado o y in string linha n=4 e aqui dentro do list eu voltei alterei ele para inteiro.
total = [float(y) for x, y in carrinho]
print(carrinho)
print(total)
print('#' * 100)
# como preciso somar vou envolver a list com a biblioteca sum(). 
total = sum([float(y) for x, y in carrinho])
print(total)