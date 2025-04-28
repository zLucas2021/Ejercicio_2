# Análisis de Líneas en Archivos de Texto

Este proyecto contiene una función en Python llamada `analizar_lineas`, que permite analizar un archivo de texto y obtener estadísticas sobre su contenido, como el número total de líneas, líneas vacías, líneas con solo espacios y líneas con contenido.

## Descripción

La función `analizar_lineas` recibe la ruta de un archivo de texto y devuelve un diccionario con las siguientes estadísticas:
- **`total_lineas`**: Número total de líneas en el archivo.
- **`lineas_vacias`**: Número de líneas completamente vacías (solo contienen un salto de línea `\n`).
- **`lineas_solo_espacios`**: Número de líneas que contienen únicamente espacios o tabulaciones.
- **`lineas_con_contenido`**: Número de líneas que contienen texto o cualquier otro contenido no vacío.
