
total_salarios = 0
total_por10 = 0
total_por1 = 0
total_despesa = 0
total_investimento = 0

with open('Arquivo.txt', 'r') as n:

    meses = []
    salarios = []
    despesas = []
    porcentos_10 =[]
    porcentos_1 = []

    armazem = n.readlines()

    for linha in n:
        # Separar os valores da linha pelo caractere ","
        valores = linha.split(",")

        mes = float(valores[0])
        salario = float(valores[1])
        porcento_10 = float(valores[2])
        porcento_1 = float(valores[3])
        despesa = float(valores[4].strip())

        meses.append(mes)
        salarios.append(salario)
        porcentos_10.append(porcento_10)
        porcentos_1.append(porcento_1)
        despesas.append(despesa)

    for cada in salarios:
        total_salarios += cada

    for cada in porcentos_10:
        total_por10 += cada

    for cada in porcentos_1:
        total_por1 += cada

    for cada in despesas:
        total_despesa += cada

total_investimento = float(total_por10 + total_por1)

opcoes = int(input("MENU \n 1)TOTAL DE SALÁRIOS \n 2)TOTAL INVESTIMENTO \n 3)TOTAL RENDIMENTO \n 4)TOTAL DE DESPESAS\n 5) SAAIR DO MENU\n\n Resposta: "))


while opcoes != 5:
    if opcoes == 1:
        print(f'O total de salários recebido foi : {total_salarios}')
    if opcoes == 2:
        print(f'O total investido foi : {total_por10}')
    if opcoes == 3:
            print(f'O total do rendimento : {total_por1}')
    if opcoes == 4:
        opcoes = int(input(f'O total das despesas : {total_despesa}'))