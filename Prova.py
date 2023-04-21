#lista para armazenamento de dados
armazenamento = []

#laço de repetição
while True:

    rendimento = float(input('Informe seu rendimento no mês: '))#coletando informações
    t = (rendimento/0.1)#calculando 1%
    d = rendimento-t#calculando despesas

    mes = str(input('Informe o mês: '))
    armazenamento.append([rendimento, mes])
    alterador = input('Quer alterar? S/N').upper() != "S"

    if alterador == "S":
        n_rendimento = input('Informe seu rendimento no mês: ')
        armazenamento.append(n_rendimento[0])

    if input("Deseja continuar? (S/N)").upper() != "S":
            break

print(armazenamento)
print(rendimento)
print(d)
print(t)