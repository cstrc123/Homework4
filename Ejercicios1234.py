

#Ejercicio 1

def contar_caracteres(cadena):
    letras = 0
    numeros = 0
    caracteres_especiales = 0
    
    for caracter in cadena:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:
            caracteres_especiales += 1
    
    print("Letras =", letras)
    print("Números =", numeros)
    print("Caracteres especiales =", caracteres_especiales)

cadena = input("Ingrese una cadena de texto: ")
contar_caracteres(cadena)

#Caso de prueba:
#Entrada: "Hola mundo 123!$"
#Salida esperada:
#Letras = 8
#Números = 3
#Caracteres especiales = 3

#Ejecución exitosa:
#Ingrese una cadena de texto: Hola mundo 123!$
#Letras = 8
#Números = 3
#Caracteres especiales = 3


#Ejercicio 2

def contar_apariciones(cadena):
    apariciones = {}
    for caracter in cadena:
        if caracter in apariciones:
            apariciones[caracter] += 1
        else:
            apariciones[caracter] = 1
    print(apariciones)

cadena = input("Ingrese una cadena de texto, números o símbulos:")
contar_apariciones(cadena)

#Caso de prueba:

#Entrada: "hola mundo"
#Salida esperada: {'h': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

#Ejecución:
#Ingrese una cadena de texto, números o símbulos:hola mundo
#{'h': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


#Ejercicio 3

def eliminar_elemento(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
eliminar_elemento(mi_lista, 85)
print(mi_lista)

# Caso de prueba y ejecución:

#mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
#eliminar_elemento(mi_lista, 85)
#print(mi_lista) # debería imprimir [1, 2, 3, 4, 2, 5, 7, 10, 100, 589]


#Ejercicio 4

def imprimir_lista_y_tupla(secuencia):
    lista = []
    for numero in secuencia:
        lista.append(int(numero))
    tupla = tuple(lista)
    print("Lista:", lista)
    print("Tupla:", tupla)

entrada = input("Ingrese una secuencia de números separados por comas: ")
numeros = entrada.split(",")
imprimir_lista_y_tupla(numeros)

#Caso de prueba: 

#Entrada: "1,2,3,4,5"
#Salida esperada:
#Lista: [1, 2, 3, 4, 5]
#Tupla: (1, 2, 3, 4, 5)

#Ejecución:

#Ingrese una secuencia de números separados por comas: 1,2,3,4,5
#Lista: [1, 2, 3, 4, 5]
#Tupla: (1, 2, 3, 4, 5)