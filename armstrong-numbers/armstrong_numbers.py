def is_armstrong(number):
    str_num = str(number)
    res = 0
    for i in range(len(str_num)):
        res += pow(int(str_num[i]),len(str_num))

    return res == number