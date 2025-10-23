#Viết Hàm tính ROI
def ROI(dt, cp):
    return (dt - cp) / cp

def GoiYDaTu(roi):
    if roi > 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

# Chương trình chính
print("Chương trình tính ROI")
dt = int(input("Nhập Doanh Thu: "))
cp = int(input("Nhập chi phí: "))

roi = ROI(dt, cp)
print("Tỉ Lệ ROI =", roi)
print("==>", GoiYDaTu(roi))