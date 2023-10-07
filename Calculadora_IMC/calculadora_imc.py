from time import sleep

# Apresentação da calculadora
sleep(1)
print('Bem-vindo à Calculadora de IMC! Para iniciarmos, preciso de algumas informações. Vamos começar?')

sleep(1)
input('Aperte qualquer tecla para começar')

while True:
    # Requisição dos dados do usuário para o cálculo
    nome = input('Digite seu nome: ').strip().title()
    peso = float(input(f'Olá {nome}, agora preciso que você me diga seu peso: '))
    altura_cm = int(input('Agora preciso que digite sua altura em centímetros: '))

    # Conversão da altura em centímetros e cálculo do IMC
    altura = altura_cm / 100.0
    imc = peso / (altura**2)

    # Classificação do IMC
    def classificacao_imc(imc):
        if imc < 18.5:
            return ('abaixo do peso ideal.')
        elif imc < 25:
            return ('peso ideal')
        elif imc < 30:
            return ('acima do peso ideal')
        elif imc < 35:
            return ('obesidade grau I')
        elif imc < 40:
            return ('obesidade grau II')
        else:
            return ('obesidade mórbida')

    # Resultado do usuário
    resultado = classificacao_imc(imc)
    print(f'{nome}, seu IMC é de {imc:.1f} e é considerado como {resultado}')

    # Pergunta se o usuário deseja fazer outro cálculo
    dnv = input("Deseja fazer outro cálculo? (s/n): ").lower().strip()
    if dnv != 's':
        break

print(f'Foi um prazer te ajudar, {nome}. Até logo!')
