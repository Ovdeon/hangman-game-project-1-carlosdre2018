# Juego del ahorcado

Hola jugadores, les damos la bienvenida al juego del ahorcado.
Se presenta una interfaz y un codigo simples para poder jugar este clasico juego considerando varios escenarios.


## Consideracioness
- Se puede cometer hasta 6 errores.
- No se descartan puntos si una letra correcta se vuelve a digitar.
- Tampoco se descartaran si se digita más de una letra o número.
- Las unicas entradas validas seran letras o números, no simbolos ni conjunto de letras o números o ambos.
- Para terminar el juego será necesario que se digite N en la pregunta, caso contrario se volverá a jugar.
- La palabra u oración a elegir se debera de sacar mediante el archivo .json [data]
- El orden de las partes del ahorcado son: cabeza, cuello, brazo izquierdo, brazo derecho, pierna derecha, pierna izquierda
- El programa reconoce tildes y mayusculas por lo que no lo toma como distinto, es decir que una letra mayuscula será considerada tambien como minuscula.
- El punto anterior tambien incluye las tildes.

## Bonus
- write tests.

### What was your creative process:
Se usaron variables de cadena, enteras y booleanas asi como dos funciones para poder resolver este problema.
- La variable desplaz se usa para verificar si una letra se encuentra en la oracion o palabra a adivinar.
- Las variables booleanas se usaron para identificar la entrada o no a condicionales.
- En la lista corrects se añaden todas las letras que ya se adivinaron correctamente.
- La variable verif sirve para identificar cuando se ha ganado el juego o no.
- No se han usado librerias externas a las ya incluidas en python por defecto  como json o random, por lo tanto no se requiere un requirement.txt
 
