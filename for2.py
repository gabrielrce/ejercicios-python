# el n+1 es para que no termine la iteracion antes del numero asignado
def run():
    n = int(input("Introduce un número entero positivo: "))
    for i in range(1, n+1, 2):
        print(i, end=", ")


if __name__ == '__main__':
    run()
