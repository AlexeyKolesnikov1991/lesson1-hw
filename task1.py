#Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

#1) до минуты: <s> сек;
#2) до часа: <m> мин <s> сек;
#3) до суток: <h> час <m> мин <s> сек;
#4) сутки или больше: <d> дн <h> час <m> мин <s> сек

#Например, если пользователь введет 4567 секунд, вывести:
#1 час 16 мин 7 сек

time = int(input('Введите значение промежутка времени в секундах:'))

minutes = time // 60
hours = minutes // 60
days = hours // 24

seconds = time % 60
minutes %= 60
hours %= 24

if time < 60:
    print(f"{seconds} сек")

elif time < 60*60:
    print(f"{minutes} мин {seconds} сек")

elif time < 24*60*60:
    print(f"{hours} часы {minutes} мин {seconds} сек")

elif time >24*60*60:
    print(f"{days} дни {hours} час {minutes} мин {seconds} сек")
