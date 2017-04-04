#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eirisdg
"""

class Operaciones():

    @staticmethod
    def suma(a, b):
        res = None
        try:
            res = a + b
        except TypeError:
            print("Alguno de los parametros no es un número.")
        finally:
            return res

    @staticmethod
    def resta(a, b):
        res = None
        try:
            res = a - b
        except TypeError:
            print("Alguno de los parametros no es un número.")
        finally:
            return res

    @staticmethod
    def producto(a, b):
        res = None
        try:
            res = a * b
        except TypeError:
            print("Alguno de los parametros no es un número.")
        finally:
            return res

    @staticmethod
    def division(a, b):
        res = None
        try:
            res = a / b
        except TypeError:
            print("Alguno de los parametros no es un número.")
        except ZeroDivisionError:
            print("No se puede dividir por cero.")
        finally:
            return res