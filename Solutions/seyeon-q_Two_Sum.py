string = input("숫자들을 입력하세요")
target = input("타겟을 입력하세요")
str_list = string.split()
num_list = []

for i in str_list:
    num_list.append(int(i))

length = len(num_list)

for i in range(0, length):
    for j in range(0, length):
        if (i!=j):
            if(num_list[i]+num_list[j]==target):
                print("["+i+","+ j+ "]")
