#Viết hàm đệ qui Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def list_fibo(n):
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        result.append(fibonacci(i))
    return result

# Ví dụ sử dụng
n = 9
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
print(f"Dãy Fibonacci từ 1 đến {n} là: {list_fibo(n)}")