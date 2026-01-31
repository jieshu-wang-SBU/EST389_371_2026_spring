#%%
from typing import Callable

10 // 3
#%%
my_tuple = (1,[2,3],3)
my_tuple[1][0]=4.234
print(my_tuple)

#%%
my_range = range(10)
#%%
type(my_range)
#%%
[1,2,3][-2:]
#%%
plus: Callable[[int, int], int] = lambda x, y: x + y
#%%
class MyClass:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def greet(self):
        print(self.x, self.y, "hello")

my_class: MyClass = MyClass(x=1,y=2)
#%%
my_string = 'Jieshu'
my_string[1]='l'
print(my_string)
#%%
name="Alice"
price = 5000
print(f"Welcome, {{name}}! %B, %d, %y!"
      f"")
#%%
#BUG

name: str = 'Dr. Jieshu Wang'
if (num_char := len(name)) > 5:
    print(f'Your name has {num_char} characters and is too long')

#%%
price = {'apple': 2.5, 'water':1.99, 'steak': 19.39}
#%%
del price['apple']
#%%
set_ = {1, 2, 3}
print(set_)
#%%
set_.add('4')
print(set_)
#%%
list_ = (1,2,3,4)
#%%
{1,2} - {2, 3}
#%%
print(list_.pop())
#%%
def my_func(list_:list=[1,2]):
    return list_
#%%
li_ = [4, 1,2,3]
li_.sort(reverse=True)
print(li_)
#%%
number = 0
while number < 3:
    print(number)
    number += 1
else:
    print(f"end with {number}")
#%%
numbers = range(0, 10)
for number in numbers:
    if number == 5:
        break
    print(number)
#%%
numbers = range(0, 3)
squ = [i**2 for i in numbers]
#%%

#%%
def add(a: int, b: int = 1) -> int:
    """
    This function adds two numbers
    :param a: an integer
    :param b: an integer
    :return: an integer
    """
    c = a + b
    return c

result = add(a=2, b=3)
#%%
a = 1
print(f"{a=}")
#%%

#%%
from itertools import combinations

numbers = [1,2,3]
combination_of_numbers = list(combinations(numbers, 2))
print(combination_of_numbers)


#%%
import numpy as np

my_array = np.array([1, 2, 3], dtype=np.int64)
print(my_array)
#%%
a=[1,2,3]
print(id(a[0]))
a.pop()
print(id(a[0]))

#%%
import numpy as np
from datetime import datetime

list_op = lambda x: sum((tmp:=[(i**3)**0.5+1 for i in x]))/len(tmp)
array_op = lambda x: (np.power(np.power(x, 3), 0.5)+1).mean()

num = 1_000_000

speed = {}
for (op, array, name) in zip((list_op, array_op),
                             (list(range(1, num)), np.arange(1, num)),
                             ('Python list', 'numpy array')):
    start_time = datetime.now()
    result = op(array)
    end_time = datetime.now()
    speed[name] = (end_time - start_time).total_seconds()
    print(f"{name}: {end_time - start_time}")

print(f"numpy array operation is {speed['Python list']/speed['numpy array']:.0f} times of Python list operation")

#%%

#%%
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
for item in x:
    print(item)
#%%


#%%
import re

pattern = r"(EST)( |-)?(3[0-9]{2})"
course_list = ['EST389', 'EST 371', 'CSE 213', 'EST-303', 'EST 232']
for course in course_list:
    match = re.match(pattern, course)
    if match:
        print(course)


#%%