# Loops
# str = "welcome python"
# s = str.split()
# print(s)
# s.reverse()
# print(s)

#1. WAP to check string palindrom using for loop 
str = "nayan"
rev_str = ""
for i in str:
    rev_str = i + rev_str
if str == rev_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#2. WAP to check string palindrom using indexing 
# str = input("Enter a string: ")
# rev_str = ""
# for i in range(len(str)-1, -1, -1):
#     rev_str = rev_str + str[i]  
# if str == rev_str:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# str = "Bhushan Khedekar"
# if str == str[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# WAP to check digit palindrom by using for loop
# num = input("Enter a number: ")
# num = 121
# rev_num = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     rev_num = rev_num * 10 + digit
#     temp //= 10
# if num == rev_num:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

# WAP to check armstrong number by using for loop
# num = 153
# order = len(str(num))
# sum = 0
# temp = num
# for i in range(temp):
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if num == sum:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")


# num = int(input("Enter a number: "))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if num == sum:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")