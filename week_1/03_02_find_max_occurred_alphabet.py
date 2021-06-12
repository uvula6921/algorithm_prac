def find_alphabet_occurrence_array(string):
  alphabet_occurrence_array = [0] * 26

  for i in string:
    if str.isalpha(i):
      alphabet_occurrence_array[ord(i) - 97] += 1

  max = 0
  max_alphabet_index = 0
  
  for i, val in enumerate(alphabet_occurrence_array):
    if val > max:
      max_alphabet_index = i
      max = val
      
  print(chr(max_alphabet_index+ord("a")))
      
      
    



#   max_occurrence = 0
#   max_alphabet = alphabet_occurrence_array[0]
  
#   for alphabet in alphabet_array:
#     occurrence = 0
#     for char in string:
#       if char == alphabet:
#         occurrence += 1
        
#     if occurrence > max_occurrence:
#       max_occurrence = occurrence
#       max_alphabet = alphabet

#   return max_alphabet


find_alphabet_occurrence_array("hello my name is sparta")