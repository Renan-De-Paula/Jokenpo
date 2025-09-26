# Importa a função randint para gerar jogadas aleatórias para o computador
from random import randint

# Importa a função sleep para criar uma pausa entre as falas do jogo
from time import sleep

# Tupla contendo as opções do jogo
itens = ("pedra", "papel", "tesoura")

# Gera uma jogada aleatória (0, 1 ou 2) para o computador
computador = randint(0, 2)

# Exibe as opções para o jogador com formatação colorida no terminal
print(""" 
\033[90m\033[41m[ 0 ] PEDRA \033[0m
\033[98m\033[42m[ 1 ] PAPEL \033[0m
\033[91m\033[46m[ 2 ] TESOURA \033[0m""")

# Recebe a escolha do jogador
jogador = int(input("\033[94mQual sua jogada? \033[0m"))

# Simula a contagem de "JO-KEN-PO" com pausas e cores
print("\033[98mJO\033[0m")
sleep(0.5)
print("\033[96mKEN\033[0m")
sleep(0.5)
print("\033[95mPO!!!\033[0m")
sleep(0.5)

# Exibe a escolha de cada participante
print("--" * 10)
print("\033[92mJogador: {}.".format(itens[jogador]))
print("--" * 10)
print("\033[94mComputador: {}.".format(itens[computador]))
print("--" * 10)

# Lógica do jogo: verifica todas as combinações possíveis
if computador == 0:  # Computador escolheu PEDRA
    if jogador == 0:
        print("\033[93m\033[42mEmpate!\033[0m")
    elif jogador == 1:
        print("\033[92m\033[44mJogador ganhou\033[0m")
    else:
        print("\033[93m\033[41mComputador ganhou!\033[0m")

elif computador == 1:  # Computador escolheu PAPEL
    if jogador == 0:
        print("\033[93m\033[41mComputador ganhou!\033[0m")
    elif jogador == 1:
        print("\033[93m\033[42mEmpate!\033[0m")
    else:
        print("\033[92m\033[44mJogador ganhou\033[0m")

elif computador == 2:  # Computador escolheu TESOURA
    if jogador == 0:
        print("\033[92m\033[44mJogador ganhou\033[0m")
    elif jogador == 1:
        print("\033[93m\033[41mComputador ganhou!\033[0m")
    else:
        print("\033[93m\033[42mEmpate!\033[0m")
