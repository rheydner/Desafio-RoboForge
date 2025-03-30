from math import sqrt, acos, degrees, isclose

def distancia(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("Digite as coordenadas dos três pontos (x y):")
try:
    p1 = tuple(map(float, input("Ponto 1: ").split()))
    p2 = tuple(map(float, input("Ponto 2: ").split()))
    p3 = tuple(map(float, input("Ponto 3: ").split()))
    if len(p1) != 2 or len(p2) != 2 or len(p3) != 2:
        raise ValueError("Cada ponto deve ter duas coordenadas (ex: 10 13).")
except ValueError as e:
    print(f"Erro: {e}")
    exit()

#Calcular os lados (Parte 3)
a = distancia(p2, p3)
b = distancia(p1, p3)
c = distancia(p1, p2)
print(f"\nLados calculados: {a:.2f}, {b:.2f}, {c:.2f}")

# Verifica se é um triângulo válido
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Os pontos não formam um triângulo válido.")
else:
    #Parte 4: Ângulos
    angulo_A = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angulo_B = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angulo_C = degrees(acos((a**2 + b**2 - c**2) / (2 * a * b)))
    print(f"Ângulos: {angulo_A:.2f}°, {angulo_B:.2f}°, {angulo_C:.2f}°")

    #Parte 5: Perímetro e área
    perimetro = a + b + c
    s = perimetro / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Perímetro: {perimetro:.2f}")
    print(f"Área: {area:.2f}")

    #Parte 6: Classificação por lados
    if isclose(a, b) and isclose(b, c):
        tipo_lado = "equilátero"
    elif isclose(a, b) or isclose(b, c) or isclose(a, c):
        tipo_lado = "isósceles"
    else:
        tipo_lado = "escaleno"
    print(f"Tipo (lados): {tipo_lado}")

    #Parte 7: Classificação por ângulos
    if any(isclose(angulo, 90, abs_tol=1e-9) for angulo in [angulo_A, angulo_B, angulo_C]):
        tipo_angulo = "retângulo"
    elif any(angulo > 90 for angulo in [angulo_A, angulo_B, angulo_C]):
        tipo_angulo = "obtusângulo"
    else:
        tipo_angulo = "acutângulo"
    print(f"Tipo (ângulos): {tipo_angulo}")