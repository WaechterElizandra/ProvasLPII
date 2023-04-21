

nome = open('Arquivo.txt', 'r') # Abra o arquivo (leitura)
conteudo = nome.readlines()
mes = int(input('Informe o seu mês:'))

salario = float(input('Informe seu salário:'))

alterar_salario = str(input('Quer alterar? [S/N]')).upper().split()[0]
# Calculando valor que será investido, ou seja, os 10% do salário.
porcento_10 = ((salario * 10)/100)

    # calculando o juros sobre o investimento, ou seja, o 1% sobre os 10% retirados do salário.
porcento_1 = (porcento_10 * 1) / 100

    # calculando despesas
despesa_mensal = (salario - porcento_10)

if alterar_salario == 'S':
    novo_salario = float(input('Informe o novo salario:'))
    salario = novo_salario

conteudo.append([mes, salario, porcento_10, porcento_1, despesa_mensal])   # insira seu conteúdo

nome = open('Arquivo.txt', 'w') # Abre novamente o arquivo (escrita)
nome.writelines(str(conteudo)) # escreva o conteúdo criado anteriormente nele.

nome.close()