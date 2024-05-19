#1
#x=int(input('введите число'))
#if (x>0):
#    s = 0
#    p = 1
#    while (x > 0):
#        n = x % 10
#        s += n
#        p *= n
#        x = x // 10
#        print("Сумма цифр = ", s)
#        print("Произведение цифр", p)
#else:
#    print("введены неправильные данные")
#2
#x=int(input('введите число'))
#if (x>0):
#    h = 0
#    j = 0
#    while (x>0):
#        n = x % 10
#        
#        if n%2 == 0:
#            h = h + 1
#        else:
#            j+=1
#        x = x // 10
#    print('кол во четных', h)
#    print("кол во не четных", j)
#3
#x=int(input('введите число'))
#if (x > 0):
#    p = 1
#    while (x > 0):
#        p =  p * x
#        x = x - 1
#    print('факториал равен', p)
#else:
#    print('введены неправильные данные')
#4
x=int(input('введите число'))
if (x>0):
    a = 0
    p = 1
    while (x > 0):
        p = x % 10
        a = a * 10
        a =a + p
        x =x // 10
    print(a)
