chislo = int(input("Type a number: "))
a = chislo
mas = []
strr = ''
while a > 0:
    mas.append(a%10)
    a = a // 10
print ("Reversed typed number: ", end = '')
for i in range (len(mas)):
    print (mas[i], end = '')

for i in range (len(mas)):
    strr = strr + str(mas[i])
print ("\n")

reversd = int(strr)
result = abs(reversd - chislo)
print ("Result:", result)
