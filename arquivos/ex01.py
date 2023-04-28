arquivos = open("ocorrencia.txt", "r")

# arquivos = open("diciplinas.txt", "r", encoding= 'UTF-8') So no windows, é para configurar a acentuação
print(arquivos.readline())

for i in arquivos:
    print(i)