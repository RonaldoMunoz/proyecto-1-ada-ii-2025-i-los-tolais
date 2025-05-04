def party(lines):
    """
    Para cada caso:
     - lee m, la matriz de supervisión y los pesos
     - construye el árbol
     - aplica DP de Independent Set en árbol
     - reconstruye el conjunto óptimo de invitados
     - devuelve la línea de salida (bits + suma)
    """
    idx = 0
    t = int(lines[idx]); idx+=1
    answers = []
    for _ in range(t):
        m = int(lines[idx]); idx+=1
        # leer matriz m×m
        mat = []
        for i in range(m):
            row = list(map(int, lines[idx].split())); idx+=1
            mat.append(row)
        weights = list(map(int, lines[idx].split())); idx+=1
        # construir lista de hijos y detectar raíz
        children = {i: [] for i in range(m)}
        has_parent = [False]*m
        for i in range(m):
            for j in range(m):
                if mat[i][j]==1:
                    children[i].append(j)
                    has_parent[j] = True
        root = next(i for i,hp in enumerate(has_parent) if not hp)
        # DP: para cada nodo devolvemos (excl_val, incl_val, excl_set, incl_set)
        sys.setrecursionlimit(10000)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(u):
            incl_val = weights[u]
            incl_set = {u}
            excl_val = 0
            excl_set = set()
            # procesar hijos
            for v in children[u]:
                e_excl, e_incl, set_excl, set_incl = dfs(v)
                # si u NO está: hijos pueden o no estar
                if e_incl > e_excl:
                    excl_val += e_incl
                    excl_set |= set_incl
                else:
                    excl_val += e_excl
                    excl_set |= set_excl
                # si u SÍ está: hijos NO pueden estar
                incl_val += e_excl
                incl_set |= set_excl
            return (excl_val, incl_val, frozenset(excl_set), frozenset(incl_set))

        e_excl, e_incl, set_excl, set_incl = dfs(root)
        best_set = set_incl if e_incl>e_excl else set_excl
        best_val = max(e_incl, e_excl)
        # construir línea de bits
        bits = ['1' if i in best_set else '0' for i in range(m)]
        answers.append(' '.join(bits) + f' {best_val}')
    return answers