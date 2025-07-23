# Hard coded Example
# expenses = [10.50, 8, 5, 15, 20, 5, 3]

# total = sum(expenses)
# # sum = 0

# # for x in expenses:
# #     sum += x

# # print('You spent R', sum, sep='')

# print('You spent R', total, sep='')

# Using range method
expenses = []

num = int(input("Enter number of expenses: "))

# for x in range(7):
for x in range(num):
    expenses.append(float(input("Please enter expense ")))

total = sum(expenses)

print(total)