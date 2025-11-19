# Câu 5: Xác định kết quả khi thực thi list

lst = [20, 1, -34, 40, -8, 60, 1, 3]

# (a) lst -> toàn bộ list
# Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]

# (b) lst[0:3] -> các phần tử từ index 0 đến 2
# Kết quả: [20, 1, -34]

# (c) lst[4:8] -> các phần tử từ index 4 đến 7
# Kết quả: [-8, 60, 1, 3]

# (d) lst[4:33] -> từ index 4 đến cuối (vượt quá độ dài list thì lấy đến cuối)
# Kết quả: [-8, 60, 1, 3]

# (e) lst[-5:-3] -> từ index -5 đến -3-1
# lst[-5] = 40, lst[-4] = -8
# Kết quả: [40, -8]

# (f) lst[-22:3] -> index âm vượt quá list → bắt đầu từ đầu (0)
# lst[0:3] = [20, 1, -34]
# Kết quả: [20, 1, -34]

# (g) lst[4:] -> từ index 4 đến hết
# Kết quả: [-8, 60, 1, 3]

# (h) lst[:] -> toàn bộ list
# Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]

# (i) lst[:4] -> từ đầu đến index 3
# Kết quả: [20, 1, -34, 40]

# (j) lst[1:5] -> từ index 1 đến 4
# Kết quả: [1, -34, 40, -8]

# (k) -34 in lst -> kiểm tra có phần tử -34 trong list không
# Kết quả: True

# (l) -34 not in lst -> kiểm tra -34 không có trong list
# Kết quả: False

# (m) len(lst) -> độ dài list
# Kết quả: 8
