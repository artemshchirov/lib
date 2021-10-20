list = [4, 8, 9, 1, 2, 3, 7, 10, 6, 5]
print(list)

def bubbleSort(list):
	'''
	Пузырьковая сортировка
	'''
	for i in range(len(list) - 1):
		print(f'i: {i} {list}')
		for j in range(len(list) -1 - i):
			if (list[j] < list[j + 1]):
				list[j], list[j + 1] = list[j + 1], list[j]
			print(f'j: {j} [{list}]')
	print(f'Sorted: {list}')

# ======================================



# ======================================

# bubbleSort(list)
print(list)
