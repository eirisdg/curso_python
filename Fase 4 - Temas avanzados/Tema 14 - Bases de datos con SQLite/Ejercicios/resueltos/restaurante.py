#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
            ''')
        cursor.execute('''
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
            ''')
        print("Se ha creado la base de datos restaurante.db con las tablas 'categoria' y 'platos'")
    except sqlite3.OperationalError as e:
        cursor.execute('''
            SELECT name FROM sqlite_master
            WHERE type='table'
            AND name!='sqlite_sequence'
            ORDER BY name;
            ''')
        tablas = cursor.fetchall()
        print("Ya está creada la BD y las tablas '{}' y '{}'".format(tablas[0][0], tablas[1][0]))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexion.close()


def agregar_categoria():
    categoria = input("Introduce el nombre de la categoría a crear:")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT nombre FROM categoria WHERE nombre='{}'".format(categoria))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO categoria VALUES (null,?)", [categoria])
            conexion.commit()
        else:
            raise Exception ("Esa categoría ya se encuentra en la base de datos.")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT nombre FROM categoria")
        categorias = cursor.fetchall()
        print("Categorías disponibles:")
        contador = 0
        for c in categorias:
            contador += 1
            print("{} => {}".format(contador, c[0]))
        cat = int(input("Elije una categoría:"))
        plato = input("Introduce el nombre del plato:")
        cursor.execute("SELECT nombre FROM plato WHERE nombre='{}'".format(plato))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO plato VALUES(null,?,?)", [plato, cat])
            conexion.commit()
        else:
            raise Exception("Ese plato ya se encuentra en la base de datos.")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexion.close()

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM categoria")
        categorias = cursor.fetchall()
        for c in categorias:
            print("{}".format(c[1]))
            cursor.execute("SELECT nombre FROM plato WHERE categoria_id={}".format(c[0]))
            platos = cursor.fetchall()
            for p in platos:
                print("\t- {}".format(p[0]))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexion.close()

crear_bd()

while True:
    menu = -1
    try:
        menu = int(input('''
            Bienvenido al restaurante.
            
            1- Crear categoría
            2- Agregar plato
            3- Mostrar menu
            0- Salir
            '''))
    except:
        print("No has introducido un valor válido.")
    if menu == 1:
        agregar_categoria()
    elif menu == 2:
        agregar_plato()
    elif menu ==3:
        mostrar_menu()
    elif menu == 0:
        print("¡Hasta luego!")
        break
    else:
        print("No has introducido un valor válido.")