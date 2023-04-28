arquivo= open("disc.txt", "r", encoding='utf-16-le')
arquivo.seek(22)
print(arquivo.readline())

arquivo.close()