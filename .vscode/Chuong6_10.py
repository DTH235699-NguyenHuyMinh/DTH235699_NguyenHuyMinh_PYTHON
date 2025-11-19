def nhap_ma_tran(m, n, name):
    print(f"Nhập ma trận {name}:")
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            val = float(input(f"{name}[{i}][{j}]: "))
            row.append(val)
        mat.append(row)
    return mat

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def xuat_ma_tran(M, name):
    print(f"Ma trận {name}:")
    for row in M:
        print('\t'.join(map(str, row)))

# Nhập kích thước ma trận
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = nhap_ma_tran(m, n, "A")
B = nhap_ma_tran(m, n, "B")

# Cộng ma trận
C = cong_ma_tran(A, B)
xuat_ma_tran(C, "A + B")

# Hoán vị ma trận
At = transpose(A)
Bt = transpose(B)
xuat_ma_tran(At, "A^T")
xuat_ma_tran(Bt, "B^T")
