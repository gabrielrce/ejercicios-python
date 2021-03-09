def run():
    currencies = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    currency = input("Introduce una divisa: ")
    print(currencies.get(currency.title(), "La divisa no está."))


if __name__ == '__main__':
    run()
