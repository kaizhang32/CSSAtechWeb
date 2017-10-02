# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:33:37 2017

@author: Danni
"""

def plural(word):  
    if word[-2:] in ['ay','ey','iy','oy','uy']:  
        return word+ 's'
    elif word[-2:] in ['cy','by','dy','fy','gy','hy','jy','qy','ky','ly','my','ny','py','ry','sy','ty','vy','wy','xy','yy','zy']:
        return word[:-1] + 'ies'  
    elif word[-1] in 'sxoz' or word[-2:] in ['sh', 'ch']:  
        return word + 'es'    
    else:  
        return word + 's'
    
t=input('Enter a sentence:')
l=t.split()
a=" ".join([plural(word) for word in l])

plural(a)
print(a)