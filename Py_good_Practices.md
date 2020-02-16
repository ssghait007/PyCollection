  

1. Ternary operators:

  
```
x=1 if condition else 0

  ```

2. F strings

  
```
print(f'{total:,}')
```
- total is number we r using separator as , we can use _ in number to read properly , that will noy affect calculations

3. Context manager

- manually closing file, thread, DB connections handling
```
with open('f.txt' , 'r') as f:

file= f.read()
```
- anytime you are setting up and tearing down resources

4. Enumerate for getting index in loop
```
names=['a','b','c','d','e',]

for index, name in enumerate(names, start=1):

print(index, name)
```
- loop over two lists

- zip will stop after shortest list (in case of unequal) use zip_longest() for longest traversal

- values unpacked are tuple

  
```
names=['a','b','c','d','e',]

heroes=['a','b','c','d','e',]

for name,hero in zip(names, heroes):

print(f'{name} is actually {hero}')
```
  

5. Tuple unpacking if u are just using one variable from tuple, assign underscore to others (mismatch of values gives error)

  
```
a,_=(1,2)

print(a)

a,b,*c=(1,2,3,4,5)

c=[3,4,5]

a,b,*_=(1,2,3,4,5)

now use a and b

a,b,*c,d=(1,2,3,4,5,6,7)

c=[3,4,5,6]
```

6. Class you can dynamically add the attributes

  
```
class Person:

pass

person=Person()

person.first='anderson'

last_key='last'

last_val='corey'

setattr(person,last_key,last_val)

getattr(person,last_key)

person_info={'first':'corey','last':'anderson'}

for key ,item in person_info.items():

setattr(person,key,value)
```

7. Sensitive info get from user

  
```
fron getpass import getpass

user=input('username:')

pass=getpass('password:')
```

8. -m using both below things run same program(if program is added in syspath directory)

  
```
python pass.py

python -m pass
```
9.  Will this compile??   
```
class Dog:
	def __init__(self):
		self.bark()
```


Yes because code is interpreted at runtime

 10. Will this compile
```
 def make_class(x):
	 class Dog:
		 def __init__(self,name):
			 self.name=name
		 def print_val(self):
			 print(x)
	return Dog

cls=make_class()
print(cls)
d=cls('tim')
print(d.name)
d.print_val()
>>> <class '__main__.make_class.<locals>.Dog'>
>>> tim
>>> 10
```
Yes all the values are checked at runtime, So even if outside variables (x) are used in class this will compile

11. func def
```
for i in range(10):
	def show():
		print(i*2)
	show()
>>> 0
>>> 2
>>> 4 ...
```
if func is declared outside it returns last value which is 18

12. diff function call based on argument
```
def func(x):
	if x == 1:
		def rv():
			print('x equals 1')
	else:
		def rv():
			print('x not equal to 1')
	return rv
new_func = func(1)
new_func()
new_func = func(10)
new_func()

>>> x equals 1
>>> x not equal to 1
``` 

13. inspect module to get inside properties and source code 
```
import inspect

inspect.getmembers(func) #get properties and methods
inspect.getsource(func) # gets source code o func

``` 
