word = input()
temp_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for t in temp_alphabets:
  while True:
    loc = word.find(t)
    if loc == -1:
      break
    word = word[:loc] + " " + word[loc+len(t):]
    count += 1

word = word.replace(" ", "")
if len(word):
  count += len(word)
  
print(count)