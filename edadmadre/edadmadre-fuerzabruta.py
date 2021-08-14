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

while(sum(hijas) != mama):
    mama += 1
    hijas = [h+1 for h in hijas]

end = time.time()

print(f"La mamá tendra {mama} y se tardó en calcular {end - start}")