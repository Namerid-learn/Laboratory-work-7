import random

def print_matrix(matrix):
        for row in matrix:
            for el in row:
                print (f'{el:^3}', end='  ')
            print ()

def print_list(lst):
    for el in lst:
        print (f'{el:^3}', end='  ')

def func(lst):
    s = 0
    for i in range(1, len(lst), 2):
        el = lst[i]
        if el > 0:
            s += el
    return s

try:    
    while True:
        number_of_columns = int(input("Введите количество столбцов матрицы: "))
        number_of_rows = int(input("Введите количество строк матрицы: "))

        if number_of_columns >= 0 and number_of_rows >= 0:
            break
        else:
            print ('Ошибка ввода!\n')

    matrix = [[random.randint(-15, 15) for i in range(number_of_columns)] for i in range(number_of_rows)]
    original_matrix = matrix[:]

    for ii in range(len(matrix) - 1):
        for i in range(len(matrix) - 1):
            if func(matrix[i]) > func(matrix[i + 1]):
                value = matrix[i]
                matrix[i] = matrix[i + 1]
                matrix[i + 1] = value

    lst = []
    for row in matrix:
        lst.append(func(row))

    print ("\nИсходная матрица:\n")
    print_matrix(original_matrix)
    print ("\nИтоговая матрица:\n")
    print_matrix(matrix)
    print ("\nХарактеристики итоговой матрицы:\n")
    for el in lst:
        print (el, end = ' ')

except ValueError:
    print ("Ошибка ввода! ")

