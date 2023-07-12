def calculate_length(str):
    if str == "":
        return 0
    else:
        return 1 + calculate_length(str[1:])


str1 = "abcd"
print(calculate_length(str1))  # Output: 4

str2 = "GEEKSFORGEEKS"
print(calculate_length(str2))  # Output: 13
