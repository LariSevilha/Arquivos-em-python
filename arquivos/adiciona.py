arquivo = open('diciplinas.txt', 'a', encoding='utf-8')

while True:
 disciplina = input('Entre com o nome da disciplina: ')
 if disciplina == 'fim':
     break
 arquivo.write("\n"+disciplina)
 arquivo.close()