# no dicionario você, controla o indice. Também chamado de chave


# d1 = {'chave1':'valor da chave'}
# d1['nova_chave'] = 'Valor da nova Chave'

# print(d1['nova_chave'])

# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')

# d1 = { 1: 'valor', 2: 'valor', 3: 'valor real da chave' }

# d1 = {
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'Tupla'
# }

# for k, v in d1.items():
#     print(k, v)


clientes = {
    'cliente1' : {
        'nome' : 'Matheus',
        'Sobrenome' : 'Henrique',
    },
    'cliente2' : {
        'nome' : 'Joao',
        'Sobrenome' : 'Moreira',
    },
}


for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')






# Uma maneira de encontrar valores ai dentro do seu dicionario
# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())