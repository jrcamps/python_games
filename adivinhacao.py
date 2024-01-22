import random

def jogar():
    print("********************************")
    print("Bem Vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    numero_tentativas = 0
    pontuacao = 1000

    print("Níveis de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel_selecionado = int(input("Selecione o nível: "))
    # print(numero_secreto)

    if (nivel_selecionado == 1):
        numero_tentativas = 20
    elif(nivel_selecionado == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    for rodada in range(1, numero_tentativas + 1):
        print(f"\nTentativa {rodada} de {numero_tentativas}:")
        chute = int(input("Digite um número: "))

        if (chute < 1 or chute > 100):
            print("Digite um valor entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nParabéns, você acertou o número secreto!")
            print(f"Você marcou {pontuacao} pontos.")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos
            if (maior):
                print("O número que você digitou é maior.")
                if (rodada == numero_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você marcou {pontuacao} pontos!")
            elif(menor):
                print("O número que você digitou é menor.")
                if (rodada == numero_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você marcou {pontuacao} pontos!")

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()
