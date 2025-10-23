#Vẽ hình dùng Sleep
import time
import os

for i in range(4):
    print("*" * (i + 1))  # In số sao tăng dần theo số lần lặp
    time.sleep(1)  # Dừng 1 giây sau mỗi lần in
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình (Windows: cls, Linux/Mac: clear)

print("*" * 4)  # In lần cuối sau khi kết thúc vòng lặp