# Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

thang = int(input("Nhập vào một tháng (1 - 12): "))

if 1 <= thang <= 3:
    print("Tháng", thang, "thuộc quý I")
elif 4 <= thang <= 6:
    print("Tháng", thang, "thuộc quý II")
elif 7 <= thang <= 9:
    print("Tháng", thang, "thuộc quý III")
elif 10 <= thang <= 12:
    print("Tháng", thang, "thuộc quý IV")
else:
    print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")

