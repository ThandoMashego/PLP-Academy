user_input = input("please enter numbers seperated by spaces")
input_list = user_input.split(" ")
numbers = []
for i in input_list :
    num = int(i)
    numbers.append(num)
    total_sum = sum(numbers)

print(numbers)
print(total_sum)