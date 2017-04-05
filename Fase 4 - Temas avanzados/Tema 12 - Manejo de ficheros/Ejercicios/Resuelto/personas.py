#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import open
import pickle

class Personas():

    personas = []

    def __init__(self):
        self.cargar()

    def cargar(self):
        fichero = open("personas.txt", "r", encoding="utf8")
        fichero.seek(0)
        try:
            for l in fichero:
                id = l.split(";")[0]
                nombre = l.split(";")[1]
                apellido = l.split(";")[2]
                fecha_nac = l.split(";")[3]
                fecha_nac = fecha_nac.split("\n")[0]
                persona = {"id":id, "nombre":nombre, "apellido": apellido, "fecha_nac":fecha_nac}
                self.personas.append(persona)
        except:
            print("Error al cargar el fichero.")
        finally:
            fichero.close()
            print("Se ha cargado la lista de personas.")

    def mostrar(self):
        for p in self.personas:
            print("{} => {} {} ({})".format(p["id"], p["nombre"], p["apellido"], p["fecha_nac"]))

personas = Personas()
personas.mostrar()
