nomes = []
notas = []
medias = []
situacao = ['','','','','','','','','','','','','']
while True:
  nome = input('Digite o nome do aluno:')
  nomes.append(nome)
  notas = []
  for i in range(4):
    notass = float(input('Digite a nota:'))
    notas.append(notass)
  soma = sum(notas) 
  media = soma / 4
  medias.append(media)
  pergunta = input('Deseja continuar?\n'
                    'Digite 1 para Sim e 2 para Não!')
  if pergunta == '1':
    
    continue
  if pergunta == '2':
    cont = 0
    for i in medias:
      if i >= 6 and i <= 10:
        situacao[cont] = 'Aprovado!'
        cont += 1 
      if i < 6 and i >= 0:
        situacao[cont] = 'Reprovado!'
        cont += 1
      if i < 0 or i > 10: 
        print('Erro nas notas digitadas!')
      
    for i in range(len(nomes)):
      print(f'Aluno:{nomes[i]}\n'
            f'Média:{medias[i]}\n'
            f'Situação:{situacao[i]}'
      )
    break
  else:
    continue