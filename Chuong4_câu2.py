# Viết Hàm để chơi Game Đoán Số
from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    
    while solandoan < 7:
        solandoan += 1
        try:
            songuoi = int(input("Máy đã chọn [1..100], mời bạn đoán: "))
            print("Bạn đoán lần thứ", solandoan)
            
            if somay == songuoi:
                print("Chúc mừng bạn đoán đúng, số máy là =", somay)
                win = True
                break
            elif somay > songuoi:
                print("Bạn đoán sai, số máy > số bạn")
            else:
                print("Bạn đoán sai, số máy < số bạn")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            solandoan -= 1  # Không tính lần nhập sai
    
    if not win:
        print("GAME OVER!, số máy =", somay)
    
    hoi = input("Tiếp không? (Nhập 'k' để kết thúc): ").lower()
    if hoi == "k":
        break

print("Cám ơn bạn đã chơi Game!")