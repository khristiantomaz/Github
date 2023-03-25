# aqui definimos o input do peso
peso = float(input(f'entre seu seu kg aqui'))

# aqui definimos o input da altura
altura = float(input(f'entre sua altua aqui'))

# definimos o calculo do imc da pessoa
imc = peso / (altura*altura)

# definindo o imc para pessoas abaixo do peso
if imc <= 20:
    print('você está abaixo do peso!:')

# definindo o imc para pessoas do peso ideal
elif imc <= 24:
    print('você está no peso ideal!')

# defindo o imc para pessoas acima do peso
else:
    imc >= 24
    print('você está muito acima do peso!')