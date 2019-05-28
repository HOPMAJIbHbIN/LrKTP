print ("Задание 1")
import random
my_number=random.randint(0,10)
user_number=int(input("Введите число: "))
if user_number==my_number:
    print("Введено число равное заданному.")
    print("Заданное число:",my_number)
else:
    while True:
        user_number=int(input("Ваше число не равно заданному, введите снова: "))
        if(user_number==my_number):
            print("Введено число равно заданному.")
            print("Заданное число:",my_number)
            break

print ("Задание 2")
l = ['2312132amvr','qwert','21d32rf3r24g34','1548964865668887','123','688','0']
print("Строки размером до 10 символов")
for item in l:
    if((len(item)<=10)):
        print(item)

print ("Задание 3")
import string

N=int(input("Введите число: "))
r="R"
print (r*N)

print ("Задание 4")
import re
s = input('Введите строку:')
s = re.sub(r"\d+", "", s, flags=re.UNICODE)
print (s)

input('Press Enter to exit')