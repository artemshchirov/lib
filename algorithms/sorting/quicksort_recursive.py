# TODO: Понять как писать его в reverse (не с min до max чисел, а с max до min чисел)
# Upd: Это происходит т.к в recursiveQsort(small) не правильно становятся числа ([4, 5] вместо [5, 4], например)
# Как это исправить?
# Upd: Готово! В "if (list[0] -> > <- (Исправить на -> < <-) list[1]):"

listStart = [4, 8, 9, 1, 2, 3, 7, 10, 6, 5]
print(f'Start : {listStart}')
countRec = 0

def recursiveQsort(list):
	global countRec
	countRec += 1

	if (len(list) == 2):
		if (list[0] > list[1]):
			list[0], list[1] = list[1], list[0]
		return list

	elif (len(list) > 2):
		average = list[len(list) // 2]

		small = []
		large = []
		equal = []

		print(f'\nlist: {list}')

		countFor = 0
		for i in list:
			countFor += 1

			print(f'i: {i}, average: {average}, countFor: {countFor}, countRec: {countRec}')

			if (i < average):
				small.append(i)
			elif (i > average):
				large.append(i)
			else:
				equal.append(i)

			print(f'small: {small}')
			print(f'large: {large}')
			print(f'equal: {equal}')
			print(f'list : {small + equal + large}\n')

		return recursiveQsort(small) + equal + recursiveQsort(large)
	else:
		return list

def qsort(list):
	'''
	Рекурсивная сортировка.
	Тренировочное поле:
	'''

	# ======================================



	# ======================================

listSorted = qsort(listStart)

# listSorted = recursiveQsort(listStart)
print(f'Sorted: {listSorted}')
