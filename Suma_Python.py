def sumar_dos_numeros():
    try:
        # Pedir el primer número
        numero1 = float(input("Ingrese el primer número: "))
        # Pedir el segundo número
        numero2 = float(input("Ingrese el segundo número: "))
        # Suma
        suma = numero1 + numero2
        # Mostrar resultado
        print(f"{numero1} + {numero2} es: {suma}")
        return suma
    except ValueError:
        print("Error: Debes ingresar números válidos")
        # De nuevo si  sale error
sumar_dos_numeros()
