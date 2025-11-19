N = int(input("Nhập số lượng phần tử của dãy: "))

lst = []

print("Nhập các số theo thứ tự tăng:")

for i in range(N):
    while True:
        num = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0 or num > lst[-1]:
            lst.append(num)
            break
        else:
            print(f"Số phải lớn hơn {lst[-1]}. Vui lòng nhập lại.")

print("Dãy số bạn vừa nhập là:", lst)
