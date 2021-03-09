def run():
    print("Comienzo")
    cuenta = 0
    for i in range(1, 6):
        if i % 2 == 0:
            cuenta = cuenta + 1
    print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")


if __name__ == '__main__':
    run()
