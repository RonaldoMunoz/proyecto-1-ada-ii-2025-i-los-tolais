import sys
from tkinter.filedialog import askopenfilename
from tkinter import Tk

from ejercicios.lps.lps_dynamic import solve_lps_dp
from ejercicios.lps.lps_brute import solve_lps_brute
from ejercicios.lps.lps_voraz import solve_lps_greedy

def main():
    Tk().withdraw()
    file = askopenfilename(title="Selecciona el archivo de entrada")
    if not file:
        print("No se seleccionó archivo.", file=sys.stderr)
        return
    with open(file, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Detectar si es LPS (n seguido de n líneas)
    is_lps = False
    try:
        n0 = int(lines[0])
        if len(lines) - 1 == n0:
            is_lps = True
    except ValueError:
        pass

    if is_lps:
        # Selecciona el método aquí:
        #results = solve_lps_brute(lines) # programación dinámica
        #results = solve_lps_dp(lines)  # fuerza bruta
        results = solve_lps_greedy(lines) # voraz

        for result in results:
            print(result)

if __name__ == '__main__':
    main()
