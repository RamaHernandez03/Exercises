

def equal_password(invented_password):

    while True:
        print("Introduci la contraseña correcta")
        user_password = input("Introduzca la contraseña: ")
        if user_password == invented_password:
            print("Contraseña aceptada :)")
            return False
        
'''Escribir una función que reciba un número natural e imprima todos los números
impares que hay hasta ese número.'''

def n_primos(natural):

    cant_numeros = int(natural)
    numeros_printear = []

    for i in range(0, cant_numeros + 1):
        if (i%2 != 0):
            numeros_printear.append(i)
    
    print(numeros_printear)

'''a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
    es una subcadena de 'subcadena'.
    b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
    debe devolver 'gnome'.'''

def es_subcadena(str1, str2):

    if str2 in str1:
        print("Es una subcadena")
    else:
        print("No es una subcadena")

    if str1 < str2:
        print(f"La que va primero alfabéticamente es: '{str1}'")
        return str1
    else:
        print(f"La que va primero alfabéticamente es: '{str2}'")
        return str2
    
'''Ejercicio 7.3. Campaña electoral
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
el mensaje Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.'''

#a,c)

def vote_por_mi(tupla):

    for nombre, genero in tupla:
        if genero == 'f':
            print(f'Estimada, Vote por mi {nombre}')
        else:
            print(f'Estimado, Vote por mi {nombre}')

#b,c)

def mensaje_anterior(tupla, p, n):

    cantidad = int(n)
    posicion = int(p)

    for i in range(posicion, cantidad + posicion):
        if i < len(tupla):
            nombre, genero = tupla[i]
            if genero == 'f':
                print(f'Estimada, Vote por mi {nombre}.')
            else:
                print(f'Estimado, Vote por mi {nombre}.')

'''Ejercicio 7.9. Escribir una función empaquetar para una lista, donde epaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
, (1, 2), (3, 2)].'''

def empaquetar(lista):

    resultado = []
    contador = 1
    elemento_actual = lista[0]

    for i in range(lista[1:]):
        if i == elemento_actual:
            contador += 1
        else:
            resultado.append((elemento_actual, contador))
            elemento_actual == i
            contador = 1
    
    resultado.append((elemento_actual, contador))
    return resultado

'''Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números.'''

# a)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def lista_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero) == True:
            lista_primos.append(numero)
    return lista_primos

# b)

def sumatoria_y_promedio(lista):
    
    resultado = []
    largo = len(lista)
    sumatoria = 0

    for elemento in lista:
        sumatoria += elemento
    
    promedio = sumatoria / largo

    resultado.append((sumatoria, promedio))
    return resultado

# c)

def factoriales(lista):

    resultado = []

    for elemento in lista:
        temporal = 1
        if elemento < 2:
            resultado.append(1)
        else:
            for i in range(2, elemento + 1):
                temporal = temporal * i
        resultado.append(temporal)

'''Ejercicio 7.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k.'''

# a)

def lista_de_tres(list,k):
    menores = []
    mayores = []
    iguales = []
    param = k

    for element in list:
        if element > param:
            mayores.append(element)
        elif element < param:
            menores.append(element)
        else:
            iguales.append(element)

    return [mayores,menores,iguales]

# b)

def multiplos_k(lista, k):
    son_multiplos = []

    for elemento in lista:
        if elemento%k == 0:
            son_multiplos.append(elemento)
    
    return son_multiplos

'''Ejercicio 7.8. Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modi-
fique la lista dada para invertirla, sin usar listas auxiliares.'''

def reverse_list(list):
    new_list = []
    for elemento in list:
        new_list.append(elemento)
    new_list.reverse()
    return new_list

#b) 


'''Ejercicio 7.10. Matrices.
a) Escribir una función que reciba dos matrices y devuelva la suma.
b) Escribir una función que reciba dos matrices y devuelva el producto.

c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana de-
vuelva una matriz triangular superior.

d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una
lista, son linealmente independientes o no.'''

# a)

def suma_matrix(m1,m2):
    resultado = []

    for fila1, fila2 in zip(m1,m2):
        fila_suma = []
        for elem1, elem2 in zip(fila1,fila2):
            fila_suma.append(elem1 + elem2)
        resultado.append(fila_suma)

    return resultado

# b)

def producto_matrix(m1,m2):
    resultado = []

    for fila1, fila2 in zip(m1,m2):
        fila_suma = []
        for elem1, elem2 in zip(fila1,fila2):
            fila_suma.append(elem1 * elem2)
        resultado.append(fila_suma)

    return resultado

# c)

def gauss(matrix):

    filas = len(matrix)
    columnas = len(matrix[0])

    for i in range(min(filas,columnas)):
        if matrix[i][i] == 0:
            for k in range(i+1, filas):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            else:
                continue

        for j in range(i + 1, filas):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, columnas):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


''' Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe
devolver USB.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
república argentina debe devolver República Argentina.
c) Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer
debe devolver 'Antes ayer'''

# a)

def strings(string):
    words = string.split()
    letters = ""

    for word in words:
        if word:
            letters += word[0]
    
    return letters

# b)

def first_upper(string):
    words = string.split()
    string_upper = ""
    
    for word in words:
        if word: 
            uppered = word[0].upper() + word[1:]
            string_upper += uppered + " "

    return string_upper.strip()

# c)

def only_that_letter(string):
    words = string.split()
    new_string = ""

    for word in words:
        if word:
            aux = word[0]
            if aux == "A" or aux == "a":
                new_string += word + " "
    
    return new_string.strip()

'''Ejercicio 7.12. Funciones que reciben funciones.
a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista
que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una
lista con los elementos de la lista recibida para los cuales la función recibida devuelve un
valor verdadero.'''

# a)

def map(func, list):
    new_list = []

    for e in list:
        new_list.append(func(e))
    
    return new_list

# b)

def filter(func, list):
    new_list = []

    for e in list:
        aux = func(e)
        if aux:
            new_list.append(e)
    
    return new_list

'''Ejercicio 7.11. ⋆ Plegado de un texto. 

Escribir una función que reciba un párrafo de texto (pala-
bras separadas por espacios) y una longitud n, y devuelva una lista conteniendo líneas de texto
de longitud máxima n. Las líneas deben ser cortadas correctamente en los espacios (sin cortar
las palabras). Asumir que ninguna palabra tiene longitud mayor a n.

Ejemplo:
>>> plegar('El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado
↪ un saxofón', 20)
['El viejo Señor Gómez', 'pedía queso, kiwi y', 'habas, pero le ha', 'tocado un
↪ saxofón']'''

def paragraph_n(text, n):
    words = text.split()
    result = []
    line = ""

    for word in words:
        # Si agregar la palabra supera el largo n, guardamos la línea actual
        if len(line) + len(word) + 1 > n:
            result.append(line.strip())
            line = ""

        line += word + " "

    # Agregamos la última línea si quedó algo
    if line:
        result.append(line.strip())

    return result

'''Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:

a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.

b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones.'''











        














        



    



    
    







    




    







