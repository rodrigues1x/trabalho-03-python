unidadesdefato = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]

def convert(quantidade, unidadeorigem, unidadedestino):
    fator = 1
    if unidadeorigem == "bit":
        fator /=8
        unidadeorigem = "byte"
    indiceorigem = unidadesdefato.index(unidadeorigem)
    indicedestino = unidadesdefato.index(unidadedestino)
    if indiceorigem < indicedestino:
        for i in range(indiceorigem + 1, indicedestino + 1):
            fator /= 1024
    else:
        for i in range(indicedestino + 1, indiceorigem + 1):
            fator *= 1024
        if unidadedestino == "bit":
            fator = (fator/1024)*8
    
    quantidadedestino = quantidade * fator
    
    return quantidadedestino


quantidade = float(input("Digite a quantidade a ser convertida: "))
unidade_origem = input("Digite a unidade de medida de origem: ")
unidade_destino = input("Digite a unidade de medida de destino: ")


quantidade_convertida = convert(quantidade, unidade_origem, unidade_destino)
print(f"{quantidade} {unidade_origem} = {quantidade_convertida} {unidade_destino}")