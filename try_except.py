
try:
    b = 1/0
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale come ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperador.')
else:
    pass
finally:
    b = ''

print(b)