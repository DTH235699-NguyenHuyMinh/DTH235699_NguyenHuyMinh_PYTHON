thang = input("Nhập vào 1 tháng (1-12): ")

if thang == "1" or thang == "2" or thang == "3":
    print(f"Tháng {thang} thuộc quý 1")
elif thang == "4" or thang == "5" or thang == "6":
    print(f"Tháng {thang} thuộc quý 2")
elif thang == "7" or thang == "8" or thang == "9":
    print(f"Tháng {thang} thuộc quý 3")
elif thang == "10" or thang == "11" or thang == "12":
    print(f"Tháng {thang} thuộc quý 4")
else:
    print("Tháng không hợp lệ!")