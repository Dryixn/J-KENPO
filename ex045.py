from time import sleep
import random
print("-=-" * 20)
escolha = str(input("\033[34mPedra, papel ou tesoura?\033[m ")).lower()
lista = ["papel", "tesoura", "pedra"]
escolhapc = random.choice(lista)
sleep(2)
print("JÔ  ")
sleep(1)
print("KEN  ")
sleep(1)
print("PO")
print("-=-" * 20)
sleep(1)
if escolha == escolhapc:
    print("\033[36mEmpatou, os dois escolheram \033[m{}".format(escolha))
if escolha == "papel" and escolhapc == "tesoura":
    print("\033[36mO computador venceu, ele escolheu \033[m{}".format(escolhapc))
if escolha == "papel" and escolhapc == "pedra":
    print("\033[36mVocê venceu, o computador escolheu \033[m{}".format(escolhapc))
if escolha == "tesoura" and escolhapc == "papel":
    print("\033[36mVocê venceu, o computador escolheu \033[m{}".format(escolhapc))
if escolha == "pedra" and escolhapc == "papel":
    print("\033[36mO computador venceu, ele escolheu \033[m{}".format(escolhapc))
if escolha == "tesoura" and escolhapc == "pedra":
    print("\033[36mO computador venceu, ele escolheu \033[m{}".format(escolhapc))
if escolha == "pedra" and escolhapc == "tesoura":
    print("\033[36mVocê venceu, o computador escolheu \033[m{}".format(escolhapc))
print("-=-" * 20)
