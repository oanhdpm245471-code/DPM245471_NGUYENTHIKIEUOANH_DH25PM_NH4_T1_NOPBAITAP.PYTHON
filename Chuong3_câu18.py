# Vẽ các hình dưới đây
n = int(input("Nhập chiều cao n: "))

print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\nHình 2:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 3:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
