# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:48:03 2017

@author: Kai
"""
def plural(word):  
  if word.endswith('y'):  
     return word[:-1] + 'ies'  
   elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:  
      return word + 'es'  
   elif word.endswith('an'):  
      return word[:-2] + 'en'  
   else:  
       return word + 's'

t=input('Enter a sentence:')
l=t.split()
a=" ".join([plural(word) for word in l])

plural(a)
print(a)


