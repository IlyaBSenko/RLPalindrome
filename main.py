length = 5
total = 0
special_nums = []
palindromes = []

def palindrome(num):
    num_str = str(num)
    if num_str == num_str[::1]:
        palindromes.append(num_str)

num = 12221
palindrome(num)
print(palindromes)
