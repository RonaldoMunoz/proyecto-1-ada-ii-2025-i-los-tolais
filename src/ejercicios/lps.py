def normalize(s):
    return ''.join(ch.lower() for ch in s if ch.isalnum())

def lps_dp(s):
    """
    Construye la tabla DP L donde L[i][j] = longitud de la LPS en s[i..j].
    Devuelve la tabla L.
    Complejidad: O(n^2) tiempo, O(n^2) espacio.
    """
    n = len(s)
    L = [[0]*n for _ in range(n)]
    # cada carácter aislado es palíndromo de longitud 1
    for i in range(n):
        L[i][i] = 1
    # llenar para longitudes crecientes
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                L[i][j] = 2 + (L[i+1][j-1] if length>2 else 0)
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])
    return L

def lps_backtrack(s, L, i, j):
    """
    Reconstruye una LPS óptima a partir de la tabla L.
    """
    if i>j:
        return ''
    if i==j:
        return s[i]
    if s[i]==s[j]:
        return s[i] + lps_backtrack(s, L, i+1, j-1) + s[j]
    # elegir el mejor de omitir i o j
    if L[i+1][j] >= L[i][j-1]:
        return lps_backtrack(s, L, i+1, j)
    else:
        return lps_backtrack(s, L, i, j-1)

def solve_lps(lines):
    """
    Lee n cadenas, para cada una imprime su LPS (normalizada y en minúsculas).
    """
    n = int(lines[0])
    out = []
    for k in range(1, n+1):
        raw = lines[k].rstrip('\n')
        s = normalize(raw)
        if not s:
            out.append('')
            continue
        L = lps_dp(s)
        p = lps_backtrack(s, L, 0, len(s)-1)
        out.append(p)
    return out
