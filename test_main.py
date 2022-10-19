import unittest
from game import Game
from unittest.mock import patch

game = Game()

class TestGame(unittest.TestCase):
    def test_entero_valido(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(game.entero_valido(''), 1)
    
    def test_solicitar_columna(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(game.solicitar_columna(), 1)
    
    def test_colocar_ficha(self):
        game.colocar_ficha(1)
        game.colocar_ficha(2)
        game.colocar_ficha(1)
        self.assertEqual(game.tablero[0][0], 1)
        self.assertEqual(game.tablero[0][1], 1)
        self.assertEqual(game.tablero[1][0], 1)
        
    # Verificar que ha ganado el jugador 1
    def test_win_h_p1(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [0, 0, 0, 0, 0, 0, 0]
        fila_3 = [0, 0, 0, 0, 0, 0, 0]
        fila_2 = [0, 0, 0, 0, 0, 0, 0]
        fila_1 = [1, 1, 1, 1, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 1)
    
    def test_win_v_p1(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [1, 0, 0, 0, 0, 0, 0]
        fila_3 = [1, 0, 0, 0, 0, 0, 0]
        fila_2 = [1, 0, 0, 0, 0, 0, 0]
        fila_1 = [1, 0, 0, 0, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 1)
    
    def test_win_d_p1(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [0, 0, 0, 1, 0, 0, 0]
        fila_3 = [0, 0, 1, 0, 0, 0, 0]
        fila_2 = [0, 1, 0, 0, 0, 0, 0]
        fila_1 = [1, 0, 0, 0, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 1)

    # Verificar que ha ganado el jugador 2
    def test_win_h_p2(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [0, 0, 0, 0, 0, 0, 0]
        fila_3 = [0, 0, 0, 0, 0, 0, 0]
        fila_2 = [0, 0, 0, 0, 0, 0, 0]
        fila_1 = [2, 2, 2, 2, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 2)
    
    def test_win_v_p2(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [2, 0, 0, 0, 0, 0, 0]
        fila_3 = [2, 0, 0, 0, 0, 0, 0]
        fila_2 = [2, 0, 0, 0, 0, 0, 0]
        fila_1 = [2, 0, 0, 0, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 2)
    
    def test_win_d_p2(self):
        fila_6 = [0, 0, 0, 0, 0, 0, 0]
        fila_5 = [0, 0, 0, 0, 0, 0, 0]
        fila_4 = [0, 0, 0, 2, 0, 0, 0]
        fila_3 = [0, 0, 2, 0, 0, 0, 0]
        fila_2 = [0, 2, 0, 0, 0, 0, 0]
        fila_1 = [2, 0, 0, 0, 0, 0, 0]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 2)
    
    # Verificar empate
    def test_empate(self):
        fila_6 = [2, 1, 2, 1, 2, 1, 2]
        fila_5 = [2, 1, 2, 1, 2, 1, 2]
        fila_4 = [2, 1, 2, 1, 2, 1, 2]
        fila_3 = [1, 2, 1, 2, 1, 2, 1]
        fila_2 = [1, 2, 1, 2, 1, 2, 1]
        fila_1 = [1, 2, 1, 2, 1, 2, 1]
        game.tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

        self.assertEqual(game.verificar_ganador(), 3)

if __name__ == '__main__':
    unittest.main()