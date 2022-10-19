# 4 en linea
# Alumno: TISERA AGUILERA, Adriano Gabriel
# Legajo: 59059
# DNI: 43.484.836
# Carrera: Ingeniería Informática

import unittest
import os

class Game:
    def __init__(self):
        # Tablero
        fila_1 = [0, 0, 0, 0, 0, 0, 0]
        fila_2 = [0, 0, 0, 0, 0, 0, 0]
        fila_3 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        self.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        # Turno
        self.turno = True

        # Jugadores
        self.p1 = "Adriano"
        self.p2 = "Giuliano"
        
        self.score1 = 0
        self.score2 = 0

        self.ronda = 0

        # Ganador
        self.ganador = 0
    
    def mostrar_logo(self):
        os.system('clear')
        print('''
██╗  ██╗    ███████╗███╗   ██╗    ██████╗  █████╗ ██╗   ██╗ █████╗ 
██║  ██║    ██╔════╝████╗  ██║    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗
███████║    █████╗  ██╔██╗ ██║    ██████╔╝███████║ ╚████╔╝ ███████║
╚════██║    ██╔══╝  ██║╚██╗██║    ██╔══██╗██╔══██║  ╚██╔╝  ██╔══██║
     ██║    ███████╗██║ ╚████║    ██║  ██║██║  ██║   ██║   ██║  ██║
     ╚═╝    ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                  
                  █▓▒▒░░░Por Adriano Tisera░░░▒▒▓█
''')

    def mostrar_game_over(self):
        print('''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
''')

    def nombre_jugadores(self):
        self.mostrar_logo()
        self.p1 = input("Nombre del jugador 1: ")
        self.p2 = input("Nombre del jugador 2: ")

    def entero_valido(self, mensaje):
        while True:
            try:
                entero = int(input(mensaje))
                return entero
            except ValueError:
                print("Ingrese un número entero válido.")
            except KeyboardInterrupt:
                print("Saliendo...")
                exit()

    def solicitar_columna(self):
        while True:
            columna = int
            if self.turno:
                columna = self.entero_valido("Turno de " + self.p1 + " (🌚). Ingrese la columna en la que desea colocar su ficha: ")
            else:
                columna = self.entero_valido("Turno de " + self.p2 + " (🌝). Ingrese la columna en la que desea colocar su ficha: ")
            if columna >= 1 and columna <= 7:
                return columna
            else:
                columna = self.entero_valido("Ingrese una columna válida (1-7): ")
            return columna
    
    def colocar_ficha(self, columna):
        for fila in self.tablero:
            if fila[columna - 1] == 0:
                if self.turno:
                    fila[columna - 1] = 1
                else:
                    fila[columna - 1] = 2
                break
    
    def verificar_ganador(self):
        # Verificar filas
        for fila in self.tablero:
            for i in range(4):
                if fila[i] != 0 and fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return fila[i]
        
        # Verificar columnas
        for i in range(7):
            for j in range(3):
                if self.tablero[j][i] != 0 and self.tablero[j][i] == self.tablero[j + 1][i] == self.tablero[j + 2][i] == self.tablero[j + 3][i]:
                    return self.tablero[j][i]
        
        # Verificar diagonales
        for i in range(4):
            for j in range(3):
                if self.tablero[j][i] != 0 and self.tablero[j][i] == self.tablero[j + 1][i + 1] == self.tablero[j + 2][i + 2] == self.tablero[j + 3][i + 3]:
                    return self.tablero[j][i]
                if self.tablero[j][i + 3] != 0 and self.tablero[j][i + 3] == self.tablero[j + 1][i + 2] == self.tablero[j + 2][i + 1] == self.tablero[j + 3][i]:
                    return self.tablero[j][i + 3]
        
        # Verificar empate
        if 0 not in self.tablero[5]:
            return 3
        
        return 0

    def mostrar_tablero(self):
        print("┌──┬──┬──┬──┬──┬──┬──┐")
        print("│1 │2 │3 │4 │5 │6 │7 │")
        fila = 5
        while fila >= 0:
            print("├──┼──┼──┼──┼──┼──┼──┤")
            print((str(self.tablero[fila])).replace("1", "🌚").replace("2", "🌝").replace(" ", "│").replace("[", "│").replace("]", "│").replace("0,", "  ").replace("0", "  ").replace(",", ""))
            fila -= 1
        print("└──┴──┴──┴──┴──┴──┴──┘")
        print("█▓▒▒░░░PUNTAJE░░░▒▒▓█")
        print(self.p1 + ": " + str(self.score1))
        print(self.p2 + ": " + str(self.score2))

    def loop(self):
        while self.ganador == 0:
            self.mostrar_logo()
            self.mostrar_tablero()
            columna = self.solicitar_columna()
            self.colocar_ficha(columna)
            os.system('clear')
            self.turno = not self.turno
            self.ganador = self.verificar_ganador()

    def jugar(self):
        if self.ronda == 0:
            self.nombre_jugadores()
        self.ronda += 1
        self.loop()
        self.mostrar_game_over()
        self.mostrar_tablero()
        if self.ganador == 1:
            self.score1 += 1
            print("¡La victoria es para " + self.p1 + "!")
        elif self.ganador == 2:
            self.score2 += 1
            print("¡La victoria es para " + self.p2 + "!")
        elif self.ganador == 3:
            print(self.p1 + " y " + self.p2 + " han empatado... ¡Qué improbable!")
        self.reset()

    def reset(self):
        eleccion = input("¿Desea jugar de nuevo? (s/n): ")
        if eleccion.lower() == "s":
            self.ganador = 0
            for i in range(6):
                for j in range(7):
                    self.tablero[i][j] = 0
            self.jugar()
        else:
            print("¡Hasta la próxima!")
            exit()
