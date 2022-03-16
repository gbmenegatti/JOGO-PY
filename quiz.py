print("Seja bem-vindo ao nosso quiz!")
usuario = input("Vamos começar? (S/N)")
if usuario != "S":
    quit()

score = 0
print("Vamos começar!")

print(" PERGUNTA 1 - Em qual dessas opções tem somente vogais? \n A) a,e,i,o,u  \n B) b, e ,d c, h \n C) t, u, v, x, z  \n D) a, e , i, k, g \n") 
resposta1 = input ("Resposta: ")

if resposta1 == "A":
    print("Você acertou!")
    score = score+1
else:print("Você errou")

print("PERGUNTA 2 - Quantas sílabas tem a palavra MORANGO \n A) 8 Sílabas  \n B) 6 sílabas \n C) 3 sílabas  \n D) 5 sílabas \n") 
resposta2 = input ("Resposta: ")

if resposta2 == "C":
    print ("Você acertou!")
    score = score+1
else: print("Você errou!")

print("PERGUNTA 3 - José tinha 4 maçãs mas estava com fome e comeu 1. Com quantas maçãs José ficou? \n A) 4 maçãs  \n B) 3 maçãs \n C- 5 maçãs \n D) 1 maçã \n") 
resposta3 = input ("Resposta: ")

if resposta3 == "B":
    print("Você acertou!")
    score = score+1
else: print("Você errou!")

print("PERGUNTA 4 - André tem 1 carrinho, seu aniversário foi ontem e ele ganhou mais 2 carrinhos. Com quantos carrinhos André ficou? \n A) 1 carrinho  \n B) 0 carrinhos \n C) 5 carrinhos  \n D) 3 carrinhos \n") 
resposta4 = input ("Resposta: ")

if resposta4 == "D":
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






