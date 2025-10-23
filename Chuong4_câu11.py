#Kiểm tra kết quả thực hiện
def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

def main():
    global val
    val = 5
    print("sum1(5) =", sum1(5))
    print("sum2() =", sum2())
    print("sum3() =", sum3())

main()

# Trường hợp 2
def main2():
    global val
    val = 5
    print("sum1(5) =", sum1(5))
    print("sum3() =", sum3())
    print("sum2() =", sum2())

main2()

# Trường hợp 3
def main3():
    global val
    val = 5
    print("sum2() =", sum2())
    print("sum1(5) =", sum1(5))
    print("sum3() =", sum3())

main3()