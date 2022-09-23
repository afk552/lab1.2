while True:
    try:
        chislo = (input("Type a number: "))
        if (chislo.isdigit() == True and chislo[0]!="0"):
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
        print ("Result:", result)
        break
    except:
        print("It looks like you made a mistake, you must write the number! ¯\_(ツ)_/¯")
