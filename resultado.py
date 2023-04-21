nome = open('Arquivo.txt', 'r') # Abra o arquivo (leitura)

conteudo = nome.readlines()
total = conteudo
print(conteudo)
print(total)
print(total[0][1])
#print("MENU \n 1)TOTAL DE SALÁRIOS \n 2)TOTAL INVESTIMENTO \n 3)TOTAL RENDIMENTO \n 4)TOTAL DE DESPESAS ")