import adivinhacao
import forca
import time

def biblioteca_jogos():
    print("********************************")
    print("Biblioteca de Jogos")
    print("********************************")

    print("\nJogos disponíveis:")
    print("(1) Adivinhação (2) Forca")
    escolha = int(input("\nEcolha uma das opções: "))

    if (escolha == 1):
        print("Iniciando o jogo da Adivinhação...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        time.sleep(1)
        adivinhacao.jogar()
    elif (escolha == 2):
        print("Iniciando o jogo da Forca...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        time.sleep(1)
        forca.jogar()

if (__name__ == "__main__"):
    biblioteca_jogos()

