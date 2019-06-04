class method():
    def printMatrix(self, matrix):
        # 打印矩阵
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix:
                matrix = self.rotate(matrix)
        return result

    def rotate(self, matrix):
        # 逆时针旋转矩阵
        row = len(matrix)
        col = len(matrix[0])
        # 存放旋转后的矩阵
        new_matrix = []
        # 行列调换
        for i in range(col):
            new_line = []
            for j in range(row):
                new_line.append(matrix[j][col-1-i])
            new_matrix.append(new_line)
        return new_matrix
