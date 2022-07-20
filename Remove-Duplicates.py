def remove_duplicates(test):
  print(test)
  check = {}
  print(check)
  for i in test:
    print(check)
    check[i] = check[i]+1 if check.get(i) else 1
  return(check.keys())
