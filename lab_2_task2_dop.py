a=int(input())
b=int(input())
c=int(input())
if (a<(b+c) and b<(a+c) and c<(a+b)) and (a==c==b):
  print('треугольник существует и он равносторонний')
elif (a<(b+c) and b<(a+c) and c<(a+b)) and (a==b!=c or b==c!=a or a==c!=b):
  print('треугольник существует и он равнобедренный')
elif (a<(b+c) and b<(a+c) and c<(a+b)) and (a!=c!=b):
  print('треугольник существует и он разносторонний')
else:
  print('такого треугольника нет')