num_list = [1, 3, 5, 6, 8]
target = 8

length = len(num_list)

for i in range(0, length):
    for j in range(i+1, length):
        if(num_list[i]+num_list[j]==target):
            print("["+ str(i)+","+ str(j)+ "]")
