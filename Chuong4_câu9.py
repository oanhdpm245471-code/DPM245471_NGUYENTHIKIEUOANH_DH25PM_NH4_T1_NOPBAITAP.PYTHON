#Viết chương trình tính căn bậc 2 lồng nhau
def nested_square_root(x, n):
    result = x
    for i in range(n):
        result = result ** 0.5
    return result

def main():
    x = float(input("Nhập giá trị cần tính căn: "))
    n = int(input("Nhập số lượng dấu căn lồng nhau: "))
    
    if n < 1:
        print("Xin lỗi, số lượng dấu căn lồng nhau phải lớn hơn hoặc bằng 1.")
    else:
        result = nested_square_root(x, n)
        print(f"Căn bậc {2**n} của {x} là: {result}")

if __name__ == "__main__":
    main()