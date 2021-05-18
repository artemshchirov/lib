list = [4, 8, 9, 1, 2, 3, 7, 10, 6, 5]
print(list)

def insertSort(list):
	'''
	Сортировка вставками
	'''
	count = 0
	for i in range(1, len(list)):
		n = list[i]                         # Запоминание "текущего элемента"
		j = i - 1                           # Индекс для вставки
		print(f'n: {n}, j: {j} {list}')
		while (j >= 0 and list[j] < n):
			list[j + 1] = list[j]           # Сдвиг для освобождения места для n
			j -= 1                          # Уменьшение индекса j
			count += 1						# Счетчик итераций
			print(f'n: {n}, j: {j} {list}')
		list[j + 1] = n                     # Установка n в найденное место
		print(f'n: {n}, j: {j} {list}')
	print(f'Sorted: {list}, count: {count}')

# ======================================



# ======================================

# insertSort(list)
print(list)
