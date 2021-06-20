from random import randint


def printList2D(lst):
    """
    Принимает двумерный список и красиво его выводит
    """
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(f'{lst[i][j]}', end=" ")
        print()


n = 10  # Кол- во работников
m = 12  # Кол- во месяцев
mylist = []
all = 0  # Сумма всех зарплат за 12 мес
ave = 0  # Среднее на работника за 12 мес по предприятию
aveOne = 0  # Среднее зарплат одного работника за 12 мес

for i in range(n):
    mylist.append([])
    for j in range(m):
        mylist[i].append(randint(10, 99))
        all += mylist[i][j]

ave = all // n

count = 0
for i in range(n):
    aveOne = 0
    for j in range(m):
        aveOne += mylist[i][j]
    if aveOne > ave:
        count += 1
        print(aveOne, ave)

max = mylist[0][0]
min = mylist[0][0]

for i in range(n):
    for j in range(m):
        if mylist[i][j] > max:
            max = mylist[i][j]
        if mylist[i][j] < min:
            min = mylist[i][j]

printList2D(mylist)
print('max:', max)
print('min:', min)
print('all:', all)
print('average:', ave)
print('count', count)
