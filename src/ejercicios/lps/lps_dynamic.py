from .utils import normalize

def solve_lps_dp(lines: list[str]) -> list[str]:
    """
    Dada la entrada, devuelve para cada línea la subcadena
    palindrómica CONTINUA más larga tras normalizar.
    """
    # Si hay un entero n al inicio, tomar las n líneas siguientes
    try:
        n = int(lines[0])
        raws = lines[1:1+n]
    except ValueError:
        raws = lines

    out = []
    for raw in raws:
        s = normalize(raw)
        m = len(s)
        if m == 0:
            out.append('')
            continue

        # P[i][j] = True si s[i..j] es palíndromo
        P = [[False]*m for _ in range(m)]
        start, max_len = 0, 1

        # Longitud 1
        for i in range(m):
            P[i][i] = True

        # Longitud 2
        for i in range(m-1):
            if s[i] == s[i+1]:
                P[i][i+1] = True
                start, max_len = i, 2

        # Longitud ≥ 3
        for length in range(3, m+1):
            for i in range(0, m-length+1):
                j = i + length - 1
                if s[i] == s[j] and P[i+1][j-1]:
                    P[i][j] = True
                    if length > max_len:
                        start, max_len = i, length

        # Extraer la subcadena óptima
        out.append(s[start:start+max_len])

    return out