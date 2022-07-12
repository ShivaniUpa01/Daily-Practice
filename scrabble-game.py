def scrabble_score(text):
  list1 = list(text)
  total = 0
  for item in list1:
    total += score[item.lower()]
  return(total)
