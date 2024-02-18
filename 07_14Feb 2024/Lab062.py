# Reverse the string
str1 = "naman"
rev_str = ""
for c in str1:
    rev_str = c + rev_str
print(rev_str)


# Method2 using function
def reverse_string(text):
    rev_str2 = ""
    for ch in text:
        rev_str2 = ch + rev_str2
    return rev_str2


original_str1 = input("Enter the string\n")
original_str1 = original_str1.lower()
result = reverse_string(original_str1)
print(result)

# palindrome - srt = rev_str ->Palindrome
if original_str1 == result:
    print("palindrome")
else:
    print("Not a palindrome")
