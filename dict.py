######class dict(**kwarg) or dict(mapping,**kwarg) or dict(iterabl,**kwarg)
'''
			Mapping Types - dict
   dict or dictionary can be used to store the key value pair, it is mutable objects. 
	a dict keys are almost arbitrary values. values that are not hashable. that is value containing list, dictionaries or other mutable types

	return a new dictionary initialized from an optional positional argument. the position argument must be mapping or iterable
	
	before 3.7 dict does not maintain the insertion order, if you need you can use collections.OrderedDict.
	after 3.7 it will maintain the LIFO order in dict

	if the key is mulitple time declared then it will override the last one

	while iterating the dict then adding element to the same dict it will raises the RuntimeError

	
'''
a = dict() ## creates empty dict
print(a)

##a = dict(1='one',1.0='one.one',2='two') ## keyword cannot be an a expression
a = {1:'one',1.0:'one.one',2:'two'}
print(a)

a = dict(one=1,two=2,three=3) #kwargs
b = {'one':1,'two':2,'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2),('three',3),('one',1)])
e = dict({'one':1,'two':2,'three':3})
print(a == b == c == d == e)

'''
	len(d) - return the number of items
'''
print(len(d))
'''
	d[key] - return the item with key key,if key is not in the map Raises a KeyError
	the subclass of dict defines method __missing__() and key is not present it calls , if this method is not found then it throughs on exeception

	Ex: collections.Counter using __missing__ method

'''
print(d['one'])
#print(d['one1']) #KeyError
d['one']=10 ## it is used to set value
print(d['one'])
del d['one'] ## delete key from the dict
print('one' in d) ## return true if the key is available in the dict
print('one' not in d) ## reutrn true if the key is not available.
print(iter(d))


print(iter(d.keys())) ## return iteration over keys
for key in d.keys():
     print(key)
a.clear() ## clear elements from the dict
print(a)
a = b.copy() ## returns a shallow copy(exact copy of original ie just reference address are copied) of the dictionary
print(a)

'''
	classmethod fromkeys(seq,[value])
create the new dictionary with keys from seq and values set to value.
value default to None.
'''
seq = {'a','e','i','o','u'}
az = dict.fromkeys(seq);
print(az)
value = [1]
az = dict.fromkeys(seq,value);
print(az)
value.append(2) # when the mutable object is modified each element of the sequence also updated. ie points to the same object in the memory. to avoid this issue we use dictionary comprehension
print(az)
#dict comprehension
az = {key:list(value) for key in seq}
print(az)
value.append(3) 
print(az)
'''
	get(key[,default])
return the value for the key otherwise default will return
'''
print(b.get('one')) #it will return the value
print(b.get('asdfas')) # it will return the None 
'''
	items() 
	returns the view of the dict items (key,value) paris
'''
for key,value in d.items():
     print(key,"---",value)
'''
	keys()
return the view of the dict keys
'''
for key in d.keys():
     print(key)
'''
	pop(key[,default])
if key is in the dict, remove it and reutrn its value. else return default.
if default does not provide returns rises KeyError
'''
print(d)
print(d.pop('one',None)) ## key is not there so it return default - None
#print(d.pop('one')) ## key is not there so it raises KeyError
print(d.pop('two'))
d.setdefault('one',1)
print(d)

'''
	popitem()
remove and return a (key, value) pair from the dictionary. pairs are returned in LIFO order

if dict is empty then raise KeyError
in Version 3.7 LIFO order is now guaranteed. in prior version, popitem() would return any arbitrary key/value pair.
'''
d=dict([('two',2),('three',3),('one',1)])
d.setdefault('zero',0)
print(d)
a = d.popitem()
print(a)
a = d.popitem()
print(a)
a = d.popitem()
print(a)
a = d.popitem()
print(a)
#a = d.popitem() dict d is empty so it raises KeyError
#print(a)
'''
	setdefault(key[,value])
if key in the dict it return value, if not, insery key with a value of default and return default
'''
d=dict([('two',2),('three',3),('one',1)])
print(d.setdefault('zero',0))
print(d.setdefault('one',10))
'''
	update([other])
update the dict with the key/value pairs from other, overwriting existing keys, Return None
if the key is not available it will add the key to the dict.
it accepts another dict or iterable
'''
d=dict([('two',2),('three',3),('one',1)])
print(d)
d_new = dict({'ten':10});
d.update(d_new)
print(d)
print(d_new)
d_new = dict([('ten','ten'),('one','one')]);
d.update(d_new)
print(d)
print(d_new)
'''
	values()
return a values of the dict
	
'''
print(d.values());
print(list(d)) ## return key as a list
print(list(d.keys()))
print(list(d.values()))
d = dict({None:1,None:'asdf','test':'asdfasdfas'})
print(d)
