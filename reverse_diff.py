def revcalc(result):
    a = int(chislo)
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
    result = abs(reversd - int(chislo))
    return result

while True:
    try:
        print ("This program reverse your number and count the difference between your number and reversed one.")
        chislo = (input("Type a number: "))
        if (chislo.isdigit() == True and chislo[0]!="0"):
            print ("Result:", revcalc(chislo))
            break
        else:
            print("It looks like you made a mistake, you must write the number! ¯\_(ツ)_/¯")
    except:
        print("Error!")
