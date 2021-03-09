def tipoCambio(x):
    monedaMx = 20
    return monedaMx * x


def run():
    print('Convertidor de Dolares a Pesos')
    print(' ')
    x = float(input('Escribe la cantidad de pesos que deseas convertir: '))
    res = tipoCambio(x)
    print('El resultado es: ${}' .format(res))



if __name__ == '__main__':
    run()