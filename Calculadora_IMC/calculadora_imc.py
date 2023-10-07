from time import sleep

# Apresentação da calculadora
sleep(1)
print('Bem-vindo á Calculadora de IMC! Para iniciarmos preciso de algumas informações, vamos começar?')

sleep(1)
input('Aperte qualquer tecla para começar')

dnv = 'n'
while dnv == 's':
    # Requisição dos dados do usuário para o cálculo
    nome = input('Digite seu nome: ').strip().title()
    peso = float(input(F'Olá {nome}, agora preciso que você me diga seu peso: '))
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
    print(f'{nome}, seu imc é de {imc:.1f} e é considerado como {resultado}')
    
    # Função de calcular novamente:
    while dnv != 's':
        dnv = input("Deseja fazer outro cálculo? (s/n): ").lower().strip()
        print('Digite uma opção válida.')
        if dnv == 's':
            break
    break
print(f'Foi um prazer te ajudar, {nome}. Até logo!')