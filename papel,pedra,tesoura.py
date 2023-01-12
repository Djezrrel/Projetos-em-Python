import random

def jogador():
    Opções = ['pedra','papel','tesoura']
    Escolha_do_PC = random.choice(Opções)
    Escolha_do_USER = input("Escolha sua opção: pedra, papel ou tesoura? ")
    while Escolha_do_USER not in Opções:
        Escolha_do_USER = input("Opção inválida. Escolha sua opção: pedra, papel ou tesoura? ")
    print("O computador escolheu: " + Escolha_do_PC)
    if Escolha_do_USER == Escolha_do_PC:
        print("Empate!")
    elif Escolha_do_USER == 'pedra' and Escolha_do_PC == 'tesoura':
        print("Você ganhou!")
    elif Escolha_do_USER == 'papel' and Escolha_do_PC == 'pedra':
        print("Você ganhou!")
    elif Escolha_do_USER == 'tesoura' and Escolha_do_PC == 'papel':
        print("Você ganhou!")
    else:
        print("Você perdeu.")

jogador()