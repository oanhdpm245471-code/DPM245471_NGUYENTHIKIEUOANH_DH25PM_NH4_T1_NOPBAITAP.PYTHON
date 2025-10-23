#Hàm kiểm tra số hoàn thiện, số thịnh vượng
def is_perfect_number(n):
    if n <= 0:
        return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

def is_abundant_number(n):
    if n <= 0:
        return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors > n

# Kiểm tra các số trong danh sách
numbers = [1, 2, 3, 6, 12]
for num in numbers:
    if is_perfect_number(num):
        print(f"{num} là số hoàn thiện")
    elif is_abundant_number(num):
        print(f"{num} là số dư thừa")
    else:
        print(f"{num} không phải là số hoàn thiện hoặc số dư thừa")

# Kiểm tra số dư thừa với danh sách khác
abundant_numbers = [12, 18, 20, 24, 30]
for num in abundant_numbers:
    if is_abundant_number(num):
        print(f"{num} là số dư thừa")