# Palindrome Checker
# Create a function that checks if a given string is a palindrome (reads the same forward and backwards)
# examples:
# madam -> reverse same (madam)
# naman -> reverse same (naman)

def palindrome(text):
    rev_palindrome = ""
    for ch in text:
        rev_palindrome = ch + rev_palindrome
    return rev_palindrome


given_str1 = input("Please enter the string:")
result1 = palindrome(given_str1)
if given_str1 == result1:
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")

# result2 = palindrome("naman")
# print(result1)
# print(result2)
