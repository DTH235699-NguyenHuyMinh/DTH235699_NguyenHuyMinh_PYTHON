import re

def NegativeNumberInStrings(s):
    """
    Hàm nhận vào một chuỗi s và xuất ra các số nguyên âm trong chuỗi.
    """
   
    numbers = re.findall(r'-\d+', s)
    
    
    negative_numbers = [int(num) for num in numbers if int(num) < 0]
    
    return negative_numbers

s = "abc-5xyz-12k9l--p"
result = NegativeNumberInStrings(s)
print("Các số nguyên âm trong chuỗi:", result)
