def is_int(x):
  print (x)
  n = abs(round(x)-x)
  type_n = type(n)
  if n == 0 and n == 0.0:
    return True
  else:
    return False
