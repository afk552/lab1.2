chislo = int(input())
a = chislo
mas = []
strr = ''
while a > 0:
    mas.append(a%10)
    a = a // 10
print (mas)


for i in range (len(mas)):
    strr = strr + str(mas[i])

reversd = int(strr)
result = abs(reversd - chislo)

print (result)