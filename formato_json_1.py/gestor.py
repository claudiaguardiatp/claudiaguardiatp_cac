import json
from libros import *
import os
import pathlib

class gestor:
    AGREGAR_LIBRO = 1
    CONSULTAR_LIBRO = 2
    SALIR = 0
    
    def _init_(self):
        self._libros = []
        self.recuperar_libros('libros.json')
        
    def _del_(self):
        self.almacenar_libros('libros.json')
    
    @property
    def libros(self):
        return self._libros
    @libros.setter
    def libros(self, valor):
        self._libros = valor
    @libros.deleter
    def libros(self):
        del self._libros
    
    def recuperar_libros(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                datos = json.load(archivo)
            for lib in datos['libros']:
                self.libros.append("desde_json"(lib))
                
    
    def almacenar_libros(self, ruta):
        with open(ruta, 'w') as archivo:
           json.dump({'libros':self.libros}, archivo, cls=Libro_Encoder, indent=4)
              
            
    
    def agregar_libros(self):
        os.system('cls')
        print('                      agregar libro')
        isbn = input('isbn: ')
        titulo = input('titulo: ')
        autor = input('autor: ')        
        self.libros.append(Libro(isbn,titulo,autor))
    
    def consultar_libros(self):
        os.system('cls')
        print('                      consultar libros')
        if len(self.libros == 0):
            print('No hay libros registrados.')
        else:
            for lib in self.libros:
              print(f'{lib}')
              print('~', *50)
    
    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print: (                gestor
{gestor.AGREGAR_LIBRO} agregar libro
{gestor.CONSULTAR_LIBRO} consultar libro
{gestor.SALIR}) salir
        opc = input('seleccione una opcion')
        try:
            opc = int(opc)
        except:
            opc = -1
        if opc == gestor.AGREGAR_LIBRO:
            self.agregar_libro()
        elif opc == gestor.CONSULTAR_LIBROS:
            self.consultar_libros()
        elif opc == gestor.SALIR:
            continuar = False
        else:
            os.system('cls')
            print('Opcion no valida.')
        input('presiona enter para continuar.')
    input('presiona enter para salir.')