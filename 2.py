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

    min = matrix[0][0]
    row_index_min = 0
    el_index_min = 0
    row_index = 0
    el_index = 0

    while row_index != number_of_rows - 1:
        el_index = 0
        while el_index != number_of_columns - 1:
            if matrix[row_index][el_index] < min:
                min = matrix[row_index][el_index]
                row_index_min = row_index
                el_index_min = el_index
            el_index += 1

        row_index += 1

    matrix.pop(row_index_min)

    print ("\nИсходная матрица:\n")
    print_matrix(original_matrix)

    row_index = 0
    el_index = 0

    while row_index != number_of_rows - 1:
        el_index = 0
        while el_index != number_of_columns - 1:
            if el_index == el_index_min:
                matrix[row_index].pop(el_index)
            el_index += 1

        row_index += 1

    print ("\nИтоговая матрица:\n")
    print_matrix(matrix)

except ValueError:
    print ("Ошибка ввода! ")