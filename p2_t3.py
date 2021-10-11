a = int(input("Введите год:"))
if (a%2==0) and (a% 100!=0) or (a%400!=0):
  print("Високосный")
else:
  print ("Невисокосный")