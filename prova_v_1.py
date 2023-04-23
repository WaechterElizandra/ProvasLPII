with open('Arquivo.txt', 'r') as nome: # Abra o arquivo (leitura)
    conteudo = nome.readlines()
meses = []
salarios = []
despesas = []
porcentos_10 =[]
porcentos_1 = []

try:
    mes = int(input('Informe o seu mês:'))
    meses.append(mes)

    salario = float(input('Informe seu salário:'))
except(TypeError, ValueError):
    print('Valor incorreto')
else:
    salarios.append(salario)
    alterar_salario = str(input('Quer alterar? [S/N]')).upper().split()[0]
    # Calculando valor que será investido, ou seja, os 10% do salário.
    porcento_10 = ((salario * 10)/100)
    porcentos_10.append(porcento_10)
        # calculando o juros sobre o investimento, ou seja, o 1% sobre os 10% retirados do salário.
    porcento_1 = (porcento_10 * 1) / 100
    porcentos_1.append(porcento_1)
    # calculando despesas
    despesa_mensal = (salario - porcento_10)
    despesas.append(despesa_mensal)

    if alterar_salario == 'S':
        novo_salario = float(input('Informe o novo salario:'))
        salario = novo_salario


    with open('Arquivo.txt', 'a') as nome: # Abre novamente o arquivo (escrita)
        nome.write(f'{mes},{salario},{porcento_10},{porcento_1},{despesa_mensal}\n')


    nome.close()
