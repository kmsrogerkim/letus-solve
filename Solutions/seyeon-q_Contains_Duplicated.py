list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 5]

def Dup(arr):
    ck = False
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                ck = True
                break
    print(ck)

Dup(list1)
Dup(list2)