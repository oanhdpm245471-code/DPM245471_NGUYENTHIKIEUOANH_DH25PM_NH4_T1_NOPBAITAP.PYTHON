# Viết Hàm tính BMI
def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi Béo"
    elif bmi <= 34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi <= 39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp Độ 3"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung Bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất Cao"
    else:
        return "Nguy Hiểm"

# Nhập dữ liệu từ người dùng
print("Nhập vào chiều cao:")
height = float(input())

print("Nhập vào cân nặng:")
weight = float(input())

# Tính BMI
bmi = BMI(height, weight)

# In kết quả
print("BMI của bạn =", bmi)
print("Phân loại bàn =", PhanLoai(bmi))
print("Nguy cơ bệnh của Thím =", NguyCoBenh(bmi))