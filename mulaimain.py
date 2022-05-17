from newgame import new_game
from banner import logo
import os

def mulai():
#   global end_game
  global new
  end_game = False
  while not end_game:
    print(logo)
    new = input("Silakan memilih (0) Exit, (1) New game, (2) Clear Screen : ")
    try: 
        if new == "1":
            new_game()
        elif new == "0":
            end_game = True
            print("Anda Memilih Exit Game, Terima Kasih sudah bermain..")
        elif new == "2":
            os.system("clear")
        else:
            os.system("clear")
            print("Mohon memilih 0 atau 1 atau 2")
    except: 
        print("Mohon memilih 0 atau 1 atau 2")