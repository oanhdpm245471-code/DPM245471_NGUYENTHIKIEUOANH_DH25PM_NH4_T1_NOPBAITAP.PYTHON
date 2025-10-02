#Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
#(vd: n=35 => Ba mươi lăm, n=5 => năm). 
#hàm
def doc_so(n):
    if n < 0 or n > 99:
        return "Số không hợp lệ"

    speak_hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    speak_hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    hang_chuc = n // 10
    hang_don_vi = n % 10

    if n == 0:
        return "Không"

    if n <= 9:
        return speak_hang_don_vi[n]

    if n % 10 == 0:
        return speak_hang_chuc[n // 10]

    return speak_hang_chuc[hang_chuc] + " " + speak_hang_don_vi[hang_don_vi]

# Test với các số từ 0 đến 99
a = int(input("Nhập Một Số:"))
b = doc_so(a)
print(b)