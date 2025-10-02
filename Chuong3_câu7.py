#Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
#vừa nhập (ngày/tháng/năm).
#hàm
def ngay_nhuan(nam):
    if nam%4==0:
        if nam%100!=0 or nam%400==0:
            return True
    return False

def tim_ngay_ke(ngay, thang, nam):
    so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ngay_nhuan(nam):
        so_ngay_trong_thang[2] =  29

    if thang == 12 and ngay == 31:
        return 1, 1, nam+1
    elif ngay == so_ngay_trong_thang[thang]:
        return 1, thang + 1,nam
    else:
        return ngay + 1, thang, nam 

ngay = int(input("Nhập Ngày: "))
thang = int(input("Nhập Tháng: "))
nam = int(input("Nhập Năm: "))

ketqua_ngay = tim_ngay_ke(ngay,thang,nam)
print("Ngày kế sau là:", "/".join(map(str,ketqua_ngay)))