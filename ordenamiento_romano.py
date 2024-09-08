# Flor Jazmin Mayon Cisneros - 22760045
# Lenguajes y autómatas II
# Ordenamiento de palabras de acuerdo a numeros romanos encontrados en dichas palabras

""" 
Se definen las letras romanas y su valor en el sistema decimal en un diccionario
y la Lista de las palabras para analizar.
"""
orden_romano = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
palabras = ["miel", "papa", "ximena", "hola", "flor", "pixel"] 


"""
Se crea una funcion para descartar las palabras que no tienen letras romanas.
Se itera sobre cada elemento de la lista "palabras" y verifica si alguna letra
está en "orden_romano", si es True se añade a "palabras_validas".
"""
def descartar_palabras(palabras):
    palabras_validas = [] # Almacena las palabras con formato romano

    for i in palabras: 
        if any(letra.upper() in orden_romano for letra in i):
            palabras_validas.append(i)
    return palabras_validas


""" 
Se extraen las letras romanas de la nueva lista anterior "palabras_validas".
"""
def extraer_letras_romanas(palabras_validas):
    letras_romanas_encontradas = {} # Diccionario para asociar las palabras y sus letras encontradas
    
    for i in palabras_validas:
        letras_palabras = [letra.upper() for letra in i if letra.upper() in orden_romano]
        if letras_palabras:
            letras_romanas_encontradas[i] = letras_palabras
    
    return letras_romanas_encontradas


"""
Convierte las letras romanas en su valor decimal, descarta las que no estan en orden correcto.
"""
def convertir_romano_individual(secuencia):
    total = 0 # Para la suma de numeros romanos
    prev_value = float('inf') # Para que el valor romano sea menor al inicio.

    for i in secuencia:
        valor = orden_romano[i] # Asigna el valor del num romano en la iteración
        if valor > prev_value: # Si el valor del num romano actual es > que el anterior, no es válido
            break
        total += valor  # El valor se va sumando al total
        prev_value = valor # Se actualiza

    return total

"""
Procesa el dic "letras_romanas_encontradas" y convierte cada secuencia en su valor decimal usando 
la funcion anterior.
"""
def procesar_letras_romanas(letras_romanas_encontradas):
    resultados = {}

    for palabra, secuencia in letras_romanas_encontradas.items():
        valor_decimal = convertir_romano_individual(secuencia) # llama a la funcion para convertir en su valor decimal
        resultados[palabra] = valor_decimal # Asocia la palabra y su valor decimal

    return resultados


"""
Ordena el diccionario "resultados"
"""
def ordenar_por_valor_decimal(resultados):
    resultados_ordenados = dict(sorted(resultados.items(), key = lambda item: item[1], reverse = True ))

    return resultados_ordenados


def main():
    # Palabras que contien letras romanas
    palabras_validas = descartar_palabras(palabras)
    print("\nPalabras con letras romanas:", palabras_validas)

    # Imprime las palabras con las letras romanas separadas
    letras_romanas_encontradas = extraer_letras_romanas(palabras_validas)
    print("\nLetras Romanas Encontradas en cada palabra: ", letras_romanas_encontradas)

    
    resultado_final = procesar_letras_romanas(letras_romanas_encontradas)
    print("\nValores decimales de letras validas(desordenado): ", resultado_final)

    resultado_ordenado = ordenar_por_valor_decimal(resultado_final)
    print("\nPalabras de mayor a menor en sistema decimal(ordenado)", resultado_ordenado)
    

if __name__ == "__main__":
    main()

    # .upper convierte caracteres en mayuscula
    # .append añadir elementos al final de la lista