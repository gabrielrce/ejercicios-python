def run():
    premios = []
    i = 0
    x = int(input('Escribe la cantidad de ganadores de la loteria: '))
    for i in range(x):
        premios.append(int(input("Introduce un número ganador: ")))
    premios.sort()
    print("Los números ganadores son " + str(premios))


if __name__ == '__main__':
    run()
