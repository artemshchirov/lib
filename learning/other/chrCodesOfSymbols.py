ch = "A"
# Найти код символа операционной системы
# print(ord(ch))

# Определить символ по десятчиному коду системы
code = 65 
# print(chr(code))
code = ord("A")
# print(chr(code))

# Таблица кода символов русского алфавита
start = ord("А")
end = ord("я")
for i in range(start, end+1):
    print(f'{chr(i)} = {i}  ', end='')
    if ((i+1) % 13 == 0):
        print()
