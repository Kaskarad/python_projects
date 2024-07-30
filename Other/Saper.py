def saper (size):

    # задаем размер поля
    n = int(size[0])
    m = int(size[1])


    # формируем поле. Звездочки заменяем на единицы
    a = [[''for i in range(m)] for j in range(n)]

    for i in range(n):
        b = str(input())
        for j in range(m):
            if b[j] == '*':
                a[i][j] = 1
            else:
                a[i][j] = 0

    #формируем верхнюю и нижнюю рамку
    
    upper_frame = [0 for i in range(m + 2)]
    lower_frame = [0 for i in range(m + 2)]
    new_frame_temp = []

    #формируем новую матрицу с рамкой
    for i in range (n):
        new_frame = new_frame_temp + [[0] + a[i] + [0]]
        new_frame_temp = new_frame

    final_frame = [upper_frame] + new_frame + [lower_frame]

    # возвращаем звездочки в основную матрицу
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i][j] = '*'

    # создаем матрицу с указанием количества звездочек вокруг ячейки
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if final_frame[i][j] != 1:
                a[i-1][j-1] = (final_frame[i - 1][j - 1] + final_frame[i - 1][j] + final_frame[i - 1][j + 1] +
                               final_frame[i][j - 1] + final_frame[i][j + 1] + final_frame[i + 1][j - 1] +
                               final_frame[i + 1][j] + final_frame[i + 1][j + 1])
    for i in a:
        print(*i, sep='')

saper (input().split())