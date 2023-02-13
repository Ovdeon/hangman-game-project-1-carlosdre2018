import json
import random

def tildes(vocal):
    if vocal == "á":
        vocal = "a"
    elif vocal == "é":
        vocal = "e"
    elif vocal == "í":
        vocal = "i"
    elif vocal == "ó":
        vocal = "o"
    elif vocal == "ú":
        vocal = "u"
    return vocal
def tildes_inv(vocal):
    if vocal == "a":
        vocal = "á"
    elif vocal == "e":
        vocal = "é"
    elif vocal == "i":
        vocal = "í"
    elif vocal == "o":
        vocal = "ó"
    elif vocal == "u":
        vocal = "ú"
    return vocal

with open("words.json") as my_words:
    words = json.loads(my_words.read())
play = True

print("\n\n---------------------Bienvenido al juego del ahorcado ------------------------")
while play:
    r = random.randint(0, len(words['data']) - 1)
    word_game = words['data'][r]
    contador = 0
    corrects = []
    print("\n\nSe ha seleccionado aleatoriamente una palabra a adivinar: \n")

    for a in word_game:
        if a != " ":
            print("_", end=" ")
        elif a == " ":
            print("   ", end=" ")
    while contador < 6:
        verif = 0
        desplaz = 0
        max_dig = True
        repetido = True
        print("\n\n\n*******************************************************************")
        n = input("\n\nDigite su letra o numero: ")
        if len(n)>1:
            print("\n\n-----------Solo una letra o número a la vez-----------")
            max_dig = False
        elif len(n)==1:
            if (n in corrects) or (n.swapcase() in corrects) or (tildes(n) in corrects) or (tildes(n).swapcase() in corrects) or (tildes_inv(n) in corrects) or (tildes_inv(n).swapcase() in corrects):
                print("\n\n-----------El valor dado ya fue digitado-----------\n\n")
                repetido = False
        for i in word_game:
            if (i == n or i == n.swapcase() or n == tildes(i) or n == tildes(i).swapcase() or i == tildes(n) or i == tildes(n).swapcase()) and repetido:
                print(f"\nCORRECTO, la letra <<{i}>> esta en la frase\n")
                corrects.append(i)
                break
            elif i != n:
                desplaz = desplaz + 1
            if desplaz == len(word_game) and max_dig and repetido:
                print(f"\nINCORRECTO, la letra <<{n}>> no se encuentra en la frase")
                contador = contador + 1
        if contador == 1:
            print("\n\t _________")
            print("\t |")
            print("\t🙂\n\n")
        if contador == 2:
            print("\n\t _________")
            print("\t |")
            print("\t🙂")
            print("\t |\n\n")
        if contador == 3:
            print("\n\t _________")
            print("\t |")
            print("\t🙂")
            print("\t |")
            print("\t  \ \n\n")
        if contador == 4:
            print("\n\t _________")
            print("\t |")
            print("\t🙂")
            print("\t |")
            print("\t/|\ \n\n")
        if contador == 5:
            print("\n\t _________")
            print("\t |")
            print("\t🙂")
            print("\t |")
            print("\t/|\ ")
            print("\t/  \n\n")
        for j in word_game:
            desplaz2 = 0
            if (j in corrects) or (j.swapcase() in corrects):
                print(f"{j}", end =" ")
            else:
                if j!= " ":
                    print("_", end = " ")
                    verif = verif + 1
                elif j == " ":
                    print("   ", end= " ")
        if len(corrects) == 0:
            for a in word_game:
                if a != " ":
                    print("_", end=" ")
                elif a == " ":
                    print("   ", end=" ")
        if len(corrects) > 0:
            if verif == 0:
                print("\n\n\nHaz ganado el juego, FELICIDADES")
                game = input("Desea seguir jugando? (N para dejar de jugar): ")
                break
    if contador == 6:
        print("\n\n\t _________")
        print("\t |")
        print("\t🙂")
        print("\t |")
        print("\t/|\ ")
        print("\t/ \ ")
        print("\n\nHas perdido, suerte a la proxima\n\n")

        print(f"\tLa frase a adivinar era: {word_game}")
        game = input("\n\nDesea seguir jugando? (N para dejar de jugar) : ")
        if game == "N":
            play = False
print("\n\nGracias por jugar al ahorcado, buen dia.")