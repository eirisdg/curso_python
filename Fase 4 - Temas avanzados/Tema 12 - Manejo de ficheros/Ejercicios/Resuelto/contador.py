#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import open


class Contador():

    contador = None

    def __init__(self):
        self.cargar()

    def cargar(self):
        try:
            fichero = open("contador.txt", "r")
            fichero.seek(0)
            self.contador = fichero.read()
        except:
            print("El fichero no existe, se crea a cero")
            fichero = open("contador.txt", "w")
            fichero.write("0")
        finally:
            fichero.close()

    def guardar(self):
        try:
            fichero = open("contador.txt", "w")
            fichero.seek(0)
            fichero.write(str(self.contador))
        except Exception as e:
            print(str(e))
            print("Error en la escritura")
        finally:
            fichero.close()

    def variar(self):
        while True:
            var = input("¿Qué deseas hacer?\n"
                        "inc -> incrementar el valor\n"
                        "dec -> decrementar el valor\n"
                        "0 -> Salir\n")
            self.cargar()
            if var == "inc":
                self.contador = int(self.contador) + 1
            elif var == "dec":
                self.contador = int(self.contador) - 1
            elif var == "0":
                print(self.contador)
                self.guardar()
                return
            else:
                pass
            print(self.contador)
            self.guardar()

    def __del__(self):
        pass

c = Contador()

c.variar()