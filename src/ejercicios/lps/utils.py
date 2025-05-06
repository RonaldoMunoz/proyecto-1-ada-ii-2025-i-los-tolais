from tkinter import Tk
from tkinter.filedialog import askopenfilename

def normalize(s: str) -> str:
    """
    Convierte a minúsculas y elimina todo lo que no sea letra o dígito.
    """
    return ''.join(ch.lower() for ch in s if ch.isalnum())

def choose_input_file() -> str:
    """
    Abre un diálogo para elegir un archivo y devuelve la ruta.
    """
    Tk().withdraw()
    filename = askopenfilename(title="Selecciona el archivo de entrada")
    if not filename:
        raise FileNotFoundError("No se seleccionó ningún archivo.")
    return filename