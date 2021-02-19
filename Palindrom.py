liche = 0
sude = 0
def reverse(text):
  return text[::-1]
def is_palindrome(text):
  return text == reverse(text)
celkem = 0
with open("syn2010_word.vyber-ascii.txt", "r") as syn2010_word:
  for line in syn2010_word.readlines():
      newline = line.rstrip()
      if len(newline) > 3:
          if (is_palindrome(newline)):
              celkem = celkem + 1
              if len(newline) % 2 == 0:
                  with open("palindromy-sudé.txt", "a") as file:
                      file.write(line)
                  sude = sude + 1
              else:
                  with open("palindromy-liché.txt", "a") as file:
                      file.write(line)
                      liche = liche + 1
print(sude)
print(liche)
print(celkem)