sIn = 'HelloWorld'
sOut = ''
sIn2 = ''
count = 0
for letter in sIn:
    print('letter:', letter)
    print('ord(letter):', ord(letter))
    print('count', count)
    print('(count % 10 + 1) =', (count % 10) + 1)
    ch = ord(letter) + (count % 10) + 1
    print('ch:', ch, 'chr(ch):', chr(ch))
    sOut += chr(ch)
    sIn2 += letter
    print(sIn2)
    print(sOut)
    count += 1

sIn2 = sOut
sOut2 = ''
sInPrint = ''
count2 = 0

for l in sIn2:

  sOut2 += chr(ord(l) - (count2 % 10) -1)
  count2 += 1

print(sOut2)
