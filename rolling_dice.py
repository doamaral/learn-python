__author__ = 'Lucas'
import random


choice = input("Deseja jogar os dados?(y/n): ")

while choice == "y":
    a = random.randrange(1, 6, 1, int)
    print(a)
    choice = input("Deseja jogar os dados?(y/n): ")

print("Obrigado por jogar os dados!")
