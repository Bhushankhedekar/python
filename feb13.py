# Slicing
# String iteration 
# # String method
# a = "Instagram"
# # -9    -8  -7  -6  -5  -4  -3  -2  -1
# #  I    N   S   T   A   G   R   A   M
# #  0    1   2   3   4   5   6   7   8
# # print(a[0:5]) # start index is included and end index is excluded

# # Case 1: Starting index is optional and default value is 0
# print(a[:5]) 
# print(a[3:6])

# # Case 2: End index is also optional and default value is length of string
# print(a[6:]) # start index is included and end index is excluded

# # Case 3: Both starting and end index is optional and default value of starting index is 0 and end index is length of string
# print(a[:]) # start index is included and end index is excluded

# # Prints blank space because starting and end index is same
# print(a[3:3]) 
# # Prints single character because end index is one more than starting index
# print(a[3:4])
# # prints string from starting index to end
# print(a[6:19]) 
# # print string with step valueof 2
# print(a[0:9:2])
# print(a[:9:2])
# print(a[::2])

# # print from 3 to 5
# print(a[3:6:1])
# # print from 6 to 4
# # 
# print(a[6:3:-1])

# # prints reverse of string
# print(a[::-1])
# print(a[-1:-10:-1])

# print(a[-6:8:1]) 
# print(a[-6:8:2]) 
# print(a[-6:8:5]) 

# Task :
# 5 positive + positive index
# 5 positive + negative index
# 5 negative + negative index
# 5 negative + positive index

# 5 on +ve step size >1 2 3 4 5
# 5 on -ve step size >-1 -2 -3 -4 -5

a = "Bhushan Khedekar"
#  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
#  B     H    U    S    H    A    N    K    H    E    D    E    K    A    R
#  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14

# 5 positive + positive index
print(a[0:15])
print(a[0:7])
print(a[7:15])
print(a[0:15:2])
print(a[1:5])

# 5 positive + negative index
print(a[0:-8])
print(a[7:-1])
print(a[0:-1])
print(a[0:-1:2])
print(a[: :-1])

# 5 negative + negative index
print(a[-9::-1])
print(a[-1:-9:-1])
print(a[-1:-15:-1])
print(a[-1:-15:-2])
print(a[:-16:-1])

# 5 negative + positive index
print(a[-1:0:1])
print(a[-9:15:1])
print(a[-9:15:2])
print(a[-9:15:3])
print(a[-9:15:4])

# 5 on +ve step size >1 2 3 4 5
print(a[0:15:1])
print(a[0:15:2])
print(a[0:15:3])
print(a[0:15:4])
print(a[0:15:5])

# 5 on -ve step size >-1 -2 -3 -4 -5
print(a[14:0:-1])
print(a[14:0:-2])
print(a[14:0:-3])
print(a[14:0:-4])
print(a[14:0:-5]) 
