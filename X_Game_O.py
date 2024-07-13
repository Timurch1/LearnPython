from random import randint


class Game:
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    not_enter_matrix = []

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

    def isintanse(self):
        return isinstance(self.first_player, HandPlayer) or isinstance(self.second_player, HandPlayer)


    def start_game(self, player_winner1=False, player_winner2=False):
        if self.isintanse():
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
                if self.isintanse():
                    print(f'Недостуные поля для хода: {self.not_enter_matrix}')
                self.print_info()
                print()

            else:
                print("Ход - О")
                self.second_player.turn(self.matrix, -1)
                player_winner2 = self.chek_is_winner(-1)
                random_move_player += 1
                if self.isintanse():
                   print(f'Недостуные поля для хода: {self.not_enter_matrix}')
                self.print_info()
                print()

        if player_winner1:
            return f'Победил крестик!'
        elif player_winner2:
            return f'Победил нолик!'
        else:
            return f'Ничья!'


class Player:

    def turn(self, matrix, value):
        raise NameError('Походу неправильно указали имя в дочернем классе, советую перепроверить.')


class HandPlayer(Player):
    def turn(self, matrix, value):
        value_insert = int(input("Введите позицию вставки:"))
        if value_insert < 10:
            Game.not_enter_matrix.append(value_insert)
        else:
            print("Такого поля нету...")
            self.turn(matrix, value)
        obj_matrix = matrix[0]
        obj_matrix2 = matrix[1]
        obj_matrix3 = matrix[2]

        if value_insert == 1:
            obj_matrix[0] = value
        if value_insert == 2:
            obj_matrix[1] = value
        if value_insert == 3:
            obj_matrix[2] = value
        if value_insert == 4:
            obj_matrix2[0] = value
        if value_insert == 5:
            obj_matrix2[1] = value
        if value_insert == 6:
            obj_matrix2[2] = value
        if value_insert == 7:
            obj_matrix3[0] = value
        if value_insert == 8:
            obj_matrix3[1] = value
        if value_insert == 9:
            obj_matrix3[2] = value



class AutoPlayer(Player):


    def turn(self, matrix, value):

        obj_matrix = matrix[0]
        obj_matrix2 = matrix[1]
        obj_matrix3 = matrix[2]

        if obj_matrix[0] == value and obj_matrix[1] == value:
            obj_matrix[2] = value
            return True
        elif obj_matrix[2] == value and obj_matrix[1] == value:
            obj_matrix[0] = value
            return True
        elif obj_matrix2[0] == value and obj_matrix2[1] == value:
            obj_matrix2[2] = value
            return True
        elif obj_matrix2[2] == value and obj_matrix2[1] == value:
            obj_matrix2[0] = value
            return True
        elif obj_matrix3[0] == value and obj_matrix3[1] == value:
            obj_matrix3[2] = value
            return True
        elif obj_matrix3[2] == value and obj_matrix3[1] == value:
            obj_matrix3[0] = value
            return True

        elif obj_matrix[0] == value and obj_matrix2[0] == value:
            obj_matrix3[0] = value
            return True
        elif obj_matrix3[0] == value and obj_matrix2[0] == value:
            obj_matrix[0] = value
            return True
        elif obj_matrix[1] == value and obj_matrix2[1] == value:
            obj_matrix3[1] = value
            return True
        elif obj_matrix3[1] == value and obj_matrix2[1] == value:
            obj_matrix[1] = value
            return True
        elif obj_matrix[2] == value and obj_matrix2[2] == value:
            obj_matrix3[2] = value
            return True
        elif obj_matrix3[2] == value and obj_matrix2[2] == value:
            obj_matrix[2] = value
            return True

        elif obj_matrix[0] == value and obj_matrix2[1] == value:
            obj_matrix3[2] = value
            return True
        elif obj_matrix3[2] == value and obj_matrix2[1] == value:
            obj_matrix[0] = value
            return True
        elif obj_matrix[2] == value and obj_matrix2[1] == value:
            obj_matrix3[0] = value
            return True
        elif obj_matrix3[0] == value and obj_matrix2[1] == value:
            obj_matrix[2] = value
            return True
        else:
            if obj_matrix2[1] != -1:
                obj_matrix2[1] = value
                return True
            if obj_matrix3[0] != -1:
                obj_matrix3[0] = value
                return True
            if obj_matrix[0] != -1:
                obj_matrix[0] = value
                return True
            if obj_matrix2[0] != -1:
                obj_matrix2[0] = value
                return True
            if obj_matrix[1] != -1:
                obj_matrix[1] = value
                return True
            if obj_matrix[2] != -1:
                obj_matrix[2] = value
                return True
            if obj_matrix2[2] != -1:
                obj_matrix2[2] = value
                return True
            if obj_matrix3[1] != -1:
                obj_matrix3[1] = value
                return True
            if obj_matrix3[2] != -1:
                obj_matrix3[2] = value
                return True
            if obj_matrix2[2] != -1:
                obj_matrix2[2] = value
                return True


game = Game(HandPlayer(), AutoPlayer())
print(game.start_game())
