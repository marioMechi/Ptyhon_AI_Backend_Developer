def mensagem(nome):
    print('Executando Nome')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando função longa')
    return f'Olá tudo bem com você {nome}'

def executar(funcao, nome):
    print('Executando executar')
    return funcao(nome)

print(executar(mensagem, 'João'))
print(executar(mensagem_longa, 'João'))