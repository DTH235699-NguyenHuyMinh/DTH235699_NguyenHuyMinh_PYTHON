import os

def LayTenFileDuoi(path):
    """
    Trả về tên file kèm đuôi từ đường dẫn
    """
    return os.path.basename(path)

def LayTenFileKhongDuoi(path):
    """
    Trả về tên file bỏ phần mở rộng
    """
    filename = os.path.basename(path)       
    name_only, ext = os.path.splitext(filename) 
    return name_only

duong_dan = r"d:\music\muabui.mp3"

print("Tên file kèm đuôi:", LayTenFileDuoi(duong_dan))
print("Tên file không đuôi:", LayTenFileKhongDuoi(duong_dan))
