# #1 Countdown

# def countdown(num):
#     for x in range(num,0,-1):
#         print(x)

# new_count=countdown(500)

# #2 print and return

# def print_and_return(num1, num2):
#     print(num1)
#     return(num2)

# par = print_and_return(1,2)

# #3 first plus length

# def first_plus_length(list):
#     print((len(list)) + list[0])

# fpl = first_plus_length([10,45,56,35,25,35,456,245,25,356356,36,3254,25,346,346,346])

#4 greater values than second

# def values_greater_than_second(list):
#     new_list = []
#     if len(list) > 2:
#         for x in list:
#             if x > list[1]:
#                 new_list.append(x)
#         print(len(new_list))
#         return new_list
#     else:
#         return False


# vgts = values_greater_than_second([5,2,3,2,1,4])
# print(vgts)

#5 This length that value

# def length_and_value(num1, num2):
#     new_list = [num2]
#     new_list *= num1
    
#     print(new_list)

# lav = length_and_value(6,2)    