
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = str(input('Введите вещественное число '))
my_list = []
fig = "0123456789"
sum1 = 0
for i in num:
    if i in fig:
        my_list.append(int(i))
        
for i in range(num):
    sum1 = sum1+my_list
print('Сумма элементов: ' + sum1) 

#print(sum(my_list))