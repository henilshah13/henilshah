import addmodule
print(addmodule.msg)
print(addmodule.add(10,20))

line='-'*40
print(line)

import sys
print(sys.path)
#sys.path.append(r'C:\pythontraining\lib')
print(line)

import  addmodule as a
print(a.msg)
print(a.add(10,20))
print(line)

from addmodule import msg,add
print(msg)
print(add(10,20))
print(line)

from addmodule import msg as m,add as a
print(m)
print(a(10,20))
print(line)

from addmodule import *
print(msg)
print(add(10,20))
print(line)

import project.net.addmodule as a
print(a.msg)
print(a.add(10,20))
print(line)