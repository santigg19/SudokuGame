import math
import os


class Sudoku():

    def __init__(self, matri):

        self.board = matri
        self.size = len(self.board)
        self.region = int(math.sqrt(self.size))
        self.validar_fila = True
        self.validar_columna = True
        self.validar_cuadrante = True
        self.validar_vacio = True
        self.cuadranteX = 0
        self.cuadranteY = 0
        self.listaCuadrante = []


    def draw_board(self, flag):
        if (flag == 1):
            for i in range(len(self.board)):
                if i % self.region == 0 and i != 0:
                    for _ in range (self.size + self.region):
                        print("- ", end = '')
                    print()

                for j in range(len(self.board[0])):
                    if j % self.region == 0 and j != 0:
                        print(" | ", end = "")
                    if j == self.size - 1:
                        print(self.board[i][j])
                    else:
                        print(str(self.board[i][j]) + " ", end = "")    
        
    def cuadrantes(self, x, y):
        if (x >= 0 and x < self.region):
            self.cuadranteX = 1
        elif (x >= self.region and x < self.region * 2):
            self.cuadranteX = 2
        elif (x >= self.region * 2 and x < self.region * 3):
            self.cuadranteX = 3

        if (y >= 0 and y < self.region):
            self.cuadranteY = 1
        elif (y >= self.region and y < self.region * 2):
            self.cuadranteY = 2
        elif (y >= self.region * 2 and y < self.region * 3):
            self.cuadranteY = 3

        self.listaCuadrante.clear()
        for fila in range ((self.cuadranteX-1) * self.region, self.cuadranteX * self.region):
            for columna in range ((self.cuadranteY-1) * self.region, self.cuadranteY * self.region):
                self.listaCuadrante.append(self.board[fila][columna])


    def validar(self, num, x, y):
        self.validar_columna = True
        for fila in range(self.size):
            if (num == self.board[fila][y]):
                self.validar_columna = False

        self.validar_fila = True
        for columna in range (self.size):
            if (num == self.board[x][columna]):
                self.validar_fila = False
            
        self.cuadrantes(x,y)
        self.validar_cuadrante = True
        for n_cuadrante in range (self.size):
            if (num == self.listaCuadrante[n_cuadrante]):
                self.validar_cuadrante = False

        self.validar_vacio = True
        if (self.board[x][y] != 'x'):
            self.validar_vacio = False


    def insert_number(self, num, x, y, flag):
        self.validar(num, x, y)

        if (self.validar_columna and self.validar_fila and self.validar_cuadrante and self.validar_vacio):
            self.board[x][y] = num
            os.system('clear')
            self.draw_board(flag)
        else:
            os.system('clear')
            self.draw_board(flag)
            # print('No podes ingresar', num, 'en la fila', x+1, 'columna', y+1)
            # os.system('clear')


    def winner(self):
        for i in range(self.size):

            if "x" in self.board[i]:
                return False
        return True