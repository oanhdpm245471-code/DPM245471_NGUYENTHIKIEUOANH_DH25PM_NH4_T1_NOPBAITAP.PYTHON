#Viết chương trình tính loga
import math

def log_base_a(x, a):
    if a <= 0 or a == 1 or x <= 0:
        return "Không hợp lệ (a > 0, a ≠ 1, x > 0)"
    return math.log(x) / math.log(a)

# Nhập dữ liệu từ người dùng
x = float(input("Nhập x (x > 0): "))
a = float(input("Nhập cơ số a (a > 0, a ≠ 1): "))

# Tính và in kết quả
result = log_base_a(x, a)
print(f"Logarit cơ số {a} của {x} là: {result}")