from api import api
from sudoku import Sudoku
import os


class Interfaz ():

    size = 9

    def ask_for_size(self):


        while self.size != "4" and self.size != "9":

            self.size = input("Por favor ingrese el tamaño del tablero que le gustaria jugar, 4 o 9:\n ")
            
            if self.size != "4" and self.size != "9":
                print("Solo puede ingresar 4 o 9 \n\n")

        os.system('clear')


    def inicio(self):

        self.ask_for_size()
        self.size = int(self.size)
        self.matri = api(self.size)
        self.game = Sudoku(self.matri)


    def enter(self, entered_value, f, c):

        try:

            if int(f) > self.size or int(f) < 1:
                return False

            elif int(c) > self.size or int(c) < 1:
                return False

            elif entered_value != "x":
                if int(entered_value) > 0 and int(entered_value) < self.size+1:
                    return True

            else:
                return True

        except Exception:
            return False

    def ask_values(self):

        self.v = input("Ingrese el valor deseado ")
        self.f = input("Ingrese fila deseada ")
        self.c = input("Ingrese columna deseada ")

        if self.enter(self.v, self.f, self.c):
            return self.game.insert_number(self.v, int(self.f)-1, int(self.c)-1, 1)

        else:
            return "\nNo puede hacer eso, ingrese valores validos"


    def play(self):

        self.inicio()
        self.game.draw_board(1)

        while not self.game.winner():
            self.ask_values()

        print("\nWINNER WINNER, CHICKEN DINNER")


if __name__ == "__main__":
    game = Interfaz()
    game.play()