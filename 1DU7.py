
import time
xs = 'A'



a = 6
b = True
while b:
  a = a + 6
  time.sleep(0.3)
  print( '{:^{spaces}}'.format(xs, spaces=a), sep='')
  if a == 60:
     b = False
  while b == False:
      a = a - 6
      print( '{:^{spaces}}'.format(xs, spaces=a), sep='')
      if a == 0:
         b = True
      time.sleep(0.3)


