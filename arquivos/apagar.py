arquivo = open('diciplinas.txt', 'w')
arquivo.write('Eita!!! Apaguei o conteúdo')
arquivo.close()

arquivo = open('diciplinas.txt', 'r')
print(arquivo.read())
arquivo.close()
