a=int(input())
b=int(input())
if b==0:
  print('на ноль делить нельзя!')
elif a%b>0:
  print('нацело не делится, но остаток равен - ', a%b, ', а частное равно - ', a/b, sep='')
else:
  print('делится, ответ: ', a//b)
