num_list=[3,5,6,9,10]
target=16
listlenght=len(num_list)

for i in range(listlenght-1):
    for j in range(i+1,listlenght):
        if (num_list[i]+num_list[j]==target):
            print("[%d,%d]"%(i,j))