def carregar_ocorrencias():
    arquivo = open("ocorrencia.txt", "r", encoding="utf-8")
    lista_ocorrencias = []
    for i in arquivo:
        id = i #arquivo.readline()
        titulo = arquivo.readline()
        descricao = arquivo.readline()
        implicacao = arquivo.readline()
        status = arquivo.readline()
        prazo = arquivo.readline()
        arquivo.readline()
 
        ocorrencia = dict(
            id = id[4:len(id)],
            titulo = titulo[8: len(titulo)], 
            descricao = descricao[10:len(descricao)],
            implicacao = implicacao[12:len(implicacao)],
            status = status[8:len(status)],
            prazo = prazo[7:len(prazo)]
        )
        lista_ocorrencias.append(ocorrencia)
    arquivo.close()
    return lista_ocorrencias
 
def impressao_ocorrencia(ocorrencia):
    print("###Ocorrência ###")
    print("Id:", ocorrencia["id"])
    print("Título:",ocorrencia["titulo"])
    print("Descrição:",ocorrencia["descricao"])
    print("Implicações:",ocorrencia["implicacao"])
    print("Status:",
    "sim" if ocorrencia["status"] == True
        else "não")
    print("Prazo (em dias):",ocorrencia["prazo"])
 
lista  = carregar_ocorrencias()
for i in lista:
    impressao_ocorrencia(i)

