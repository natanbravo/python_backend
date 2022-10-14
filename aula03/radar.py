
velocidade_permitida = 80


while velocidade_permitida:
    velocidade_usuario = int(input('Sua velocidade é: '))
    if velocidade_usuario <= velocidade_permitida:
        print('Não houve multa')
    elif velocidade_usuario > velocidade_permitida and velocidade_usuario <= velocidade_permitida + 10:
        print('Levou multa leve')
    elif velocidade_usuario >= velocidade_permitida + 11 and velocidade_usuario <= velocidade_permitida + 20:
        print('Levou multa grave')
    elif velocidade_usuario > velocidade_permitida + 20:
        print('Levou multa gravíssima')
