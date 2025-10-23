#Tối ưu chuỗi danh từ
def ToiUuChuoiDanhTu(s):
    # Bước 1: Loại bỏ khoảng trắng thừa, chuyển về chữ thường
    s = s.strip().lower()
    
    # Bước 2: Tách thành danh sách các từ
    words = s.split()
    
    # Bước 3: Viết hoa chữ cái đầu mỗi từ
    optimized_words = []
    for word in words:
        if word:  # Kiểm tra từ không rỗng
            optimized_word = word[0].upper() + word[1:]
            optimized_words.append(optimized_word)
    
    # Bước 4: Nối lại bằng một khoảng trắng
    return " ".join(optimized_words)

# --- Chương trình chính ---
print("Nhập tên cần tối ưu:")
s = input()

result = ToiUuChuoiDanhTu(s)
print("Kết quả:", result)