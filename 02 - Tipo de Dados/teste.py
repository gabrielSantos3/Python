n = input('Digite algo: ')
print('Formato de {}: '.format(n),type(n))
print('{} é numérico?'.format(n),n.isnumeric())
print('{} é alfabético?'.format(n),n.isalpha())
print('{} é alfanumérico?'.format(n),n.isalnum())
print('{} é todo maiúsculo?'.format(n),n.isupper())
print('{} é todo minúsculo?'.format(n),n.islower())
print('{} é todo espaço?'.format(n),n.isspace())
print('{} está capitalizada?'.format(n),n.istitle())

#Capitalizada é o texto que possui tanto maiúsculas quanto minúsculas

