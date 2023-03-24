alunos = []
notas = []
nome = ''
nota = 0
soma =0 
media = 0
medias = []

for i in range(3):
  nome = input('Digite o nome do aluno:')
  alunos.append(nome)
  notas = []
  for i in range(4):
    nota = float(input('Digite a nota do aluno:'))
    notas.append(nota)
    soma = sum(notas)
  media = soma / 4
  medias.append(media)


for i in range(3):
  print(f'Aluno:{alunos[i]} - Média:{medias[i]}')

posicao = 0
posicao = medias.index(max(medias,key=int),0,3)
print(f'A maior média foi de {medias[posicao]}. Aluno: {alunos[posicao]}.')

posicao2 = 0
posicao2 = medias.index(min(medias,key=int))
print(f'A menor média foi de {medias[posicao2]}. Aluno: {alunos[posicao2]}.')
