#Phương trình bậc 2

from math import sqrt



print("CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC 2")



a = float(input("Nhập a: "))

b = float(input("Nhập b: "))

c = float(input("Nhập c: "))



if a == 0:

    if b == 0 and c == 0:

        print("Vô Số Nghiệm")

    elif b == 0 and c!=0:

        print("Vô Nghiệm")

    else:

        x=-c/b

        print("No X= ",x)

else:

    delta=b**2-4*a*c

    if(delta<0):

        print("Vô Nghiệm")

    elif(delta == 0):

        x=-b/(2*a)

        print("Có Nghiệm Kép x1=x2= ",x)

    else:

        x1=(-b-sqrt(delta))/(2*a)

        x2=(-b+sqrt(delta))/(2*a)

        print("X1 = ",x1)

        print("X2 = ",x2)