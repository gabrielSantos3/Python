idade = int(input('Sua idade: '))

if idade < 3:
    print('Bebê')
elif idade < 10:
    print('Criança')
elif idade < 15:
    print('Pré-adolescente')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')