# Xử lý chuỗi với các hàm cơ bản
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra các số
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
for num in numbers:
    if is_prime(num):
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải là số nguyên tố")