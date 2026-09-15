# транспонирование матрицы
def transpose(mat: list[list[float | int]]) -> list[list]:
    """Транспонирует прямоугольную матрицу."""

    if len(mat)==0:
        return []


    if all(len(row)==len(mat[0]) for row in mat):
        stolb = len(mat[0]) #2
        row = len(mat) #3
        nmat=[]
        for i in range(stolb):
            nrow = []
            for y in range(row):
                nrow.append(mat[y][i])
            nmat.append(nrow)
        return nmat



    else: 
        raise ValueError("Матрица рваная")  

# print(transpose([[1, 2, 3]]))          # [[1], [2], [3]]
# print(transpose([[1], [2], [3]]))      # [[1, 2, 3]]
# print(transpose([[1, 2], [3, 4]]))     # [[1, 3], [2, 4]]
# print(transpose([]))                    # []
# print(transpose([[1, 2], [3]]))        # ValueError

#----------------------------------------------------------------------------------
#cумма строк
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы элементов каждой строки матрицы."""
    if len(mat)==0: raise ValueError("Пустой список")
    if  not all(len(row)==len(mat[0]) for row in mat): raise ValueError("Матрица рваная")
    else:
        return [sum(row) for row in mat]

# print(row_sums([[1, 2, 3], [4, 5, 6]]))     # [6, 15]
# print(row_sums([[-1, 1], [10, -10]]))        # [0, 0]
# print(row_sums([[0, 0], [0, 0]]))            # [0, 0]
# print(row_sums([[1, 2], [3]]))                # ValueError


#----------------------------------------------------------------------------------
#сумма столбцов
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы элементов каждого столбца матрицы."""
    if len(mat)==0: raise ValueError("Пустой список")
    if  not all(len(row)==len(mat[0]) for row in mat): raise ValueError("Матрица рваная")
    else:
        return [sum(stolb) for stolb in transpose(mat)] #юзаем функцию транспонирования

print(col_sums([[1, 2, 3], [4, 5, 6]]))     # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))        # [9, -9]
print(col_sums([[0, 0], [0, 0]]))            # [0, 0]
print(col_sums([[1, 2], [3]]))                # ValueError
