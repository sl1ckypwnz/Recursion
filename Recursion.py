﻿def f(arr):
    if not arr:
        print('Конец списка')
    else:
        print(arr[0])
        f(arr[1:])
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
f(my_list)