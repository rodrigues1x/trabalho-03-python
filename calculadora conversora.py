UNITS = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]

def convert(quantidade, unidade_origem, unidade_destino):
    fator = 1
    indice_origem = UNITS.index(unidade_origem)
    indice_destino = UNITS.index(unidade_destino)
    if indice_origem < indice_destino:
        for i in range(indice_origem + 1, indice_destino + 1):
            fator /= 1024
    else:
        for i in range(indice_destino + 1, indice_origem + 1):
            fator *= 1024
    
    quantidade_destino = quantidade * fator
    
    return quantidade_destino


quantidade = float(input("Digite a quantidade a ser convertida: "))
unidade_origem = input("Digite a unidade de medida de origem: ")
unidade_destino = input("Digite a unidade de medida de destino: ")


quantidade_convertida = convert(quantidade, unidade_origem, unidade_destino)
print(f"{quantidade} {unidade_origem} = {quantidade_convertida} {unidade_destino}")