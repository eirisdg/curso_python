#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import open
import pickle

class Personaje():
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

class Gestor():

    personajes = []

    def __init__(self):
        self.cargar()

    def cargar(self):
        try:
            fichero = open("personajes.pckl", "rb")
            fichero.seek(0)
            self.personajes = pickle.load(fichero)
        except Exception as e:
            fichero = open("contador.txt", "wb")
        finally:
            fichero.close()

    def guardar(self):
        try:
            fichero = open("personajes.pckl", "wb")
            fichero.seek(0)
            pickle.dump(self.personajes, fichero)
        except:
            print("No se puede escribir en el fichero")
        finally:
            fichero.close()

    def anadir(self, p):
        self.personajes.append(p)
        self.guardar()

    def mostrar(self):
        for i in self.personajes:
            print("{} => {} | {} | {} | {}".format(i.nombre, i.vida, i.ataque, i.defensa, i.alcance))

p1 = Personaje("Arquero", 6, 7, 6, 9)
p2 = Personaje("Guerrero", 9, 9, 9, 3)
p3 = Personaje("Caballero", 8, 8, 7, 4)

g = Gestor()
g.anadir(p3)

g.guardar()

g.mostrar()