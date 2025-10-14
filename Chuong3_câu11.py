#Kiểm tra số nguyên tố

def la_so_nguyen_to(n):
    # Các số nhỏ hơn 2 không phải là số nguyên tố
    if n < 2:
        return False
    # Kiểm tra ước của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
    so = int(input("Nhập vào một số: "))

    if la_so_nguyen_to(so):
        print(so, "là số nguyên tố.")
    else:
        print(so, "không phải là số nguyên tố.")

    tiep_tuc = input("Bạn có muốn kiểm tra số khác không? (c/k): ")
    if tiep_tuc.lower() != 'c':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break