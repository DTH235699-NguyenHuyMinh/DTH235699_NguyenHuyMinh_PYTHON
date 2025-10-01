x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
for i in range(n + 1):
    mu = 2 * i + 1
    tu = x ** mu
    mau = 1
    for j in range(1, mu + 1):
        mau *= j
    S += tu / mau
print("S({0}, {1}) = {2}".format(x, n, S))