'''
Usando alguns comandos e o tipos primitivos

'''

p = input('Digite algo: ')

print('O tipo primitivo desse valor é? ', type(p))
print('Só tem espaço? ', p.isspace())
print('É um número? ', p.isnumeric())
print('È um alfabético? ', p.isalpha())
print('È um alfanumérico? ', p.isalnum())
print('Esta em maiúsculas?', p.isupper())
print('Esta em minúsculas?', p.islower())
print('Está capitalizada?', p.istitle())
