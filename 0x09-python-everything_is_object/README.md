# 0x09. Python - Everything is object

## Resources:books:
Read or watch:
* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/n1x09X-KJSllpJkJorBw2A)
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/3teQMNNfDeyGvCtZfjsf5g)
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/JuPVygeoG27Q_qKxB2lP8g)
* [Mutation](https://intranet.hbtn.io/rltoken/UbL96sV3cIxewdQPW_zwRw)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/-t_1VsmKlgWHszL5y1YiKA)
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/IdBAdTYNLuS3YpRRQIam6Q)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

---

### [0. Who am I?](./0-answer.txt)
* What function would you use to print the type of an object?


### [1. Where are you?](./1-answer.txt)
* How do you get the variable identifier (which is the memory address in the CPython implementation)?


### [2. Right count](./2-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
<pre>
>>> a = 89
>>> b = 100
</pre>


### [3. Right count =](./3-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
<pre>
>>> a = 89
>>> b = 89
</pre>


### [4. Right count =](./4-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
<pre>
>>> a = 89
>>> b = a
</pre>

### [5. Right count =+](./5-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
<pre>
>>> a = 89
>>> b = a + 1
</pre>

### [6. Is equal](./6-answer.txt)
* What do these 3 lines print?
<pre>
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
</pre>

### [7. Is the same](./7-answer.txt)
* What do these 3 lines print?
<pre>
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
</pre>

### [8. Is really equal](./8-answer.txt)
* What do these 3 lines print?
<pre>
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
</pre>

### [9. Is really the same](./9-answer.txt)
* What do these 3 lines print?
<pre>
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
</pre>

### [10. And with a list, is it equal](./10-answer.txt)
* What do these 3 lines print?
<pre>
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
</pre>

### [11. And with a list, is it the same](./11-answer.txt)
* What do these 3 lines print?
<pre>
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
</pre>

### [12. And with a list, is it really equal](./12-answer.txt)
* What do these 3 lines print?
<pre>
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
</pre>

### [13. And with a list, is it really the same](./13-answer.txt)
* What do these 3 lines print?
<pre>
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
</pre>

### [14. List append](./14-answer.txt)
* What does this script print?
<pre>
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</pre>

### [15. List add](./15-answer.txt)
* What does this script print?
<pre>
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</pre>

### [16. Integer incrementation](./16-answer.txt)
* What does this script print?
<pre>
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</pre>

### [17. List incrementation](./17-answer.txt)
* What does this script print?
<pre>
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</pre>

### [18. List assignation](./18-answer.txt)
* What does this script print?
<pre>
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</pre>

### [19. Copy a list object](./19-copy_list.py)
* Write a function def copy_list(l): that returns a copy of a list.
<pre>
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
</pre>

### [20. Tuple or not?](./20-answer.txt)
* a = ()



### [21. Tuple or not?](./21-answer.txt)
* a = (1, 2)



### [22. Tuple or not?](./22-answer.txt)
* a = (1)



### [23. Tuple or not?](./23-answer.txt)
* a = (1, )



### [24. Richard Sim's special #0](./24-answer.txt)
* What does this script print?
<pre>
a = (1)
b = (1)
a is b
</pre>

### [25. Richard Sim's special #1](./25-answer.txt)
* What does this script print?
<pre>
a = (1, 2)
b = (1, 2)
a is b
</pre>

### [26. Richard Sim's special #2](./26-answer.txt)
* What does this script print?
<pre>
a = ()
b = ()
a is b
</pre>

### [27. Richard Sim's special #3](./27-answer.txt)
<pre>
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
</pre>


### [28. Richard Sim's special #4](./28-answer.txt)
<pre>
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
</pre>


### [29. Python3: Mutable, Immutable... everything is object!](./100-magic_string.py)
* Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):


### [30. #pythonic](./101-locked_class.py)
* Write a function magic_string() that returns a string “Holberton” n times the number of the iteration (see code):
<pre>
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
Holberton$
Holberton, Holberton$
Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
</pre>

### [31. Low memory cost](./103-line1.txt)
* Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
<pre>
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
</pre>

### [32. int 1/3](./104-line1.txt)
* julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 



### [33. int 2/3](./105-line1.txt)
* julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 



### [34. int 3/3](./106-line1.txt)
* julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 



---

## Author
* **Samuel Martinez** - [samuelsrmv](https://github.com/samuelsrmv)