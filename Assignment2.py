my_list = []
my_list.append(10) 
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

another_list = [ 50, 60, 70]
my_list.extend(another_list)
del my_list[-1]

my_list.sort()

for index,value in enumerate(my_list):
    if value == 30 :
        print(index)




