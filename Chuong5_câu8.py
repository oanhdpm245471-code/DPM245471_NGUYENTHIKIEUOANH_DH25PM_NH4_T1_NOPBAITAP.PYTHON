#Tách lấy tên bài hát
def count_words_and_chars(s):
    # Loại bỏ khoảng trắng thừa đầu/cuối
    s = s.strip()
    
    # Đếm số từ (tách bởi khoảng trắng)
    words = s.split()
    word_count = len(words)
    
    # Đếm số ký tự (không tính khoảng trắng)
    char_count = sum(1 for char in s if char != ' ')
    
    return word_count, char_count

# Nhập chuỗi từ người dùng
print("Nhập một chuỗi: ")
s = input()

# Tính và in kết quả
word_count, char_count = count_words_and_chars(s)
print(f"Số từ: {word_count}")
print(f"Số ký tự (không tính khoảng trắng): {char_count}")