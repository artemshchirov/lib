def clearCode(com):
    p = 0
    clearCom = ''
    while (p < len(com)):
        if (ord(com[p]) in listCode):
            clearCom += com[p]
        p += 1
    return clearCom

listCode = []
for i in 'WASDE123':
    listCode.append(ord(i))

com3 = 'UHWQRWGWFEG'.upper()
com2 = 'WSSWAASWAEA'.upper()
com1 = 'WWWWGFGKLKHOIKEO.......WE'.upper()
clearCom1 = clearCode(com1)
clearCom2 = clearCode(com2)
clearCom3 = clearCode(com3)
outCom = ''

p1 = 0
p2 = 0
p3 = 0

while (p1 < len(clearCom1)):
    res = False
    if (clearCom1[p1] == clearCom2[p2]):
        while (not res):
            if (clearCom2[p2] == clearCom3[p3]):
                outCom += clearCom3[p3]
                res = True
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                p3 += 1
            if (p3 >= len(clearCom3)):
                res = True
                p1 += 1
                p3 = 0
    else:
        p2 += 1
    if (p2 >= len(clearCom2)):
        p1 += 1
        p2 = 0




print(clearCom1)
print(clearCom2)
print(clearCom3)
print()
print(outCom)
