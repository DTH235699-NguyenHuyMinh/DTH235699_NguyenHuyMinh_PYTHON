def ToiUuChuoiDanhTu(s):
    s = s.strip()
    
    words = s.split()
    
    words = [word.capitalize() for word in words]
    
    result = " ".join(words)
    
    return result

s = "    TRần    duY   Thanh  "
print("Chuỗi gốc:", repr(s))
s_optimized = ToiUuChuoiDanhTu(s)
print("Chuỗi tối ưu:", repr(s_optimized))
