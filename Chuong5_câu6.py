#Trích lọc số âm trong chuỗi
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

# Danh sách số nguyên mẫu
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính và in kết quả
result = sum_odd_numbers(numbers)
print(f"Tổng các số lẻ trong danh sách {numbers} là: {result}")