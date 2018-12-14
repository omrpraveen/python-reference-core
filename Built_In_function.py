##### - headers

#####abs()
'''
    Return the absolute value of a number.
    The argument may be an integer or a floating point number
    If the argument is a complex number, its magnitude is returned.
    magnitude of complex number (a-bj) is sqrt(a** + b**)
'''
print(abs(-6)); # 6
print(abs(-6.6)); #6.6
print(abs((3-4j))); #5.0
#####all(iterable)
'''
    returns true if all elements are true or empty, it can take input as a iterable(list,set,tuples,dictionaries)

'''
print(all([1,2,3])) # true
print(all([1,2,0])) # false
print(all('00')) # true because this is a string
print(all({0: 'True', 2: 'False'})) # false
print(all({1: 'True', 2: False})) # true because in dictionaries it will check key only not values

#####any(iterable)
'''
    return true if any of the elements is true, if it is empty it is false,
'''
print(any([0,1])) ## true
print(any({0: 'True', 1: 'False'})) ##true
print(any('')) #false

#####ascii(obj)
#'''
    #return printable representation of an object,
    #but excape the ascii character of an a string using \x,\u or \U

    #For example, ö is changed to \xf6n, √ is changed to \u221a
#'''
print(ascii('ö'))
print(ascii('asdfasdföasdfasf'))


#####bin(x)
'''
    The bin() method converts and returns the binary
    equivalent string of a given integer.
    If the parameter isn't an integer, it has to implement __index__() method to return an integer.
    or else it throws TypeError
'''
print(bin(10)) #0b1010
#print(bin(a)) # return TypeError
class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple+self.orange+self.grapes

    #bool(object) if input is object then it will check
    #__bool__ in first if it is not available then it will check __len__
    def __bool__(self):
        return self.apple>0

    def __len__(self):
        return 0

    def __init__(self,apple=10):
        self.apple=apple;



print(bin(Quantity())); #0b101

#####bool([value])
'''
    The bool() method converts a value to Boolean
    (True or False) using the standard
    truth testing procedure.
'''
print(bool(0)) # false
print(bool('')) #false
print(bool(None)) #false
print(bool([0,0.0,0j])) #true
print(bool(Quantity())) #
#####breakpoint()
'''
    it is new built in funciton introduced in python 3.7
    in earlier version python debugging is a painfull because it is tight coupling between the actual
    code and the debugging module code.

    Ex:
        if you are using pdb('refer breakpoints_cmd.py') then you will have to call pdf.set_trace() in code,
        if you want to change anyother debugger then you need to change web_pdb.set_trace() method.
        this causes a huge overhead in using python debugger and make the python code hard to debug and maintain.
    how it works:
        it internally calls sys.breakpointhook() function. sys.breakpointhook() calls import pdb; pdb.set_trace() function.
        we don't have to explicitly import pdb module.
    Stop Debugging:
        sys.breakpointhook() uses environment variable PYTHONBREAKPOINT to configure the debugger.
        if it is set to 0

        PYTHONBREAKPOINT=0 python3.7 Built_In_function.py
'''
x = 10
y ='Hi'
z = 'Hello'
print(x)
#breakpoint()
print(z)




#####bytearray()
#'''
#    it returns a bytearray object which is an array of the given bytes.
#    it is mutable(can be modified)
#    sequence of integers in the range of 0 <= x < 256
#    if we want the immutable(cannot modify) then use bytes() method.
#    it takes three optional paramets.
#        source(Optional) - source to initialize the array of bytes.
#        encoding (Optional) - if source is a string, the encoding of the string.
#        errors - if source is a string, the action to take when the encoding conversion
#        fails
#        There are six types of error response
#            strict - default response which raises a UnicodeDecodeError exception on failure
#            ignore - ignores the unencodable unicode from the result
#            replace - replaces the unencodable unicode to a question mark ?
#            xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
#            backslashreplace - inserts a "\uNNNN" espace sequence instead of unencodable unicode
#            namereplace - inserts a "\N{...}" escape sequence instead of unencodable unicode
#'''
string ='pythön!'
arr = bytearray(string, 'ascii','xmlcharrefreplace')
print(arr)
arr = bytearray(string, 'ascii','namereplace')

size = 5
arr = bytearray(size)
print(arr)
print(arr.__len__())

rList = [1,4,9,65]

arr = bytearray(rList)
print(arr)
##### class bytes([source[, encoding[, errors]]])
'''
    which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray
'''
string ='pythön!'
arr = bytes(string, 'ascii','xmlcharrefreplace')
print(arr)
arr = bytes(string, 'ascii','namereplace')

size = 5
arr = bytes(size)
print(arr)
print(arr.__len__())

rList = [1,4,9,65]

arr = bytes(rList)
print(arr)
#####callable(obj)
'''
    it returns true if the object passed appears callable. other wise false
'''
x =10;
print(callable(x)) # false
def testFunction():
    print("callable")
y = testFunction
print(callable(y)) # true



#####chr(i)
'''
    it returns a unicode character from an integer
    input is integer and The valid range of the integer is from 0 through 1,114,111.
    if i is outside the range then it throws ValueError
'''
print(chr(97)) # a
print(chr(1114111))
##### @classmethod
'''
    a class method is a method that is bound to a class rather than its object.
    it does not require creation of a class instance. like staticmethod

    The difference between a static method and a class method is:

        Static method knows nothing about the class and just deals with the parameters
        Class method works with the class since its parameter is always the class itself.
    you can access classmethod like this,
        Class.classmethod()
            Or even
        Class().classmethod()
'''
## we can define classmethod in many ways.
class Persion:
    age = 25
    def printAge(cls):
        print(cls.age)

Persion.printAge = classmethod(Persion.printAge) #this convert the method to a class method so that it accepts the first parameter as a class.
Persion.printAge()
'''When to use the class method
    1.Factory Methods
    2.Correct instance creation in inheritance

    Factory Method:
        it returns a class object for different use cases.
'''
from datetime import date
class Persion1:
    def __init__(self,name,age):
        self.name= name
        self.age = age

    @classmethod
    def calculageAge(cls,name,birthYear):
        return cls(name,date.today().year - birthYear)

    def displayAge(self):
        print(self.name," is ",self.age)

persion = Persion1('Test1',20)
persion.displayAge()

persion1 = Persion1.calculageAge('Test2',1992) ## it will create the object of Persion class
persion1.displayAge()
'''
    Correct instance creation in inheritance
'''
from datetime import date
class Parrent:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    @staticmethod
    def fromFathersAge(name,fatherAge):
        return Parrent(name,fatherAge)
    @classmethod
    def fromBirthYear(cls,name,birthYear):
        return cls(name,date.today().year - birthYear)

    def displayAge():
            print(self.name," is ",self.age)

class Child(Parrent):
    sex = 'Male'

child = Child.fromBirthYear('test',1999)
print(isinstance(child,Child))

child1 = Child.fromFathersAge('test1',12)
print(isinstance(child1,Child))
#####compile()
'''
     compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

the compile method is used if the python code is in string form or is an AST object, and you want to change it to  a python code object

the exec() and eval() which will execute dynamically generated python code.

	source -- normal string, byte string or AST object.
	filename - file from which the code was read, if it wasn't read from a file, you can give a name yourself.
	mode - Either exec or eval or single.
		eval - accepts only a single expression.
		exec - it can take a code block that has python statements, class and unctions and so on.
		single - if it consists of a single interactive statement.
	flag and dont_Inherit (optional) controls which future statements affect the compilation of the source. Default value is 0.

	optimize - optinal, optimization level of the compiler. Default value -1

'''
code = '''
a=5
b=6
print(a+b)
'''
exec(compile(code,'somefilename','exec'))

#####complex() complex(real,imag)
'''
	it returns a complex when real and imaginary parts are provided or it converts a string to a comples number
	it takes two parameter
	real - real part, if real is omitted, it default is 0,
	imag - imaginary part, if imag is omitted, default is 0,
	if string must be like this real+imagj otherwise it throws ValueError

	there is no need to use complex() while you are declaring is also possible
	a=2+3j

	
'''
z = complex(1,2) #(1,2j)
print(z)
z = complex(1) #(1,0j)
print(z)
z=complex() #(0,0j)
print(z)
z= complex('1-3j') # (1-3j)
print(z)
#z=complex('1-4i') #ValueError
print(z)
a=2+3j
print(type(a)) #complex

#####delattr(object,name)
'''
	deletes an attribute from the object . if the object allows it. it does not return any value.
we can use del operator also to delete
'''
class delattrex:
     x =10
     y =2
     z= 1
result = delattrex()
print(result.x)
delattr(delattrex,'x')
##print(result.x)  throws error AttributeError because it is deleted.
#####dict()
'''
dict - see dict.py
'''
#####dir()
'''
	returns the valid attributes of the object.
 if the object has __dir__() method, then this method will be called, 
'''
number =[1,2,3,4]
print(dir(number)) ## attributes of list
d = dict({'one':'1'})
print(dir(d))
print(dir()) ## it will print attributes of the current object
print(dir(Persion))
class Persion:
     def __dir__(self):
          return ['age','number']
tea = Persion()
print(dir(tea))

#####divmod()
'''
	takes two number and returns a pair of numbers consisting of the quotient and remainder
'''
print(divmod(4,2))
#####enumerate()
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
#####
'''
'''
