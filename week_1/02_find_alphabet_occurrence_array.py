def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
      if str.isalpha(i):
        alphabet_occurrence_array[ord(i) - 97] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
