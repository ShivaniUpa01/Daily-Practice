def median(test):
  sort = sorted(test)
  length1 = len(sort)
  half = length1 / 2
  if length1 % 2 == 0:
    result = float(sort[half-1] + sort[half]) / 2
  else : 
    result = sort[half]
  return(result)
