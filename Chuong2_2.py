
t = int(input("Nhập số giây: "))


hour = (t // 3600) % 24
minute = (t % 3600) // 60
second = (t % 3600) % 60


if hour >= 12:
    am_pm = "PM"
else:
    am_pm = "AM"


hour_12 = hour % 12
if hour_12 == 0:
    hour_12 = 12

print(f"{hour_12}:{minute}:{second} {am_pm}")
