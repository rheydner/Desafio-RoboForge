import random #Biblioteca para gerar números aleatórios para a segunda parte do problema

#Definir se o numero é ou não primo e retornar True ou False
def numero(primo):
    if primo <= 1:
        return False
    if primo == 2:
        return True
    if primo % 2 == 0: #Números pares fora o 2 não são primos
        return False
    for i in range(3, int(primo**0.5)+ 1, 2):
        
        if primo % i == 0:
            return False
    return True


#Pegar uma lista de 10 numeros aleatórios e multiplicar somente os primos
def numeros_aleatorios():
    return random.getrandbits(8)  # gera numeros aleatorios até x quantidades de bits que é definido no getrandbits()

#Gera a lista com 10 números aleatórios dentro do limite de 8 bits(0 a 255)
lista_numeros = [numeros_aleatorios() for r in range(10)]

#Filtra os numeros primos da lista
def filtra_primos(lista):
    return [n for n in lista if numero(n)]

#Multiplica os primos
def multiplicar_primos(lista_primos):
    if not lista_primos:
        return 0  #Retorna 0 se não houver primos
    resultado = 1
    for p in lista_primos:
        resultado *= p
    return resultado

primos = filtra_primos(lista_numeros)
produto = multiplicar_primos(primos)
num =  int(input("Digite um número: "))
resultado = numero(num)
print("Retorna", numero(num))
print("Números gerados:", lista_numeros)
print("Primos encontrados:", primos)
print("Produto dos primos:", produto)



