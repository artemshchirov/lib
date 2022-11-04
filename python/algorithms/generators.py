def printList2D(lst):
  '''
  Принимает двумерный список и красиво его выводит
  '''
  for i in range(len(lst)):
      for j in range(len(lst[i])):
          print(f'{lst[i][j]}',  end=" ")
      print()

a = []
# Заполнение списка в рамках range(x, y)
for i in range(51):
    a.append(i)
print('generator cycle:', a)

# ГЕНЕРАТОР - ЭТО: Список = [ЭЛЕМЕНТ for i in range(КОЛИЧЕСТВО)]
# Генератор списка с элементами:
b = [i for i in range(51)]
print('generator:', b)
# Генератор с нулями:
c = [0 for i in range(51)]
print('generator:', c)

# Генератор ДВУМЕРНОГО списка с элементами:
d = [[0 for i in range(5)] for j in range(5)]
print('generator 2D:', d)
# Заполнение 1й строки состоящей из 3 элементов нулями, 2й единицами и т.д.
e = [[j for i in range(5)] for j in range(5)]
print('generator 2D:', e)

# Генератор таблицы умножения:
f = [[(i * j) for i in range(1, 10)] for j in range(1, 10)]
printList2D(f)
