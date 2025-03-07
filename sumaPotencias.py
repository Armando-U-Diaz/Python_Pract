n1 = int(input("Ingresa hasta que numero parar: "))
n = 1
e = 2
resAcum = 0
while n <= n1:
    resultado = pow(n,e)
    resAcum = resAcum + resultado
    n += 1
    e += 1
resultado = resAcum / n1
print(f"Resultado de la sumatoria: {resultado}")
