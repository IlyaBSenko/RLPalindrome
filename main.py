length = 5
total = 0
special_nums = []
palindromes = []


# also need to acount for overtime
# def special_nums(num):
    # num_str = str(num)
    


# def timer(num):


# also account for overtime
def isPalindrome(num):
    num_str = str(num)
    if (num_str[0] == num_str[-1] and num_str[1] == num_str[-2]): # since its only a 5 digit number, we can hard code this
        return True


num = 15001
starting_num = "05000" # since integers cant start with 0, and we need a starting number
isPalindrome(num)
print(palindromes)
