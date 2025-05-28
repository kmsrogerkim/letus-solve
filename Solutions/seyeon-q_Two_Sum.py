string = input("숫자들을 입력하세요")
target = int(input("타겟을 입력하세요"))
str_list = string.split()
num_list = []

for i in str_list:
    num_list.append(int(i))

length = len(num_list)

for i in range(0, length):
    for j in range(i+1, length):
        if(num_list[i]+num_list[j]==target):
            print("["+ str(i)+","+ str(j)+ "]")
