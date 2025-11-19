n = int(input("Nhập số lượng phần tử n: "))
M = []
for i in range(n):
    num = float(input(f"Nhập M[{i}]: "))
    M.append(num)

M.sort(reverse=True)
print("Dãy số sau khi sắp xếp giảm dần:")
print(M)
