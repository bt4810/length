number = [1, 2, 3, 4, 5]
user_input = int(input("Enter:"))
user_input = number[3]
number.pop()
del number[-1] 
print("list of number:", len(number))