def find (matrix,number):
    while len(matrix) > 0:
            if matrix[0][0] == number:
                return True
            elif matrix[0][-1] == number:
                return True
            else:
                matrix.remove(matrix[0])
    return False

if __name__ == '__main__':
    matrix = [[1,2],[3,4],[5,6]]
    number = 3
    print(find(matrix,number))