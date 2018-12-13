######class dict(**kwarg) or dict(mapping,**kwarg) or dict(iterabl,**kwarg)
'''
			Mapping Types - dict
   dict or dictionary can be used to store the key value pair, it is mutable objects. 
	a dict keys are almost arbitrary values. values that are not hashable. that is value containing list, dictionaries or other mutable types

	return a new dictionary initialized from an optional positional argument. the position argument must be mapping or iterable	
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
