# Problema de la Madre y las Hijas.

La tarde del 13 de Agosto de 2021, Jairo Patarroyo pone el siguiente problema en el grupo de whatsapp del colegio:

"Una madre tiene 55 años. Tiene 3 hijas. La primera tiene 15 años, la segunda tiene 7 años, la tercera tiene 21 años. ¿En cuántos años la edad de la madre será igual a la suma de las edades de sus hijas?"

Existen dos formas de enfrentar este problema. La primera es a partir de fuerza bruta y la segunda a partir del modelo algebraico que subyace en el problema. A partir de este este problema, se desarrollan varias soluciones, con algunas variantes para experimentar que comportamientos hay en el software que obtiene la solución. 

## Que se podrá encontrar en este repositorio

En este repositorio se encontrarán los siguientes programas:

- La solución de fuerza bruta
- La solución con la fórmula
- Una solución tratando de escalar el problema no a 3 hijas sino a decenas de hijas.
- Mostrando el problema de la eficiencia que podría tener pero usando a Gauss.

## Uso de este software


## Preguntas, respuestas e ideas generadas
- Pregunta por Andrés Felipe Estrada: No es mejor solicitarle al propio sistema operativo (y no al programa) que mida el tiempo de ejecución?
- Respuesta por Juan David Pineda: lo que pasa es que estarías incluyendo tiempo de carga del binario en memoria y en este caso lo que queremos medir es el tiempo de ejecución del algoritmo pero lo que vos decis se hace con cierta frecuencia para medir rendimentos de programas completos, y más ahora en nube. Ahora, ese tiempo no es determinista tampoco, ya que vos no tenes como saber el estado del sistema y depende incluso de las políticas implementadas en el scheduler del sistema operativo aunque la verda dla verdad, tampoco es una buena manera de medirlo, la manera real de medirlo es mirando el orden del algoritmo el mio es cuadratico mientras que el de patarroyo es lineal estoy viendo es como modifico el ejercicio para que sea escalable con miles de hijas pero obviamente no da porque la edad de la mamá es muy pequeña vs el número de hijas que le iba a poner como para que la suma de las edades de las hijas fuera menor que la de la mamá. 
- Idea de Gabriel Porras: Poder empezar con 3 hijas e ir aumentado n ( número de hijas) hasta que la mamá sea más o menos 100 Es un caso hipotético nada más
Eso ayudaría a observar cómo mejora el modelo mientras n crece. 
- Respuesta Juan David Pineda: Si, pero sigue siendo muy pequeño, sigue estando en el mundo de los segundos, creo que la mejor manera de ilustrar el efecto de la fuerza bruta es usando la fórmula de Gauss para sumar números vs, sumarlos secuencialmente. Sería como el equivalente sin tener la restricción de la edad de la madre
Habría que pensar en otras variables que tengan más sentido para llegar a un número alto
- Respuesta Juan David Pineda: Si, por eso para no echarle muchas cabeza pensé en n(n+1)/2
