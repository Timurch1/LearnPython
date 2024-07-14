from random import randint
import players


class Game:
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def chek_is_winner(self, value):
        not_matrix = self.matrix[0]
        not_matrix2 = self.matrix[1]
        not_matrix3 = self.matrix[2]

        if not_matrix[0] == value and not_matrix[1] == value and not_matrix[2] == value:
            return True
        if not_matrix2[0] == value and not_matrix2[1] == value and not_matrix2[2] == value:
            return True
        if not_matrix3[0] == value and not_matrix3[1] == value and not_matrix3[2] == value:
            return True
        if not_matrix[0] == value and not_matrix2[0] == value and not_matrix3[0] == value:
            return True
        if not_matrix[1] == value and not_matrix2[1] == value and not_matrix3[1] == value:
            return True
        if not_matrix[2] == value and not_matrix2[2] == value and not_matrix3[2] == value:
            return True
        if not_matrix[0] == value and not_matrix2[1] == value and not_matrix3[2] == value:
            return True
        if not_matrix[2] == value and not_matrix2[1] == value and not_matrix3[0] == value:
            return True
        return False

    def print_info(self):
        for i in range(0, 3):
            row = self.matrix[i]
            print("{0} | {1} | {2} |".format(self.convert_symbol(row[0]), self.convert_symbol(row[1]), self.convert_symbol(row[2])))

    def convert_symbol(self, value):
        if value == 1:
            return "X"
        elif value == -1:
            return "O"
        else:
            return "-"

    def start_game(self, player_winner1=False, player_winner2=False):
        print("Каждое поле в Крестики-Нолики соотвествует цифре:"'\n'
              "                [1]  [2]  [3]"'\n'
              "                [4]  [5]  [6]"'\n'
              "                [7]  [8]  [9]")
        random_move_player = randint(0, 1)
        count = -1
        while True:
            count += 1
            if count == 9:
                break
            if player_winner1:
                break
            if player_winner2:
                break

            if random_move_player == 1:
                print("Ход - Х")
                self.first_player.turn(self.matrix, 1)
                player_winner1 = self.chek_is_winner(1)
                random_move_player -= 1
                self.print_info()
                print()

            else:
                print("Ход - О")
                self.second_player.turn(self.matrix, -1)
                player_winner2 = self.chek_is_winner(-1)
                random_move_player += 1
                self.print_info()
                print()

        if player_winner1:
            return f'Победил крестик!'
        elif player_winner2:
            return f'Победил нолик!'
        else:
            return f'Ничья!'


game = Game(players.HandPlayer(), players.HandPlayer())
print(game.start_game())
