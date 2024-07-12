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
    # В принципе осталось только это, но есть проблемы с auto_player
    def print_info(self):
        pass

    def start_game(self, Player_Winner1=False, Player_Winner2=False):

        random_move_player = randint(0, 1)
        count = -1
        while True:
            count += 1
            if count == 9:
                break
            if Player_Winner1:
                break
            if Player_Winner2:
                break
            if random_move_player == 1:
                print("Ход - Х")
                self.first_player.turn(self.matrix, int(input("Введите позицию вставки:")))
                Player_Winner1 = self.chek_is_winner('X')
                random_move_player -= 1
                print(f'Недостуные поля для хода: {self.not_enter_matrix}')
                print(self.matrix)
                print()
            else:
                print("Ход - О")
                self.second_player.turn(self.matrix, int(input("Введите позицию вставки:")))
                Player_Winner2 = self.chek_is_winner('O')
                random_move_player += 1
                print(f'Недостуные поля для хода: {self.not_enter_matrix}')
                print(self.matrix)
                print()

        if Player_Winner1:
            return f'Победил крестик!'
        elif Player_Winner2:
            return f'Победил нолик!'
        else:
            return f'Ничья!'

class Player:

    def turn(self, matrix, value):
        raise NameError("Походу неправильно указали имя в дочернем классе, советую перепроверить.")

class TimurPlayer_Usual(Player):
    def turn(self, matrix, value):
        if value < 10:
            Game.not_enter_matrix.append(value)
        obj_matrix = matrix[0]
        obj_matrix2 = matrix[1]
        obj_matrix3 = matrix[2]

        if value == 1:
            obj_matrix[0] = 'X'
        if value == 2:
            obj_matrix[1] = 'X'
        if value == 3:
            obj_matrix[2] = 'X'
        if value == 4:
            obj_matrix2[0] = 'X'
        if value == 5:
            obj_matrix2[1] = 'X'
        if value == 6:
            obj_matrix2[2] = 'X'
        if value == 7:
            obj_matrix3[0] = 'X'
        if value == 8:
            obj_matrix3[1] = 'X'
        if value == 9:
            obj_matrix3[2] = 'X'

class IlyaPlayer_Usual(Player):
    def turn(self, matrix, value):
        if value < 10:
           Game.not_enter_matrix.append(value)
        obj_matrix = matrix[0]
        obj_matrix2 = matrix[1]
        obj_matrix3 = matrix[2]

        if value == 1:
            obj_matrix[0] = 'O'
        if value == 2:
            obj_matrix[1] = 'O'
        if value == 3:
            obj_matrix[2] = 'O'
        if value == 4:
            obj_matrix2[0] = 'O'
        if value == 5:
            obj_matrix2[1] = 'O'
        if value == 6:
            obj_matrix2[2] = 'O'
        if value == 7:
            obj_matrix3[0] = 'O'
        if value == 8:
            obj_matrix3[1] = 'O'
        if value == 9:
            obj_matrix3[2] = 'O'

class AutoPlayer1(Player):
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
           obj_matrix3[0] == value
           return True
       elif obj_matrix3[0] == value and obj_matrix2[0] == value:
           obj_matrix[0] == value
           return True
       elif obj_matrix[1] == value and obj_matrix2[1] == value:
           obj_matrix3[1] == value
           return True
       elif obj_matrix3[1] == value and obj_matrix2[1] == value:
           obj_matrix[1] == value
           return True
       elif obj_matrix[2] == value and obj_matrix2[2] == value:
           obj_matrix3[2] == value
           return True
       elif obj_matrix3[2] == value and obj_matrix2[2] == value:
           obj_matrix[2] == value
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
               return Tru
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
game = Game(TimurPlayer_Usual(), IlyaPlayer_Usual())
print(game.start_game())