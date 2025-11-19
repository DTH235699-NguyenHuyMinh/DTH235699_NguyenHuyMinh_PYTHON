M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

odd = [x for x in M if x % 2 != 0]
even = [x for x in M if x % 2 == 0]
prime = [x for x in M if is_prime(x)]
non_prime = [x for x in M if not is_prime(x)]

print(f"Các số lẻ: {odd}, tổng cộng: {len(odd)}")
print(f"Các số chẵn: {even}, tổng cộng: {len(even)}")
print(f"Các số nguyên tố: {prime}")
print(f"Các số không phải nguyên tố: {non_prime}")
