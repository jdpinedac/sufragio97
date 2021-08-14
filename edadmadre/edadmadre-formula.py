#!/usr/bin/env python3
# Cálculo de la edad de la madre cuando llegue a la edad que
# es la sumatoria de las edades de las hijas
# Diseñado por:
# Jairo Patarroyo <patarroyos@gmail.com>
# Implementado por:
# Juan Pineda <juan.david.pineda@gmail.com>

import time

start = time.time()
mama = 55
hijas = [15, 7, 21]

edad = mama + ((mama - sum(hijas))/2)

end = time.time()

print(f"La mamá tendra {edad} y se tardó en calcular {end - start}")