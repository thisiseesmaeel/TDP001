sum = 0

for numbers in range (0,513):
    sum += numbers
print(sum)

# total = 1

# for numbers in range (1,513):
#     total *= numbers
# print(total)

# right_number = False
# wrong_number = 1
# wrong_number_max = 1

# while right_number is False:
#     for wrong_number_max in range (1, 14):
#         if wrong_number % wrong_number_max != 0:
#             break
#         if wrong_number_max == 13:
#             right_number = wrong_number 
#     wrong_number += 1

# print (f'Detta är rätt nummer: {right_number}')

# min_num = 2
# max_num = 1000
# total = 0

# for number in range (3, 1001, 2):
#     for modolus in range (2, number):
#         if number % modolus == 0:
#             break
#     else:
#         total += number
#         print(f'Detta är summan av alla primtal under 1000: {total}')
