from random import randint

N = int(input("Nhập số phần tử N: "))

min_val = int(input("Nhập giá trị nhỏ nhất: "))
max_val = int(input("Nhập giá trị lớn nhất: "))

if max_val - min_val + 1 < N:
    print("Không thể tạo đủ N số ngẫu nhiên không trùng trong khoảng này!")
else:
    lst = []
    while len(lst) < N:
        num = randint(min_val, max_val)
        if num not in lst:
            lst.append(num)

    print("List ngẫu nhiên không trùng nhau:", lst)
