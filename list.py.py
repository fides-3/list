my_list=[]
my_list.append([10,20,30,40])
print("afterappend:",my_list)
my_list.insert(1,15)
print("afterinsert:",my_list)
my_list.extend([50,60,70])
print("listafterextend:",my_list)
my_list.pop()
print("afterremove:",my_list)
index_of_30=my_list.index(30)
print(index_of_30)

