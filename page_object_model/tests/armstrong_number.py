def test_check_armstrong_number(num):
    temp = num
    digits = 0
    while num > 1:
        num = num%10
        digits += 1
    num = temp
    power = 0
    for i in range(0, digits+1):
        n = num/10
        power += n.__pow__(digits)

    if temp == power:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

    test_check_armstrong_number(153)
