lista_de_dados = []

def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
    return int(tamanho_em_bytes)/ (2**10) **2

with open('new_data/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((usuario, tamanho_em_disco))
print(lista_de_dados)