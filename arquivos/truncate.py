arquivo= open("diciplinas.txt", "a", encoding='utf-8')
arquivo.truncate(14)
arquivo.close()
arquivo= open('diciplinas.txt', 'r', encoding='utf-8')
print(arquivo.read())
