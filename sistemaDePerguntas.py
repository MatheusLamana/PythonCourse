perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 X 2 ?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 3 X 3 ?',
        'respostas': {
            'a': '9',
            'b': '10',
            'c': '16',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 100 / 2 ?',
        'respostas': {
            'a': '40',
            'b': '51',
            'c': '50',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 2 X 10 + 3 ?',
        'respostas': {
            'a': '20',
            'b': '23',
            'c': '21',
        },
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')

    print('Respostas: ')
   #rk = resposta key, rv = resposta values
    for rk, rv in chave_resposta['respostas'].items():
        print(f' [{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    print()

    if resposta_usuario == chave_resposta['resposta_certa']:
        print('RESPOSTA CORRETA, PARABENS!!')
        respostas_certas += 1
    else:
        print('EITAAAA, RESPOSTA ERRADA TENTE NOVAMENTE  =/')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100     # aqui temos a porcentagem de acerto do usuario

print(f'Você acertou {respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')