arq_entrada = open("entrada.txt", "r")
arq_saida = open("saida.txt", "w")

linhas = arq_entrada.readlines()

i = 0
while i < len(linhas):
    nome = linhas[i].split()[0]
    notas = [int(n) for n in linhas[i+1:i+5]]  
    media = sum(notas) / len(notas)
    status = "aprovado" if media >= 6 else "reprovado"   
            
    arq_saida.write(f"{nome}\n")
    arq_saida.write(f"{media:.1f}\n")
    arq_saida.write(f"{status}\n \n")

            
    i += 5 
            
arq_entrada.close()
arq_saida.close()
