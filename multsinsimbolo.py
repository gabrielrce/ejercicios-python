def multiplicar(a, b):
    if b < 0:
        return -multiplicar(a, -b)
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicar(a, b - 1)


if __name__ == "__main__":
    resultado = multiplicar(10, -2)
    print(resultado)
    resultado = multiplicar(1, 2)
    print(resultado)
