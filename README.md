# Parcial

## Operaciones.
En el archivo hay dos funciones aparte del main/menú.
aqui se explica brevemente lo que hace cada una:

### char_to_ascii_and_binary(char): 
Esta función toma un solo carácter como entrada (char) y lo convierte a su valor ASCII y representación binaria. Utiliza la función ord para obtener el valor ASCII y la función de formato para convertir el valor ASCII a una representación binaria de 8 bits.

### word_to_binary_representation(word): 
Esta función toma una palabra como entrada (palabra) y procesa cada carácter de la palabra. Llama a la función char_to_ascii_and_binary para cada carácter, imprimiendo el valor ASCII y la representación binaria de cada carácter. Luego concatena las representaciones binarias con espacios intermedios.

### main(): 
Esta es la función principal que implementa el sistema de menú. Presenta al usuario un menú para elegir entre dos opciones: ingresar un solo carácter o ingresar una palabra. Dependiendo de la elección del usuario, llama a las funciones apropiadas (char_to_ascii_and_binary o word_to_binary_representation). Si el usuario ingresa una opción no válida, imprime un mensaje de error y sale del programa.

## Libreria.

### Sys
Sys es la unica libreria usada en el prgrama y basicamente hace lo siguiente:

#### sys: 
es un módulo integrado en Python que proporciona acceso a algunas variables y funciones relacionadas con el intérprete de Python.

#### Función sys.exit(): 
Se utiliza para salir del programa. Cuando llama a sys.exit(), genera la excepción SystemExit que finaliza el programa. En este programa, se usa para salir del programa si el usuario ingresa una opción no válida en el menú.

Aqui esta el resultado del programa:

![34dcc5b3fb1004c7273cc4763054e246](https://github.com/JuanD-20/Parcial/assets/107315767/d6266593-05c4-45a0-a908-636bb44cde80)
