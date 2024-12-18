# Las listas
## TIpo de compuestos de datos que pueden almacenar distintos
# Valores (llamados iems)
# Oordenados entre entre [] y separados con comas

numeros = [1,2,3,4]
print(numeros)
datos = [4, "Una cadena", -15,3.14, "Otra cadena"]
print(datos)

# indices y Slicing
# funciona de una forma muy simillar a las cadenas de caracteres

datos = datos[-2]
print(datos)

# sumar listas
# Da como resultado una nueva lista que inluye todos los items.
numeros = numeros + [5,6,7,8]
print(numeros)

# Son modificables
pares = [0,2,4,5,8,10]
pares[3] = 6
print(pares)

# .append() Sirve para añadir un item al final de la lista
pares.append(12)
print(pares)

pares.append(7*2)
print(pares)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letritas = letras[:3]
print(letritas)

letras[:3] = []
print(letras)

# funcion Len()
letras = []
tamanio = len(letras)
print(tamanio)

# Listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)
sub = r[-1] # Ultima sublista
print(sub)

sub = r[-1][-1] # Prmera sublista, y de ella emana el primer item
print(sub)
