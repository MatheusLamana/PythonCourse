string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
list_comp = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(list_comp)
print(list_comp)
print(retorno)
