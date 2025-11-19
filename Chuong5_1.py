def CheckDoiXung(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def main():
    print("Nhập 1 chuỗi:")
    s = input()
    if CheckDoiXung(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")

while True:
    main()
    print("Tiếp tục hay dừng lại? (c/k):")
    s = input().lower()
    if s == "k":
        break

print("CÁM ƠN")
