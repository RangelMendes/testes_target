def pertence_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    
    return False

# Solicitar entrada do usuário
try:
    numero = int(input("Informe um número: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, informe um número inteiro válido.")
