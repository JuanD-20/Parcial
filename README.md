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

## Aqui esta el resultado del programa:

Para el caso 1, un solo caracter:

![89e6b8840dd1f08b20928d59dd081004](https://github.com/JuanD-20/Parcial/assets/107315767/fd20d099-1a6f-4ded-9eef-04447213267f)

Para el caso 2, una palabra:

![34dcc5b3fb1004c7273cc4763054e246](https://github.com/JuanD-20/Parcial/assets/107315767/d6266593-05c4-45a0-a908-636bb44cde80)

## Como usar el repositorio:

La manera mas facil es clonar el repositorio, la forma mas sencila de hacer esto es mediante [Git Hub Desktop](https://desktop.github.com/).

Una vez descargado lo abrimos he iniciamos seción y iremos a el boton que dice "File" y le daremos clic en "clone repository".

![8a43ccc9cf839a4c2aa2d07b7d971dec](https://github.com/JuanD-20/Parcial/assets/107315767/d6917dd5-5631-4e00-810e-793cd3a05896)

Luego iremos a donde dice URL y pegaremos la URL del repositorio y seleccionamos en que parte de nuestro PC queremos que se clone y damos clic en clone.

![ce7efe3d85195bc311c0ddf04107efd8](https://github.com/JuanD-20/Parcial/assets/107315767/fcd23b80-029f-4905-8411-90e5901788a9)

Ahora podemos ver el repositorio en la ubicación que seleccionamos para clonarlo y ya podremos usarlo y modificarlo.

![863b5e83962e8dc380da18a951bceb98](https://github.com/JuanD-20/Parcial/assets/107315767/54cb205d-4d6c-4793-9cfb-5faf86f3cdc6)



