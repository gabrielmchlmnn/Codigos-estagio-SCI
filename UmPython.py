lista = []
lista_pares = []
lista_impares = []
media = []

for i in range(5):
  numeros = int(input('Digite um número:'))
  lista.append(numeros)

for i in lista:
  if i%2 == 0:
    lista_pares.append(i)
  else:
    lista_impares.append(i)

soma = 0
soma = sum(lista)
media = soma / 5

print(f'Números pares:{str(lista_pares)}\n'
      f'Números ímpares:{lista_impares}\n'
      f'Média : {media}')