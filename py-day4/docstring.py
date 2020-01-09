l=[]
print(dir(l))
print(help(l.pop))

import sys
print(help(sys))

def add():
    ''' desc about add called-doc string'''
    #some comment
    """some other comment"""

print(help(add))