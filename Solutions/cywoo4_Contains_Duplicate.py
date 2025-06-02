def check(num_list):
    lenlist=len(num_list)
    for i in range(lenlist-1):
        for j in range(i+1,lenlist):
            if(num_list[i]==num_list[j]):
                print("true")
                return
    print("false")

list1=[0,0,3,4,5]
list2=[2,4,5,6,7,8]  
list3=[1,5,6,7,8,9,9,10]

check(list1)
check(list2)
check(list3)
