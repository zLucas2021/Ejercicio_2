"""
Ejercicio 2:
 
Escribí una función que reciba la ruta de un archivo de texto (.txt) y devuelva un diccionario con:
- La cantidad total de líneas.
- La cantidad de líneas vacías.
- La cantidad de líneas que contienen solo espacios.
- La cantidad de líneas que tienen contenido.
 
Resultado esperado:
"total_lineas": 13
"lineas_vacias": 2
"lineas_solo_espacios": 3
"lineas_con_contenido": 8
"""

"""
@param ruta_archivo: Ruta al archivo de texto que se desea analizar.
@return: Diccionario con las siguientes claves:
    - total_lineas: Número total de líneas en el archivo.
    - lineas_vacias: Número de líneas completamente vacías (solo contienen un salto de línea \n).
    - lineas_solo_espacios: Número de líneas que contienen únicamente espacios o tabulaciones.  
    - lineas_con_contenido: Número de líneas que contienen texto o cualquier otro contenido no vacío.
"""
def analizar_lineas(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    total = len(lineas)
    vacias = sum(1 for linea in lineas if linea == '\n')
    solo_espacios = sum(1 for linea in lineas if linea.strip() == '' and linea != '\n')
    contenido = total - vacias - solo_espacios

    archivo.close()
    return {
        "total_lineas": total,
        "lineas_vacias": vacias,
        "lineas_solo_espacios": solo_espacios,
        "lineas_con_contenido": contenido
    }


resultado = analizar_lineas("ejercicio.txt")
print(resultado)