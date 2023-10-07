from random import randint
from time import sleep

# Apresentação do jogo
sleep(1)
print(f'{"="*12}Seja bem-vindo ao Jogo da Adivinhação{"="*12}')
sleep(1)
print('Neste jogo quero que você tente adivinhar um número de 1 a 6 que eu escolhi.')
sleep(1)
input('Aperte qualquer tecla para começar')

# Início do jogo
while True:
    print('Pensando em um número...')
    sleep(2)
    print('Pronto!')
    sleep(1)
    print('Que número eu escolhi?')

    # Parte em que o usuário tenta adivinhar o número
    nm = randint(1, 6)
    nu = int(input())
      

    # Resultado
    if nm == nu:
        print(f'Parabéns! Eu pensei no número {nm} e você ACERTOU!')
    else:
        print(f'Você ERROU! Eu pensei no número {nm}')

    # Opção para jogar novamente
    while True:
        dnv = input('Deseja jogar novamente? (s/n): ')
        if dnv == 'n':
            break
        elif dnv == 's':
            break
        else:
            print('ERRO: Digite apenas "s" para jogar novamente ou "n" para sair.')

    if dnv == 'n':
        break
    
# Fim do código
print('Foi um prazer jogar com você! Até logo.')