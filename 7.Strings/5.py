def reverse_string(s, k):
    result = ''
    n = len(s)
    for i in range(0, n, 2 * k):
        result += s[i:i+k][::-1]  # Reverse the first k characters
        result += s[i+k:i+2*k]    # Append the remaining characters
    return result

# Example usage
s = "abcdefg"
k = 2
reversed_string = reverse_string(s, k)
print(reversed_string)
