import players.base_player


class HandPlayer(players.base_player.Player):
    not_enter_matrix = []

    def turn(self, matrix, value):
        value_insert = int(input("Введите позицию вставки:"))
        if value_insert < 10:
            self.not_enter_matrix.append(value_insert)
            print(f'Недостуные поля для хода: {self.not_enter_matrix}')
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
