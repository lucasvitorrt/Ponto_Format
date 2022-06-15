ajst = []


def matriz(n_linhas, n_colunas):
    return [[0]*n_colunas for _ in range(n_linhas)]


# Adiciona valor decimal em vetor de mesmo tamando de valor total
def serializa(valor, total):
    ajst.clear()
    if len(valor) <= len(total):
        k = int(len(total) - len(valor))
        for i in range(0, len(total)):
            ajst.append(0)
        for j in range(0, len(valor)):
            ajst[k] = str(valor)[j]
            k = k + 1
    else:
        print('contador > valor max')
