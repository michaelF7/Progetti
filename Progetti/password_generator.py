from random import choice
from string import printable
from os import system

system("cls")

continua = "si"

while continua.lower() == "si":
    system("cls")
    
    password = ""
    
    while True:
        leng = input("Inserisci un numero: ")
        
        try:
            val = int(leng)
            leng = int(leng)
            for i in range(leng):
                password += choice(printable)
            print("".join(password.strip()))
            break
        except ValueError:
            print("Non hai inserito un numero riprova: ")

    continua = input("Vuoi continuare?: ")
    
    while continua not in ("si, no"):
        print("Inserimento non valido!")
        continua = input("Vuoi continuare?: ") 