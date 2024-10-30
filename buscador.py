import os, datetime, time, re, math
from pathlib import Path

patron = r'N\w{3}\-\d{5}'  # Patron de currencia

directory = Path(os.getcwd())  # Directorio actual

fecha = datetime.datetime.now()  # Fecha actual, incluir el parametro "%x"


def searching():
    """
    Searches for currency codes in text files.

    Returns:
        dictionary: A dictionary containing filenames as keys and matched currency codes as values.
        float: The elapsed search duration in seconds (rounded up).
    """

    inicio = time.time()
    dictionario = {}
    try:
        for file in directory.glob("**/*.txt"):
            try:
                file_open = open(file, "r")
                for letra in file_open:
                    check = re.search(patron, letra)
                    if check:
                        dictionario[str(os.path.basename(file))] = check.group()
            except (IOError, OSError) as e:
                print(f"Error accessing file '{file}': {e}")
    except (KeyboardInterrupt, SystemExit):
        print("\nBusqueda cancelada por el usuario.")
    fin = time.time()
    return dictionario, round(fin - inicio, 2)


def inicio(duration, lista):
    """
    Prints the search results in a formatted table.

    Args:
        duration (float): The elapsed search duration in seconds.
        lista (dict): A dictionary containing filenames as keys and matched currency codes as values.
    """

    print("----------------------------------------------------\n")
    print(f"Fecha de búsqueda: {fecha.strftime('%x')}\n")
    print(f"ARCHIVO\t\t\tNRO. SERIE")
    print(f"-------\t\t\t----------")
    try:
        for a, b in lista.items():
            print(f"{a}\t\t{b}")
    except KeyError as e:
        print(f"Error accessing dictionary key: {e}")
    print(f"\nNúmeros encontrados: {len(diccionario)}.")
    print(f"Duración de la búsqueda: {math.ceil(duration)} seg.\n")
    print("----------------------------------------------------")


if __name__ == "__main__":
    diccionario, duration = searching()
    inicio(duration, diccionario)
