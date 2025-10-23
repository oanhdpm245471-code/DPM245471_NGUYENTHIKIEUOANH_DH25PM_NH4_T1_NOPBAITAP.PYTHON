#Tính và xuất độ dài đoạn AB
import math

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    # Nhập toạ độ của điểm A
    xA = float(input("Nhập toạ độ x của điểm A: "))
    yA = float(input("Nhập toạ độ y của điểm A: "))
    
    # Nhập toạ độ của điểm B
    xB = float(input("Nhập toạ độ x của điểm B: "))
    yB = float(input("Nhập toạ độ y của điểm B: "))
    
    # Tính độ dài đoạn AB
    length_AB = distance_between_points(xA, yA, xB, yB)
    
    # Xuất độ dài đoạn AB
    print(f"Độ dài của đoạn AB là: {length_AB}")

if __name__ == "__main__":
    main()