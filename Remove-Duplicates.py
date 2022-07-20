def remove_duplicates(test):
  check = {}
  for i in test:
    check[i] = check[i]+1 if check.get(i) else 1
  return(check.keys())
