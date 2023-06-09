

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

#La función "contar_caracteres" recibe como parámetro una cadena de texto y cuenta la cantidad de letras, números y caracteres especiales que contiene.
#Para ello, se inicializan tres variables: "letras", "numeros" y "caracteres_especiales" con el valor cero.
#Luego, se recorre cada caracter de la cadena con un bucle "for" y se evalúa si es una letra, un número o un caracter especial utilizando los métodos "isalpha()" y "isdigit()" de Python. 
# Si el caracter es una letra, se incrementa el contador de "letras".
#Si es un número, se incrementa el contador de "numeros".
#Si no es ni letra ni número, se incrementa el contador de "caracteres_especiales".
#Finalmente, se imprime la cantidad de letras, números y caracteres especiales encontrados en la cadena utilizando la función "print".


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

#Función contar_apariciones: Recibe una cadena de texto como parámetro y cuenta la cantidad de veces que aparece cada uno de los caracteres en la cadena. 
#Luego imprime un diccionario que contiene los caracteres como claves y la cantidad de apariciones como valores.
#Lectura de entrada: Solicita al usuario que ingrese una cadena de texto, números o símbolos.
#Llamada a la función contar_apariciones con la cadena ingresada como parámetro.


#Ejercicio 3

def eliminar_elemento(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
eliminar_elemento(mi_lista, 85)
print(mi_lista)

#Este código recibe una lista y un elemento, y remueve todas las ocurrencias del elemento en la lista.
#lista: la lista de elementos en la que se desea remover un elemento.
#elemento: el elemento que se desea remover de la lista.
#El código no tiene retorno. Modifica la lista de entrada eliminando todas las ocurrencias del elemento.
#El código elimina todas las ocurrencias del número 85 en la lista, y finalmente imprime la lista actualizada.


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

#La función 'imprimir_lista_y_tupla' recibe como parámetro una secuencia de números en forma de cadena, que se separa por comas utilizando el método 'split()'.
#Luego se recorre cada número en la secuencia y se agrega a una lista convertida a tipo entero. 
#Después se convierte la lista a una tupla y se imprimen en consola ambas secuencias.
#La ejecución del programa solicita al usuario ingresar una secuencia de números separados por comas.
#luego llama a la función 'imprimir_lista_y_tupla' para mostrar en consola tanto la lista como la tupla correspondientes a la secuencia ingresada.