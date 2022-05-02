print("Seja bem-vindo ao nosso quiz!")
usuario = input("Vamos começar? (S/N)")
if usuario != "S":
    quit()

score = 0
print("Vamos começar!")

//Perguntas de Português//

print(" PERGUNTA 1 - Há algumas delas que começam largas como boulevards e acabam estreitas que nem vielas. \n Dadas as proposições abaixo, marque a opção que preenche corretamente as lacunas: \n Major Quaresma saiu ____ alguns minutos. \n O mapa indica que o subúrbio fica ____ meia hora daqui. \n Daqui ____ um ano iremos viajar. \n Não vejo Ricardo Coração dos Outros ____ dias. \n A) a; há; há; a \n B)há; a; a; há \n C) a; há; a; há \n D) há; há; a; a \n E) a; a; há; há ")
resposta1 = input ("Resposta: ")

if resposta1 == "B":
    print("Você acertou!")
    score = score+1
else:print("Você errou")

print("PERGUNTA 2 - Em todas as palavras, o acento Agudo foi empregado corretamente, exceto: \n A) parábola, hóspede, cítrico  \n B) ópera, história, pajé \n C) exercício, açaí, músculo  \n D) cipó, régua, índio \n E) física, hospício, pastél ") 
resposta2 = input ("Resposta: ")

if resposta2 == "E":
    print ("Você acertou!")
    score = score+1
else: print("Você errou!")

//Pergunta Ciências da Natureza // 
    
print("PERGUNTA 3 - O processo de urbanização tem provocado o surgimento de inúmeros impactos ambientais. Dentre eles, podem ser citadas: 1. As enchentes urbanas. \n 2.A poluição visual. \n 3. A conturbação. \n 4. A bicefalia urbana.\n Qual dessas opções está correta: A) 3 e 4 \n B) 1 e 2 \n C) 1, 3 e 4 \n D) 1, 2 e 4 ") 

resposta3 = input ("Resposta: ")

if resposta3 == "B":
    print("Você acertou!")
    score = score+1
else: print("Você errou!")

print("PERGUNTA 4 - “Não existe geração de energia sem impacto ambiental. Esse impacto só será reduzido, se diminuirmos o consumo”, ressalta o pesquisador da Faculdade de Engenharia Mecânica da Unicamp, Gilberto Januzzi, em matéria publicada em 12/12/2004 no site http://www.comciencia.br. \n Dentre as fontes de energia indicadas abaixo, assinale a opção que apresenta a fonte alternativa de menor impacto ambiental. \n A) Construção de pequenas centrais hidrelétricas (PCHs)  \n B) Construção de Usinas Térmicas que aproveitam a energia do Urânio e do Plutônio  \n C) Geração de Energia Eólica (a partir dos ventos)  \n D) Utilização de biomassa (bagaço de cana e biogás de lixo) \n") 
resposta4 = input ("Resposta: ")

if resposta4 == "C":
    print ("Você acertou!")
    score = score+1
else: print("Você errou!")

print("PERGUNTA 5 - Nas opções abaixo, qual delas tem somente consoantes? \n A) a,b,g,u  \n B) g,h,j,k \n C) a,s,d,e  \n D) i,j,k,l \n") 
resposta4 = input ("Resposta: ")

if resposta4 == "B":
    print ("Você acertou!")
    score = score+1
else:print("Você errou!")

print(f"Fim do jogo! Pontuação :  {score}")






