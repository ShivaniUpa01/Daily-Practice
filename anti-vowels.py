def anti_vowel(text):
  result = ""
  vowel = "aeiouAEIOU"
  for i in text:
    if i not in vowel:
      result += i
  return result
