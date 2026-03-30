length = 5
total = 0
special_nums = []
palindromes = []


# def timer(num):


def isPalindrome(num):
    num_str = str(num)
    if (num_str[0] == num_str[-1] and num_str[1] == num_str[-2]): # since its only a 5 digit number, we can hard code this
        return True

num = 14041
isPalindrome(num)
print(palindromes)
