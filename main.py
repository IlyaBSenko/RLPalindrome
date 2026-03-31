length = 5
total = 0
special_nums = []
palindromes = []
# TODO: Maybe account for overtime? Would be hard since that goes to POS Infinity



# def special_nums(num):
    # num_str = str(num)
    


# needs cleanup bad
def timer(timer_num):
    timer_num_int = int(timer_num)
    while (timer_num_int != 000):
        timer_num_int -= 1
        middle = (timer_num_int % 100) // 10
        right = timer_num_int % 10
        if (middle >= 6):
            middle = 5
        if (right == 0 and middle != 0):
            right = 9
        right -= 1
    return str(timer_num_int)




def isPalindrome(num_str):
    print(num_str)
    return (num_str[0] == num_str[-1] and num_str[1] == num_str[-2]) # since its only a 5 digit number, we can hard code this



def main(num_str):
    total = 0
    timer_num = '500'
    if (isPalindrome(timer(timer_num))):
        palindromes.append(num_str)
        total += 1
    print(palindromes)



team1 = '0'
timer_num = '500'
team2 = '0'
num_str = team1 + timer_num + team2
main(num_str)

