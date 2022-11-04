from random import randint

def crypt(s, key):

    lenKey = len(key)
    start = 0          # Позиция в строке, которую шифруют. Изначально = 0
    posInKey = 0       # Позиция в списке ключе. Изначально = 0

    if (len(s) % lenKey != 0):
        while (len(s) % lenKey != 0):
            s += chr(randint(ord('!'), ord('=')))

    lenS = len(s)
    sEncrypt = ''

    while (start + lenKey < lenS + 1):
        sEncrypt += s[start + key[posInKey] - 1]
        posInKey += 1
        if (posInKey >= lenKey):
            posInKey = 0
            start += lenKey

    return sEncrypt

encryptKey = [3, 6, 4, 2, 1, 5]
decryptKey = [5, 4, 1, 3, 6, 2]

stringCrypt = crypt('На мели мы налимов ленило ловили, это зашифровано', encryptKey)
print('Зашифровано:', stringCrypt)

stringCrypt = crypt(stringCrypt, decryptKey)
print('Расшифровано:', stringCrypt)
