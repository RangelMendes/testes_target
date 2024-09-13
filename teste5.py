# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma nova string vazia
    resultado = ''
    # Percorre a string original do final para o começo
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# Exemplo de uso
entrada = input("Digite uma string para inverter: ")
string_invertida = inverter_string(entrada)
print("String invertida:", string_invertida)
