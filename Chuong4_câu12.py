#Hàm oscillate
def oscillate(start, end):
    result = []
    # Tăng từ start đến end
    for n in range(start, end + 1):
        result.append(n)
    # Giảm từ end-1 về start với bước nhảy -2, sau đó điều chỉnh
    for n in range(end - 1, start - 1, -2):
        result.append(n)
    # Thêm các giá trị dao động bổ sung theo mẫu
    if start < 0:
        for n in range(start + 1, 0):
            result.append(n)
            result.append(-n)
        result.append(0)  # Thêm 0 một lần nữa
        for n in range(1, end + 1):
            result.append(n)
            result.append(-n)
    return result

# In kết quả
result = oscillate(-3, 5)
print(" ".join(map(str, result)))