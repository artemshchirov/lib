# РЕКУРСИВНЫЙ QUICKSORT

def qsort(a):

	if (len(a) == 2):
		if (a[0] > a[1]):
			a[0], a[1] = a[1], a[0]
		return a
	# Если длина списка больше 2
	elif (len(a) > 2):
	# В качестве average берем среднее значение из списка, т.к без высчитыванние я - быстрее
		average = sum(a) // len(a)

		# То начинаем: считаем среднее арифметическое списка
		# average = sum(a) // len(a)    # Этот способ, в отличии от предыдущего экономит память
		sp1 = []    # Элементы меньше average
		sp2 = []    # Элементы равные average
		sp3 = []    # Элементы большие average

		for i in a:
			if (i < average):
				sp1.append(i)
			elif (i == average):
				sp2.append(i)
			elif (i > average):
				sp3.append(i)

		# Возвращаем рекурентное соотношение, результат результата возвращается результатом
		return qsort(sp1) + sp2 + qsort(sp3)
	else:
		return a

a = [5, 8, 1, 5, 3, 5, 2, 0, 2, 5, 2]
print(a)
a = qsort(a)
print(a)
