#Вводим возраст
a = float(input('Введите человеческий возраст: '))
if a > 0: #проверка на положительное число
    if a - 10.5 > 0: #проверка на первый особый год
        sa = 1
        a = a - 10.5
        if a - 10.5 > 0: #проверка на второй особый год
            sa = 2
            a = a - 10.5
            while a >= 4: #все остальные года
                sa += 1
                a = a - 4
            sa = sa + a/10.5 #расчеты
            print(sa, 'собачих лет') #вывод
        else:
            print(1 + (a / 10.5), 'собачих лет')
    else:
        print(a / 10.5, 'собачих лет')
else:
    print('')
