def reverse_words(s):
    words = s.split()  # Split the sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words with whitespace
    return reversed_sentence

# Example usage
s = "Let's take LeetCode contest"
reversed_sentence = reverse_words(s)
print(reversed_sentence)
