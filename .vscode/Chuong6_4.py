# Câu 4: Xác định kết quả khi thực thi list

lst = [3, 0, 1, 5, 2]
x = 2

# (a) lst[0] -> phần tử ở vị trí 0
# Kết quả: 3

# (b) lst[3] -> phần tử ở vị trí 3
# Kết quả: 5

# (c) lst[x] -> lst[2] = 1
# Kết quả: 1

# (d) lst[-x] -> lst[-2] = phần tử thứ 2 từ cuối = lst[3] = 5
# Kết quả: 5

# (e) lst[x + 1] -> lst[3] = 5
# Kết quả: 5

# (f) lst[x] + 1 -> lst[2] + 1 = 1 + 1 = 2
# Kết quả: 2

# (g) lst[lst[x]] -> lst[lst[2]] = lst[1] = 0
# Kết quả: 0

# (h) lst[lst[lst[x]]] -> lst[lst[lst[2]]] = lst[lst[1]] = lst[0] = 3
# Kết quả: 3
