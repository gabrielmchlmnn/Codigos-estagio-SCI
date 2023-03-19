lista = []
maior = 0
menor = 0

for i in range(5):
  numeros = int(input('Insira um número:'))
  lista.append(numeros)

maior = max(lista)
menor = min(lista)

print(f'O maior número é {maior}, e o menor número é {menor}.')