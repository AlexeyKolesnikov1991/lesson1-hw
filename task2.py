#ЗАДАНИЕ 2

#Сумма цифр числа
#Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
#Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".

number = str(input("Введите целое число:"))
sum = 0
lst_str = list(str_number)
lst_number = map(int, lst_str)
    while number != 0:
        sum = sum(map(int, lst_str))
    return(sum)
