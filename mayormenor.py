def run():
    lista = []
    cantidad = int(input("Cantidad: "))
    mayor = 0
    menor = 0
    i = 1
    while (cantidad > 0):
        numero = int(input("Numero: " + str(i) + ": "))
        lista.append(numero)
        i = i + 1
        cantidad = cantidad-1
    mayor = max(lista)
    menor = min(lista)
    print("Lista: ", lista)
    print("El numero mayor es: {}".format(mayor))
    print("El num menor es: ", menor)


if __name__ == '__main__':
    run()
