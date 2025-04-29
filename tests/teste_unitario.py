def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro de divisão por zero'


# Testes unitários (sem usar bibliotecas externas)
def executar_testes():
    # Teste de soma
    resultado = somar(2, 3)
    print(f'Teste de soma: {"Passou" if resultado == 5 else "Falhou"}')

    # Teste de subtração
    resultado = subtrair(5, 3)
    print(f'Teste de subtração: {"Passou" if resultado == 2 else "Falhou"}')

    # Teste de multiplicação
    resultado = multiplicar(4, 3)
    print(f'Teste de multiplicação: {"Passou" if resultado == 12 else "Falhou"}')

    # Teste de divisão
    resultado = dividir(10, 2)
    print(f'Teste de divisão: {"Passou" if resultado == 5 else "Falhou"}')

    # Teste de divisão por zero
    resultado = dividir(10, 0)
    print(f'Teste de divisão por zero: {"Passou" if resultado == "Erro de divisão por zero" else "Falhou"}')


# Executar os testes
if __name__ == '__main__':
    executar_testes()
