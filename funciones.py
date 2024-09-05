# Ejercicios

# 2 - Crear una funcion sin parámetros que retorne el año actual como numero entero

def año() -> int : 
    """_summary_
La funcion retorna el año en el que estamos actualmente
    Returns:
        _type_: int
    """
    año_actual = print(2023)
    return año_actual

# 3 - Crear una función que dado un parametro que corresponde a un numbre, salude.

def saludo(nombre: str) -> str:
    """_summary_
Esta funcion va a devolver un saludo al parametro que se le de
    Args:
        nombre (str): _description_

    Returns:
        str: _description_
    """
    print(f"Bienvenido {nombre}!")

# 5 - Crear una funcion con parámetros que dado un radio, calcule el area de un circulo

def area_del_circulo(radio: float) -> float:
    """_summary_
Esta funcion va a devolver el area del circulo
    Args:
        radio (float): _description_

    Returns:
        float: _description_
    """
    area = 3.14 * (radio * radio)
    print(f"El area del circulo con radio {radio} es {area}")
    return area

# 9 - Crear una función con parametros que dada una palabra y una letra, retorne 
#       la cantidad de letras coincidentes que tiene esa palabra

# def palabra_y_letra(palabra: str, letra: str) -> int:
#     """_summary_
# Esta funcion devuelve la cantidad de letras que coinciden con la palabra
#     Args:
#         palabra (str): _description_
#         letra (str): _description_

#     Returns:
#         int: _description_
#     """
#     contador = 0
#     for numero in range():
        


# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras
#       y retorne dicha cantidad como un entero.

def letras_de_una_palabra(palabra: str) -> int:
    """_summary_
Esta funcion va a retornar la cantidad de letras que tenga la palabra
    Args:
        palabra (str): _description_

    Returns:
        str: _description_
    """
    contador_caracteres = 0

    for caracter in palabra:
        contador_caracteres += 1

        return contador_caracteres
    
# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego
#       calculará cual de ellas tiene mayor cantidad de letras y tendra que imprimirla en consola
#       junto con la cantidad de letras que posee

def tres_palabras():
    
    cantidad_caracteres_mayor = None
    palabra_mas_larga = None

    for i in range(3):
        palabra = input(f"Ingrese la {i + 1}° palabra: ")
        cantidad_letras_palabra_actual = letras_de_una_palabra(palabra)
        if cantidad_caracteres_mayor == None or cantidad_letras_palabra_actual > cantidad_caracteres_mayor:
            cantidad_caracteres_mayor = cantidad_letras_palabra_actual
            palabra_mas_larga = palabra

    texto = f"La palabra con mas cantidad de caracteres es: {palabra_mas_larga} y tiene un total de {cantidad_caracteres_mayor} caracteres."
    print(texto)

año()
saludo("jose")
area_del_circulo(7)
letras_de_una_palabra("asas")
tres_palabras()

