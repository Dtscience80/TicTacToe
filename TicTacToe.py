
#from mulaimain import mulai
#from newgame import new_game
#from newgame import new_game
#from banner import logo
import os
import random
import time
import numpy as np
import os
#from banner import logo
import colorama
from colorama import Fore, Back, Style
import streamlit as st

logo = """
🆃 🅸 🅲\n  🆃 🅰 🅲\n    🆃 🅾 🅴
      """



st.sidebar.info('Welcome to the TICTACTOE game. Silakan Masukkan nama anda tuan ')

st.title("GAME (TICTATOE vs Komputer) INI adalah FINAL PROJECT Kelompok K")
st.header("Terima kasih Anda memainkan Game ini ")
st.text("Game ini dimainkan Oleh Komputer dengan tanda \"X\"")
st.text("Game ini dimainkan Oleh Anda dengan tanda \"#\" \n")
# nama = input("Silakan masukkan nama anda Tuan: ")
# end_game = False
#new=2



def available():
 # return[[True for i in range(n)] for j in range(n) if( isinstance(board[i][j],int)) ]
    for i in range(n):
          for j in range(n):
            if (isinstance(board[i][j],int)):
              return True  

def menang(user):
  if (user==1):
    sign = " #"
  elif(user==2):
    sign = " X"
  boardnp = np.array(board)
  s1=False;s2=False;

  for u in range (n):
      ls=boardnp[u,...]
      count = np.count_nonzero(ls == sign)
      if(count==n):
        s1=True
     
  for u1 in range (n):
      ls1=boardnp[...,u1]
      count1 = np.count_nonzero(ls1 == sign)
      if(count1==n):
        s2=True
  s3=True

  for v in range (n):
      if(boardnp[v][v]!=sign):s3= False
  s4=True

  for v1 in range (n):
      if(boardnp[v1][n-1-v1]!=sign):
        s4= False   
  return (s1 or s2 or s3 or s4)        
  
def cek_isi(a,b):
  return [[ True for i in range(n)] for j in range(n) if( board[a][b] ==" X" or board[a][b] ==" #" ) ]

def pilih(user,a=0,b=0):
    if (user==1):
        sign = " #"
        isi = True
        while isi:
            try : 
                pil = int(input("Silakan pilih kolom nomor berapa : "))      
                for i in range(n):
                    for j in range(n):
                        if (board[i][j]==pil): 
                            board[i][j] = sign  
                            isi = False   
            except:
                st.text("Masukkan kolom 1 s/d ", n**2)
    elif(user==2):       
        while cek_isi(a,b):
            a=random.randint(0, n-1)
            b=random.randint(0, n-1)
        else:
            board[a][b] = " X"   
            st.text("Komputer Memilih [{},{}]" .format(a,b))
            tampil()
            if(menang(2)): 
                st.text("-----FINISH---- Komputer Menang !!!! ") ; 
                return True 
    
def nilai():
  global isi
  isi = isi + 1
  return isi

def tampil():
    boardt = np.array(board)    
    
    for i in range (n):
        for j in range(n):
            if(boardt [i][j] != ' X' and boardt [i][j] != ' #' and int(boardt[i][j])<10): 
                boardt[i][j] = (" " + boardt [i][j])
    
    #[st.text(boardt[i][:], sep ="  ") for i in range(len(boardt))]
    #st.text("")
    
    print(Fore.WHITE, Style.BRIGHT)       
    for i in range(len(boardt)):
        for item in boardt[i][:]:
            if(item ==' X'): color = Back.BLUE
            elif(item==' #'): color = Back.GREEN
            else: color = Back.RED
            print(color + "" .join(str(item)), sep= " \t ", end = '   ')
        print("\n")
    print(Style.RESET_ALL + "")
    
    
def pilih_dimensi():
  ulang = False
  global n
  try: 
    n = int(st.sidebar.text_input('Masukkan dimensi (nxn) Angka (3-9) :', value = 3))
    if(n < 3 or n > 9 or (not isinstance(n,int))): ulang = True
    else: return n
  except: 
    ulang = True
  while ulang:      
    try:   
        st.text("\n Anda harus memasukan angka dari 3 - 9 untuk dimensi board")
        n = int(st.sidebar.text_input('Masukkan dimensi (nxn) Angka (3-9) :', value = 3))
        if(n>2 and n<10): ulang = False; return n;
    except:
        st.text("Dimensi board salah  ")
            
def new_game():
  global new
  global isi
  global n
  global board
  
  nama = st.sidebar.text_input("Silakan masukkan nama anda Tuan: ", value = '')
  n = pilih_dimensi()
  isi = 0;
  board = [[ nilai() for i in range(n)] for j in range(n) ]

  if(n%2==0): 
    mid=n/2
    mid=int(mid)
  else: mid = n//2

  board[mid][mid]=" X"
  tampil()
  pil = 1
  while pil>=1:   
      if(available()):
        if(not menang(1)):   
          pilih(1)
          tampil()
          if(menang(1)): st.text("-----FINISH---- Tuan", nama, " Menang !!!! ");break;          
        else: 
          st.text("-----FINISH---- Tuan", nama, " Menang !!!! ");break;
      else:
           st.text("!BOARD FULL, RELOAD!");break;
      if(available()):
        st.text("!!! Giliran Komputer Berpikir (MOHON TUNGGU 1s) !!!")
        if(not menang(2)):          
            #time.sleep(1)
            a=random.randint(0, n-1)
            b=random.randint(0, n-1)
            if(pilih(2,a,b)) : break       
        else: 
          st.text("-----FINISH---- Komputer Menang !!!! ")
      else:
           st.text("!BOARD FULL, Please RELOAD!"); break;



def mulai():
#   global end_game
  global new
  end_game = False
  while not end_game:
    print(logo)
    new = st.sidebar.text_input('Silakan memilih (0) Exit, (1) New game, (2) Clear Screen : ', value = 1)
    try: 
        if new == "1":
            new_game()
        elif new == "0":
            end_game = True
            st.text("Anda Memilih Exit Game, Terima Kasih sudah bermain..")
        elif new == "2":
            os.system("clear")
        else:
            os.system("clear")
            st.text("Mohon memilih 0 atau 1 atau 2")
    except: 
        st.text("Mohon memilih 0 atau 1 atau 2")
        
mulai()
