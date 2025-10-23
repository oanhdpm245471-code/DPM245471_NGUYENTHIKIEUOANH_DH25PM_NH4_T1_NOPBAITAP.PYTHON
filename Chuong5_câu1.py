#Kiểm tra chuỗi đối xứng
def CheckDoiXung(s):
    flag = True
    len_s = len(s)
    for i in range(len_s // 2):
        if s[i] != s[len_s - 1 - i]:
            flag = False
            break
    return flag

def main():
    while True:
        print("Nhập 1 chuỗi: ")
        s = input()
        if CheckDoiXung(s):
            print("Chuỗi ban nhập đúng")
        else:
            print("Chuỗi ban nhập không đúng")
        
        print("Tiếp không Thím? (c/k): ")
        s = input()
        if s == "k":
            break
    
    print("CẢM ƠN THÍM")

main()