F=int(input())
L=int(input())
typ=int(input("Тип линзы"))
if 2*F<L and typ!=1:
  print("действительное, перевернутое, уменьшенное")
elif F<L<2*F and typ!=1:
  print("действительное, перевернутое, увеличенное")
elif L<F and typ!=1:
  print("мнимое, прямое, увеличенное")
elif typ!=0:
  print("мнимое, прямое, уменьшенное")
else:
  print("изображения нет")