import random

def jogar():
    print("********************************")
    print("Bem Vindo ao jogo da Forca!")
    print("********************************")

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    palavra_index = (random.randrange(0,len(palavras)))
    palavra_secreta = palavras[palavra_index].upper()
    palavra_acertada = ['_' for letra in palavra_secreta]

    erros = 0
    tentativas = 6
    enforcou = False
    acertou = False

    print(palavra_acertada)

    while (not enforcou and not acertou):
        chute = input("Escolha uma letra: ")
        chute = chute.strip().upper()

        index = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    palavra_acertada[index] = letra
                index = index + 1
        else:
            erros += 1
            print(f"\nLetra incorreta! Você possui mais {tentativas-erros} tentativas\n")

        enforcou = erros == tentativas
        acertou = "_" not in palavra_acertada

        print(palavra_acertada)

    if (acertou):
        print("Parabéns você acertou!!")
    elif (enforcou):
        print(f"Você perdeu. A palavra secreta era: {palavra_secreta} ")

    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()
