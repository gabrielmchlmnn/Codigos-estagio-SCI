vetor = ['1','2','3','4','5']
numero = '0'

for i in range(5):
  numero = str(input('Digite um número:'))
  vetor[i] = numero

print(f'O terceiro número do seu vetor é {vetor[2]}')