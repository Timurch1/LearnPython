import players.base_player


class AutoPlayer(players.base_player.Player):

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
