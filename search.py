import random 
c=random.sample(range(1,1001), 100) #создаём список из случайных неповторяющихся значений
print("исходный список: ", c, "\n")

def select_sort(q): #функция сортировки выбором
   for i in range(0,len(q)):
    mn=q[i]
    for j in range(i,len(q)):
        if mn>q[j]:
            mn=q[j]
            mni=j
    q[i], q[mni] = mn, q[i]
               
def lin_poisk(x,spisok): #функция линейного поиска
    s=0
    j=0
    for i in range(0,len(spisok)):
            if x==spisok[i]:
                s+=1
                print(f"номер элемента, найденного линейным поиском: {i}, количество сравнений: {s}")
                j=i
                break
            else:
                s+=1
    if x!=spisok[j]:
            print('элемент не найден :(')
            
def bin_search(x,spisok): #функция бинарного поиска
    s=0
    left=0
    right=len(spisok)-1
    ind=-1
    while left<=right and ind==-1:
        mid=(right+left)//2
        if spisok[mid]==x:
            ind=mid
            s+=1
        else:
            if x<spisok[mid]:
                right=mid-1
                s+=1
            else:
                left=mid+1
                s+=1
    if ind!=-1:            
        print(f'номер элемента, найденного бинарным поиском {ind}, количество сравнений: {s}')
select_sort(c)
print("отсортированный список: ", c)
n=int(input("введите элемент, который требуется найти в списке: "))
lin_poisk(n,c)
bin_search(n,c)


