#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eirisdg
"""

from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, Operaciones.suma(a, b) ) )
print( "{} - {} = {}".format(b, d, Operaciones.resta(b, d) ) )
print( "{} * {} = {}".format(b, b, Operaciones.producto(b, b) ) )
print( "{} / {} = {}".format(a, c, Operaciones.division(a, c) ) )