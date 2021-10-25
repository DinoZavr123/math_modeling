a=int(input("1сторона"))
b=int(input("2чторона"))
c=int(input("3сторона"))
if c==a+b or a==c+b or b==c+a:
 print ("Не сущ")
elif a==b==c:
  print("Равносторонний")
elif a==b or b==c or c==a:
  print("Равноберенный")
else:
  print("Рвзносторонний")