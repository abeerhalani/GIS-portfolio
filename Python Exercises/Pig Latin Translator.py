#This is a Pig Latin translator

pyg = 'ay' #this is the suffix to be added

original = raw_input('Enter a word: ') #this is the user's input

if len(original) > 0 and original.isalpha(): #this translates the input to pig latin
  word = original.lower()
  first = word[0]
  new_word = word[1:] + first + pyg
  print new_word
else:
    print 'empty' #this is if the user's input is invalid (contains an empty str or non-alphabet characters)