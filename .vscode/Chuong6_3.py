from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = [randrange(100) for _ in range(n)]  # Mỗi hàng n phần tử
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

def LayDong(D, r):
    return D[r]

def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def XuatList1Chieu(lst):
    for element in lst:
        print(element, end='\t')
    print()

def MAX(D):
    max_val = D[0][0]
    for row in D:
        for val in row:
            if val > max_val:
                max_val = val
    return max_val

print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)
print("Ma trận ngẫu nhiên:")
XuatMaTran(D)

r = int(input("Mời bạn nhập dòng muốn xuất: "))
print(f"Dòng {r}:")
XuatList1Chieu(LayDong(D, r))

c = int(input("Mời bạn nhập cột muốn xuất: "))
print(f"Cột {c}:")
XuatList1Chieu(LayCot(D, c))

max_val = MAX(D)
print("Số lớn nhất trong ma trận =", max_val)
