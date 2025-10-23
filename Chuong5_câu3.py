#Xử lý Tách chuỗi
def is_perfect_square(n):
    if n < 0:
        return False
    i = 0
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

# Kiểm tra các số
numbers = [1, 4, 9, 15, 16, 25]
for num in numbers:
    if is_perfect_square(num):
        print(f"{num} là số chính phương")
    else:
        print(f"{num} không phải là số chính phương")

