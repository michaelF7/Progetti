from os import chdir, system, path, remove, mkdir

system("cls")

chdir(R"C:\Users\guide\Documents\Code\Local")

def crea(numero_file: int) -> None:
    if numero_file > 0: 
        for i in range(numero_file):
            with open(f"test_{i + 1}.py", "w") as file:
                file.write("from os import system \n\n" "system('cls')")
                print("File creato/i", i + 1)
    else: print("Numero di file insufficiente.")
    
    print(f"Numero di file creato/i: {i + 1}")
    
def distruggi(numero_file: int) -> None:
    if numero_file > 0: 
        for i in range(numero_file):
            if path.exists(f"test_{i + 1}.py"):
                remove(f"test_{i + 1}.py")
                print("File eliminato/i!", i + 1)
            else: print("Il file non esiste!") 
    else: print("Numero di file insufficiente.")
    
    print(f"Numero di file distrutto/i: {i + 1}")

def cartella_class(nome_cartella: str) -> None:
    
    mkdir(f"C:/Users/guide/Documents/Code/Local/{nome_cartella}")
    chdir(fR"C:/Users/guide/Documents/Code/Local/{nome_cartella}")
    
    with open("main.py", "w") as file:
        file.write("from os import system \n" "from obj import *" "\n\n" "system('cls')")
    with open("obj.py", "w") as file: 
        file.write("")
        
    print("La cartella è stata creata!")
    
def html(nome_progetto: str) -> None:
    
    mkdir(f"C:/Users/guide/Documents/Code/Local/{nome_progetto}")
    chdir(fR"C:/Users/guide/Documents/Code/Local/{nome_progetto}")
    
    with open("index.html", "w") as file:
        file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
                
</body>
</html>""")
    
    with open("style.css", "w") as file:
        file.write("")
        
    print("Il progetto è stato creato!")
    
print("""
    istruzioni:
    1 = Crea file.
    2 = Distruggi file.
    3 = Crea cartella classi.
    4 = HTML.
""")

modalità = int(input("Imposta: "))
if modalità == 1: crea(int(input("Inserisci il numero di file da creare: ")))
elif modalità == 2: distruggi(int(input("Inserisci il numero di file da distruggere: ")))
elif modalità == 3: cartella_class(str(input("Nome cartella: ")))
elif modalità == 4: html(str(input("Inserisci il nome del progetto: ").lower()))