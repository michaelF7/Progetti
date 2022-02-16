from os import system 
from alfabeto import alfabeto # Importo il mio dizionario con all'interno l'alfabeto.
system('cls')

def codifica(spazio: str, chiave: int,  frase: int): # Funzione che andrà a codificare la frase in input.
    
    frase_criptata = '' # Stringa vuota.
    
    for lettera in range(len(frase)): # Per ogni lettera che è presente nella nostra frase verranno eseguite le seguenti istruzioni.
        for elemento in alfabeto: # Per ogni elemento che è presente in questo dizionario verranno eseguite le seguenti istruzioni.
            
            try: # Prova 
                if spazio == "no":
                    if  frase[lettera] == alfabeto[elemento]: # Se la nostra lettera sarà uguale alla lettera nel dizionario verranno eseguite le seguenti istruzioni.
                        elemento += chiave  # Incrementando di uno se la nostra lettera sarà uguale ad A verrà sostituita con B ecc.
                        frase_criptata += alfabeto[elemento] # Inserisco la nuova lettera nella stringa vuota.
                        
                elif spazio == "si": # Nel caso in cui volessimo considerare gli spazi le seguenti istruzioni verrano eseguite.
                    if frase[lettera] == alfabeto[elemento]:
                        elemento += chiave
                        frase_criptata += alfabeto[elemento]
                        break
                    
                    elif frase[lettera] == ' ': # Se un elemento della stringa è uguale ad uno spazio le seguenti righe verrano eseguite.
                        frase_criptata += ' ' # Aggiungo uno spazio alla stringa vuota.
                        break
           
            except KeyError: # In caso di KeyError cioè il nostro algoritmo non riuscirà a trovare la chiave inesistente.
                elemento -= 26 # Andra a sostituire la prima lettera dell'alfabeto con l'ultima.
                frase_criptata += alfabeto[elemento] # Inserisco la nuova lettera nella stringa vuota.
                
    return f"Frase codificata: {frase_criptata}" # return di stringa nel programma principale.

# Fare l'inverso della codifica.

def decodifica(spazio: str, chiave: int,  frase_criptata: str):
    
    frase_decriptata = ""
    
    for lettera in range(len(frase_criptata)): 
        for elemento in alfabeto:
            
            try:
                if spazio == "no":
                    if  frase_criptata[lettera] == alfabeto[elemento]:
                        elemento -= chiave  
                        frase_decriptata += alfabeto[elemento]
                    
                elif spazio == "si":
                    if  frase_criptata[lettera] == alfabeto[elemento]:
                        elemento -= chiave  
                        frase_decriptata += alfabeto[elemento]
                        break
                    
                    elif frase_criptata[lettera] == ' ':
                        frase_decriptata += ' '
                        break
                                        
            except KeyError:
                elemento += 26
                frase_decriptata += alfabeto[elemento]
                            
    return f"Frase decodificata: {frase_decriptata.capitalize()}"
    
print("""
      Istruzioni: 
      1 = Imposta la macchina su codifica.
      2 = Impostra la macchina su decodifica.
      """)

impostazione = int(input("Imposta la macchina: "))
if impostazione == 1: print(codifica(input("Vuoi considerare gli spazi? (si/no):  ").lower(), int(input("Inserisci la chiave per la codifica: ")), input("Inserisci la frase da codificare: ").lower()))
elif impostazione == 2: print(decodifica(input("Vuoi considerare gli spazi? (si/no): ").lower(), int(input("Inserisci la chiave per la decodifica: ")), input("Inserisci la frase da decodificare: ").lower()))