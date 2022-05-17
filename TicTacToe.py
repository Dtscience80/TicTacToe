# ||CHANGES||
# -def mulai()
# -def new_game()

# ||NEED CORRECTION|
# Known BUG:
# -Start Game Error jika user input selain int (DONE main2.py)
# -0 pertama tidak langsung exit (DONE main2.py)
# -input dimensi value error jika string dan 0 (On Progress main2.py) - DONE
# -dimensi board masih bisa dimainkan lebih dari yang ditentukan - DONE
# -invicible dimensi masih bisa dipilih oleh user - DONE
# -user masih bisa memilih lokasi board yang sudah dipilih - DONE
# -saat permainan berlangsung, jika user input 0 kembali ke pilihan New Game
# -Packaging (On progress link to main2.py)
# -Tampilan Board masih berantakan, tidak simetris (bisa dibuat graphic atau angkanya 3 digit tapi integer)-DONE
# -Bisa di buat link mungkin 2 game, pil 1. game Hangman, 2. Tictactoe, jadi ga usah fokus di bug nya

#!pip install colorama
from mulaimain import mulai
from newgame import new_game

print("GAME (TICTATOE vs Komputer) INI adalah FINAL PROJECT Kelompok K")
print("Terima kasih Anda memainkan Game ini ")
print("Game ini dimainkan Oleh Komputer dengan tanda \"X\"")
print("Game ini dimainkan Oleh Anda dengan tanda \"#\" \n")
# nama = input("Silakan masukkan nama anda Tuan: ")
# end_game = False
#new=2

mulai()
