#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

specifiedList = 1, 2, 5, 45, 7, 9, 45, 5, 3, 3, 3

new_list = []

for i in specifiedList:
    if i not in new_list:
      new_list.append(i)  
print(f"Из списка {specifiedList}\nнеповторяющиеся элементы: {new_list}")

