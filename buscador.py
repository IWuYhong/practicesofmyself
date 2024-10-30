import os, datetime, time, re, math
from pathlib import Path

patron = r'N\w{3}\-\d{5}' # Patron de currencia

directory = Path(os.getcwd()) # Directorio actual

fecha = datetime.datetime.now() # Fecha actual, incluir el parametro "%x"

def searching():
    
    '''
    Sin argumentos
    
    return : count, name_file, basename
    '''
    inicio = time.time()
    dictionario = {}
    for file in directory.glob("**/*.txt"):
        file_open = open(file, "r")
        for letra in file_open:
            check = re.search(patron, letra)
            if check:
                dictionario[str(os.path.basename(file))] = check.group()
    fin = time.time()
    return dictionario, round(fin - inicio, 2)


def inicio(duration, lista ):
    
    print("----------------------------------------------------\n")
    print(f"Fecha de búsqueda: {fecha.strftime("%x")}\n")
    print(f"ARCHIVO\t\t\tNRO. SERIE")
    print(f"-------\t\t\t----------")
    for a,b in lista.items():
        print(f"{a}\t\t{b}")
    print(f"\nNúmeros encontrados: {len(diccionario)}.")
    print(f"Duración de la búsqueda: {math.ceil(duration)} seg.\n")
    print("----------------------------------------------------")
    

if __name__ == "__main__":
    diccionario, duration = searching()
    inicio(duration, diccionario)
