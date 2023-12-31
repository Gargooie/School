x = int(input("Введите кол-во мальчиков: "))
y = int(input("Введите кол-во девочек: "))

a = ""

for i in range((x + y) // 2):
  a += "B"
  x -= 1
  a += "G"
  y -= 1
print(a)

