#Viết chương trình tối ưu chuỗi
def ToiUuChuoi(s):
    s2 = s
    s2 = s2.strip()  # Loại bỏ khoảng trắng đầu và cuối
    arr = s2.split(' ')  # Tách chuỗi thành mảng các từ dựa trên khoảng trắng
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) > 0:  # Chỉ giữ các từ có độ dài lớn hơn 0
            s2 = s2 + word + " "
    return s2.strip()  # Loại bỏ khoảng trắng thừa ở cuối

# Ví dụ sử dụng
s = "   Trấn   Duy   Thanh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))