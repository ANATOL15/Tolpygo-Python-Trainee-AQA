
m = int(input('Введите начальное число диапазона: '))
n = int(input('Введите конечное число диапазона: ')) + 1
for i in range(m,n):

    if i%3==0:
        print(i, "кратно 3")
    else:
        print (i, "не кратно 3")

