def get_check_digit(code):
    lst = [int(i) * int(code[i]) for i in range(len(code))]
    a = 0
    for numbers in lst:
        a += numbers
    return(a % 5)
print(get_check_digit('3125'))
print(get_check_digit('1234'))
print(get_check_digit('50697'))