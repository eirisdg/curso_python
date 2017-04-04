#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eirisdg
"""
import random
import math


def leer_numero(ini, fin, mensaje):
    numero = -1
    while numero < ini or numero > fin or numero is -1:
        numero = int(raw_input(mensaje))
    return numero


def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:")

    lista = []
    for i in range(0,numeros,1):
        num = random.uniform(0,101)
        num_red = None
        if modo == 1:
            num_red = math.ceil(num)
        elif modo == 2:
            num_red = math.floor(num)
        elif modo == 3:
            num_red = round(num)
        print("{} ==> {}".format(num, num_red))
        lista.append(random.uniform(0,101))

    return lista


generador()