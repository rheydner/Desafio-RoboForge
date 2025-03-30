# Desafio 0

def entrada(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return "#"


num =  int(input("Digite um número: "))
resultado = entrada(num)
print(resultado)