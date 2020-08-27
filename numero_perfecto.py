numero = int(input("digite un numero: "))
def numero_perfecto():
    contador = 0
    for i in range(1, numero):
        if numero % i == 0:
            contador += i
    if contador == numero:
        print(f"el numero: {numero} es perfecto")
        return True
    else:
        print(f"el numero: {numero} no es perfecto")
    return False                


def main ():
    numero_perfecto()

if __name__ == "__main__":
    main()    