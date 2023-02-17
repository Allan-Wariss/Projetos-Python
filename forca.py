# Jogo da Forca
# Desenvolvido por Allan Wariss
import random

palavras = ["melancia", "banana", "uva", "empatia", "embuste", "verbete", "sublime", #Lista de palavras
            "sucinto", "inferir", "apático", "acepção", "astucia", "redimir", "recesso", "estigma", "cultura", "refutar",
            "virtude", "cinismo", "exortar", "soberba", "trivial", "mitigar", "cordial", "aspecto", "imputar", "emergir",
             "sucesso", "alegria", "deboche", "candura", "ademais", "excerto", "almejar", "orgulho", "contudo", "oriundo",
            "alcunha", "austero", "coragem", "salutar", "sensato", "quimera", "excesso", "fomento", "saudade", "escroto",
            "erudito", "modesto", "parcial", "conciso", "amizade", "colosso", "demanda",
            "padecer", "piedade", "racismo", "vigente", "emotivo", "intenso", "auferir", "exilado", "bizarro", "profano",
            "ansioso", "colapso"]
pal_sort = random.randrange(len(palavras))  #Sorteia a palavra da lista de palavras
palavraStr = palavras[pal_sort]             #Reduz a palavra sorteada a variável "palavraStr"
palavra = list(palavraStr)                  #Cada letra da palavra vira um indice de uma lista, ex: uva = ["u","v","a"]
tentativas = 6                              #Numero de tentarivas
jogada = ""                                 #Variável de chute da letra
print("\n"*20)
espaco = []                                 #Cria uma lista para printar espaços vazios de acordo com o tamanho da palavra
def espacoGerar():
    for i in range(0, len(palavra), 1):         #Loop para adicionar espaço de acordo com o tamanho da palavra
        espaco.append("_")
    return espaco
espacoGerar()

def espacoPrint():
    for i in range(0, len(palavra), 1):         #Loop para printar
        print(espaco[i], end="")
    print("\n")
    return espaco

def verificar ():
    global jogada, espaco, palavra, tentativas
    for i in range (0, len(palavra), 1):
        if jogada in palavra[i]:
            print("\n" * 20)
            espaco.pop(i)
            espaco.insert(i,jogada)

    if jogada not in palavra:
        tentativas -= 1
        print("\n" * 20)
        print(f"Errou! Tentativas restantes: {tentativas}")

    return (espaco, tentativas)

def main ():
    while True:
        global jogada, espaco, palavra, tentativas
        espacoPrint()
        jogada = str(input("Chute a letra: "))
        verificar()
        if espaco == palavra:
            print("VOCÊ GANHOU!")
            print(f"Sobrou {tentativas} tentativas.")
            print(palavraStr)
            break
        if tentativas == 5:
            print(" O")
            print("\n")
        elif tentativas == 4:
            print(" O/")
            print("\n")
        elif tentativas == 3:
            print(" O/")
            print(" |")
            print("\n")
        elif tentativas == 2:
            print("_O/")
            print(" |")
            print("\n")
        elif tentativas == 1:
            print("_O/")
            print(" |")
            print("/ ")
            print("\n")
        elif tentativas == 0:
            print(" 0")
            print("⅃|L")
            print("⅃ L")
            print("\n")
            print("Enforcou!")
            print(f"Era {palavraStr}")
            break
main()