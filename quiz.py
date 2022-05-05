from time import sleep

print("Seja muito bem-vindo ao nosso quiz!")
print()
usuario = input("Podemos começar? (s/n): ")
if usuario != "s":
    quit()

score = 0
print()

print("Pronto, então lá vai a primeira pergunta!")
print()
# Perguntas de Português
sleep(1)
while True:
    print(
        " PERGUNTA 1 - \n Dadas as proposições abaixo, marque a opção que preenche corretamente as lacunas: \n"
        " O Reitor Dennis saiu ____ alguns minutos. \n"
        " O mapa indica que o centro da cidade fica ____ meia hora daqui. \n"
        " Daqui ____ um ano iremos passar as férias em París. \n"
        " Não vejo os meus amigos da classe ____ dias. \n \n"
        " a) a; há; há; a \n b) há; a; a; há \n c) a; há; a; há \n d) há; há; a; a\n")
    resposta1 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta1 == "b":
        print("Parabéns! Você acertou.\n \nVamos para a próxima...\n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

sleep(0.5)
while True:
    print(
        "PERGUNTA 2 - \n Em todas as palavras, o acento Agudo foi empregado corretamente, exceto:\n \n "
        "a) parábola, hóspede, cítrico \n b) ópera, história, pajé \n "
        "c) cipó, régua, índio \n d) física, hospício, pastél \n")
    resposta2 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta2 == "d":
        print("Parabéns! Você acertou.\n \nVamos para a próxima...\n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

# Pergunta Ciências da Natureza
sleep(0.5)
while True:
    print(
        "PERGUNTA 3 - \n O processo de urbanização tem provocado o surgimento de inúmeros impactos ambientais.\n "
        "Dentre eles, podem ser citadas:\n 1. As enchentes urbanas. \n 2. A poluição visual. \n "
        "3. A conturbação. \n 4. A bicefalia urbana.\n "
        "Qual dessas opções está correta:\n \n a) 3 e 4 \n b) 1 e 2 \n c) 1, 3 e 4 \n d) 1, 2 e 4 \n")

    resposta3 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta3 == "b":
        print("Parabéns! Você acertou.\n \nVamos para a próxima...\n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

sleep(0.5)
while True:
    print(
        "PERGUNTA 4 - \n “Não existe geração de energia sem impacto ambiental. Esse impacto só será reduzido, se "
        "diminuirmos o consumo”.\n Ressalta o pesquisador da Faculdade de Engenharia Mecânica da Unicamp, "
        "Gilberto Januzzi, em matéria publicada em 12/12/2004 no site http://www.comciencia.br. \n "
        "Dentre as fontes de energia indicadas abaixo, "
        "assinale a opção que apresenta a fonte alternativa de menor impacto ambiental.\n \n "
        "a) Construção de pequenas centrais hidrelétricas (PCHs)  \n "
        "b) Construção de Usinas Térmicas que aproveitam a energia do Urânio e do Plutônio  \n "
        "c) Geração de Energia Eólica (a partir dos ventos)  \n "
        "d) Utilização de biomassa (bagaço de cana e biogás de lixo) \n")

    resposta4 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta4 == "c":
        print("Parabéns! Você acertou.\n \nVamos para a próxima...\n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

# PERGUNTAS DE MATEMÁTICA
sleep(0.5)
while True:
    print(
        "PERGUNTA 5 - \n A expressão 2 sobre 10, equivale em porcentagem a: \n \n"
        " a) 0,02%  \n b) 0,2% \n c) 2%  \n d) 20% \n")

    resposta5 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta5 == "d":
        print("Parabéns! Você acertou.\n \nVamos para a próxima...\n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

sleep(0.5)
while True:
    print(
        "PERGUNTA 6 - \n Três amigos fizeram uma aposta em uma loteria, no total jogaram R$ 50,00 sendo R$ 20,00, "
        "R$ 25,00 e R$ 5,00\n o valor que cada um deles contribuiu para a aposta. Ganharam um prêmio de R$ 265.340,50 e "
        "decidiram dividir\n o prêmio proporcionalmente ao valor apostado. Qual a parte do jogador que investiu R$ 5,00? "
        "\n \n"
        " a) 26.534,05  \n b) 26.234,50 \n b) 26.534,50  \n d) 26.534,55 \n")

    resposta6 = input("A sua resposta é: ")
    print()
    sleep(1)
    if resposta6 == "a":
        print("Parabéns! Você acertou.\n \n")
        score += 1
        break
    else:
        print("Você errou, vamos tentar novamente...\n")
        score -= 0.25
        sleep(0.5)
        continue

nota = score
print(f"Chegamos ao Final! \nE você conseguiu: {score} Pontos")
print()
if nota <= 2:
    print("Poxa, você não foi muito bem. :(")
elif nota == 6:
    print("Meus Parabéns! Você acertou todas as perguntas...")
elif nota <= 4:
    print("Você acertou uma boa parte das perguntas, muito bem!")
