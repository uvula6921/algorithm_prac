word = input().upper()
a_list = [0] * 26

for i in word:
  a_list[ord(i) - ord('A')] += 1
  
if a_list.count(max(a_list)) > 1:
  print('?')
else:
  print(chr(a_list.index(max(a_list))+ord('A')))