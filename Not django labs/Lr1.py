print ("Задание 1")
a=int(input("Введите а: "))
b=int(input("Введите b: "))
c = int(input("Введите c: "))
k = int(input("Введите k: "))
d = int(input("Введите d: "))
z=float()
while a==0:
    print ("Ошибка а не должно быть равно 0")
    a = int(input("Введите а: "))
while b==0:
    print ("Ошибка а не должно быть равно 0")
    b = int(input("Введите b: "))
z=abs(pow(((a*a-b*b*b-c*c*c*a*a)*(b-c+c*(k-d/(b*b*b)))-(k/b-k/a)*c),2)-20000)
print("Значение выражения",z)

print ("Задание 2")
q = [1, 2, 3, 4, 5,6,7,8,9,10,"a","b","c","d"]
print("Вывод нечетных элементов")
for i in range(0,len(q)):
        if i % 2 == 0:
            print(q[i])

print ("Задание 3")
q=[1,2,3,4,5,999,7,8,9,10,6,332,99]
m=0
for i in range(0,len(q)):
    if ((q[i]>=1) and (q[i]<=10)):
        m+=q[i]
print ("Результат сложения чисел от 1 до 10: ",m)

print ("Задание 4")
l=[-10,5,4,8,6,-99,55]
L=min(l)
print("Минимальное число: ",L)

input('Press ENTER to exit')