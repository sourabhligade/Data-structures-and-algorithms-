
WriteashortPythonfunctionthattakesastrings,representingasentence,
and returns a copy of the string with all punctuation removed. 
For exam- ple, if given the string "Let s try, Mike.", this function would return "Lets try Mike".

import re
def puntuation(s):
  newsent=re.sub(r'[^\s\w]','',s)
  return newsent

s='Let s try, Mike.'
print(puntuation(s))
