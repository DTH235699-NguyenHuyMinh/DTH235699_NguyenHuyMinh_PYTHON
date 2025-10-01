n = int(input("Nhập chiều cao n: "))

# Hình vuông rỗng
print("Hình vuông rỗng:")
for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * n - 3) + '*')

print()

# Hình tam giác vuông cân (nguyên)
print("Hình tam giác vuông cân:")
for i in range(1, n + 1):
    print('* ' * i)

print()

# Hình chữ nhật rỗng (chiều rộng là n, chiều cao là n-1)
print("Hình chữ nhật rỗng:")
for i in range(n - 1):
    if i == 0 or i == n - 2:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * n - 3) + '*')

print()

# Hình chữ X
print("Hình chữ X:")
for i in range(n):
    line = ""
    for j in range(n):
        if j == i or j == n - 1 - i:
            line += "*"
        else:
            line += " "
    print(line)