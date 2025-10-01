n = int(input("Nhập số n (tối đa 2 chữ số): "))

chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n < 0 or n > 99:
    print("Số không hợp lệ!")
elif n < 10:
    print(chu_so[n].capitalize())
else:
    hang_chuc = n // 10
    hang_don_vi = n % 10
    doc = ""
    if hang_chuc == 1:
        doc = "Mười"
    else:
        doc = chu_so[hang_chuc].capitalize() + " mươi"
    if hang_don_vi == 0:
        print(doc)
    elif hang_don_vi == 1:
        print(doc + " mốt")
    elif hang_don_vi == 5:
        print(doc + " lăm")
    else:
        print(doc + " " + chu_so[hang_don_vi])