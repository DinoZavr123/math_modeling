a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
if b==0:
  print ("ноль")

elif a%b==0:
  
  print(a/b)

elif a%b!=0:
  print(a/b, "Остаток",a%b)