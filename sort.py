import random
#создаем наш лист с сотней случайных элементов,котрые мы будем сортировать
list = random.sample (range(0, 1_000_000),100)
#добавляем те же значения листа во второй лист чтобы не переписывать его второй раз
list_1 = list
k = 0
m = 0
n = len(list) #длина листа
for i in range (n - 1): #задаем 1 список
    for j in range(0, n - i - 1 ): #задаем элемент который больше i
        if list [j] < list [j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
            k += 1 #добавляем счетчик  
            print("\n",list,k)

for i in range (n): #задаем 2 список
    min = i  #создаем минимальный элемент
    for j in range (i + 1, n):
        if list_1[j] > list_1[i]:
            min = j
    list_1[i], list_1[min] = list_1[min], list_1[i]
    m += 1 #добавляем счетчик 2
    print("\n",list_1,m)
    
print(" Количество сравнений в 1 списке", k)
print(" Количество сравнений во 2 списке ", m)
