r = 's'

while r != 'n':
    weight = float(input('Seu peso: '))
    height = float(input('Sua altura: '))
    
    imc = weight / (height ** 2)
    
    print(f'\nValor do IMC: {imc:.2f}')
    
    r = str(input('\nDeseja realizar o teste novamente? ')).lower()[0]