from players.base_player import Player


class IlyaPlayer(Player):

    def turn(self, matrix, value):
        # символ врага
        enemy_value = value * -1
        # символ свободной клетки
        free_value = 0

        # если центр свободен, всегда ставим туда
        if self.center_check(matrix, free_value):
            matrix[1][1] = value
            return

        # если у меня два в ряд, закрываем линию своим
        if self.check_all_critical_combinations(matrix, value, value):
            return

        # если у противника два в ряд, закрываем линию своим
        if self.check_all_critical_combinations(matrix, enemy_value, value):
            return

        # ищем для себя "первый угол"
        if matrix[0][0] != value and matrix[2][0] != value and matrix[0][2] != value and matrix[2][2] != value:
            if matrix[0][0] == free_value:
                matrix[0][0] = value
                return
            if matrix[2][0] == free_value:
                matrix[2][0] = value
                return
            if matrix[0][2] == free_value:
                matrix[0][2] = value
                return
            if matrix[2][2] == free_value:
                matrix[2][2] = value
                return

        # ищем свободный угол рядом c "моим" углом
        # ищем рядом с 0,0
        if self.left_top_check(matrix, value):
            if self.right_top_check(matrix, free_value):
                matrix[0][2] = value
                return
            if self.left_bottom_check(matrix, free_value):
                matrix[2][0] = value
                return

        # ищем рядом с 0,2
        if self.right_top_check(matrix, value):
            if self.left_top_check(matrix, free_value):
                matrix[0][0] = value
                return
            if self.right_bottom_check(matrix, free_value):
                matrix[2][2] = value
                return

        # ищем рядом с 2,0
        if self.left_bottom_check(matrix, value):
            if self.left_top_check(matrix, free_value):
                matrix[0][0] = value
                return
            if self.right_bottom_check(matrix, free_value):
                matrix[2][2] = value
                return

        # ищем рядом с 2,2
        if self.right_bottom_check(matrix, value):
            if self.right_top_check(matrix, free_value):
                matrix[0][2] = value
                return
            if self.left_bottom_check(matrix, free_value):
                matrix[2][0] = value
                return

        # уже насрать на победу просто ставим, в случайную свободную ячейку
        for i in range(0, 3):
            for j in range(0, 3):
                if matrix[i][j] == free_value:
                    matrix[i][j] = value
                    return

    def check_all_critical_combinations(self, matrix, check_value, set_value):
        # проверка 0, 0
        if self.check_0_0(matrix, check_value):
            if matrix[0][0] == 0:
                matrix[0][0] = set_value
                return True

        # проверка 0, 1
        if self.check_0_1(matrix, check_value):
            if matrix[0][1] == 0:
                matrix[0][1] = set_value
                return True

        # проверка 0, 2
        if self.check_0_2(matrix, check_value):
            if matrix[0][2] == 0:
                matrix[0][2] = set_value
                return True

        # проверка 1, 0
        if self.check_1_0(matrix, check_value):
            if matrix[1][0] == 0:
                matrix[1][0] = set_value
                return True

        # проверка 1, 2
        if self.check_1_2(matrix, check_value):
            if matrix[1][2] == 0:
                matrix[1][2] = set_value
                return True

        # проверка 2, 0
        if self.check_2_0(matrix, check_value):
            if matrix[2][0] == 0:
                matrix[2][0] = set_value
                return True

        # проверка 2, 1
        if self.check_2_1(matrix, check_value):
            if matrix[2][1] == 0:
                matrix[2][1] = set_value
                return True

        # проверка 2, 2
        if self.check_2_2(matrix, check_value):
            if matrix[2][2] == 0:
                matrix[2][2] = set_value
                return True

        return False

    def check_0_0(self, matrix, value):
        return ((self.top_check(matrix, value) and self.right_top_check(matrix, value)) or
                (self.center_check(matrix, value) and self.right_bottom_check(matrix, value)) or
                (self.left_center_check(matrix, value) and self.left_bottom_check(matrix, value)))

    def check_0_1(self, matrix, value):
        return ((self.left_top_check(matrix, value) and self.right_top_check(matrix, value)) or
                (self.center_check(matrix, value) and self.bottom_check(matrix, value)))

    def check_0_2(self, matrix, value):
        return ((self.left_top_check(matrix, value) and self.top_check(matrix, value)) or
                (self.left_bottom_check(matrix, value) and self.center_check(matrix, value)) or
                (self.right_center_check(matrix, value) and self.right_bottom_check(matrix, value)))

    def check_1_0(self, matrix, value):
        return ((self.left_top_check(matrix, value) and self.left_bottom_check(matrix, value)) or
                (self.center_check(matrix, value) and self.right_center_check(matrix, value)))

    def check_1_2(self, matrix, value):
        return ((self.right_top_check(matrix, value) and self.right_bottom_check(matrix, value)) or
                (self.left_center_check(matrix, value) and self.center_check(matrix, value)))

    def check_2_0(self, matrix, value):
        return ((self.left_top_check(matrix, value) and self.left_center_check(matrix, value)) or
                (self.center_check(matrix, value) and self.right_top_check(matrix, value)) or
                (self.bottom_check(matrix, value) and self.right_bottom_check(matrix, value)))

    def check_2_1(self, matrix, value):
        return ((self.top_check(matrix, value) and self.center_check(matrix, value)) or
                (self.left_bottom_check(matrix, value) and self.right_bottom_check(matrix, value)))

    def check_2_2(self, matrix, value):
        return ((self.right_top_check(matrix, value) and self.right_center_check(matrix, value)) or
                (self.left_bottom_check(matrix, value) and self.bottom_check(matrix, value)) or
                (self.left_top_check(matrix, value) and self.center_check(matrix, value)))

    @staticmethod
    def left_top_check(matrix, value):
        return matrix[0][0] == value

    @staticmethod
    def top_check(matrix, value):
        return matrix[0][1] == value

    @staticmethod
    def right_top_check(matrix, value):
        return matrix[0][2] == value

    @staticmethod
    def left_center_check(matrix, value):
        return matrix[1][0] == value

    @staticmethod
    def center_check(matrix, value):
        return matrix[1][1] == value

    @staticmethod
    def right_center_check(matrix, value):
        return matrix[1][2] == value

    @staticmethod
    def left_bottom_check(matrix, value):
        return matrix[2][0] == value

    @staticmethod
    def bottom_check(matrix, value):
        return matrix[2][1] == value

    @staticmethod
    def right_bottom_check(matrix, value):
        return matrix[2][2] == value
