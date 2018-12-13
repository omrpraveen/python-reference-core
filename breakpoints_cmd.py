import pdb;
'''
    pdb is a short form of python debugger

    debugger at command line:
        n -- execute next line
        c -- complete execution
        l -- list 3 lines befor and after current lines
        s -- step into function call
        b -- show ist of all break points
        b [int] -- b 15 set break points at line number 15
        b [functionname] -- b transform set break points for the functionname
        cl -- clear all the break points
        cl 15 -- clear break points at line number 10
        p -- print


'''
def transform(x,y):
    y = y**2
    x *=2
    z=x+y
    return z;

x=10
y=10
z=5

pdb.set_trace()
transform(x,y)
print('z = '+str(z))
n = transform(x,y)
print('n -- ',str(n))
