import random

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print (f'{el:^3}', end='  ')
        print ()

try:    
    while True:
        number_of_columns = int(input("Введите количество столбцов матрицы (n): "))
        number_of_rows = int(input("Введите количество строк матрицы (m): "))

        if number_of_columns >= 0 and number_of_rows >= 0:
            break
        else:
            print ('Ошибка ввода!\n')

    matrix = [[random.randint(-15, 15) for i in range(number_of_columns)] for i in range(number_of_rows)]
    original_matrix = matrix[:]

    min_ = matrix[0][0]
    row_index_min_ = 0
    el_index_min_ = 0

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
                row_index_min_ = i
                el_index_min_ = j

    print ("\nИсходная матрица:\n")
    print_matrix(original_matrix)
    print ("\nМинимальный элемент:", min_)
    print ("\nИндексы минимального элемента:")
    print ("Столбец:", el_index_min_ + 1)
    print ("Строка:", row_index_min_ + 1)

    matrix.pop(row_index_min_)
    for row in matrix:
        row.pop(el_index_min_)

    print ("\nИтоговая матрица:\n")
    print_matrix(matrix)

except ValueError:
    print ("Ошибка ввода! ")