nome = open('Arquivo.txt', 'r') # Abra o arquivo (leitura)

conteudo = nome.readlines()
total = str(conteudo)
nt = (total.replace("\\", "").replace("\'", "").replace("[[", "[").replace("]]", ""))
#print(conteudo)
print(nt.split(","))
#print(total)
#print("MENU \n 1)TOTAL DE SALÁRIOS \n 2)TOTAL INVESTIMENTO \n 3)TOTAL RENDIMENTO \n 4)TOTAL DE DESPESAS ")