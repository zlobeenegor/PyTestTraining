#function
'''
from email import contentmanager
from importlib.resources import contents
from operator import contains
'''


"""
def autoword():
    print('this is resul of work function "autoword"')

autoword()

def mult2(c,w):
    result = c*w
    return(result)

print('Testin my functions')
resnum=mult2(2345897,4988867)
#restxt=mult2(autoword())

print(resnum)
#print(restxt)

print('Test my second function')
def mult3(c,w=True):
  if w:
      return  c*2
  else:
      return  c/20

v=3
z = mult3(v,1)
print(z)

# this is function write your word ander 70 spaces
def right_justify(wrd):
    space = ('-')
    cont = ('monty')
    result = (space*25)+cont+(space*25)
    return result

print ('Lets check the right_justify(monty) function 2022')
resultfmonty = right_justify('exelent')
print(resultfmonty)

# this function draw square with oyu given dimensions
'''
"""
'''
This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/


"""

from __future__ import print_function, division

# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
    

# here is a less-straightforward solution to the
# four-by-four grid

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()

comment = """
'''
'''
After writing a draft of the 4x4 grid, I noticed that many of the
functions had the same structure: they would do something, do
something else four times, and then do something else once.
So I wrote one_four_one, which takes three functions as arguments; it
calls the first one once, then uses do_four to call the second one
four times, then calls the third.
Then I rewrote print1beam, print1post, print4beams, print4posts,
print_row and print_grid using one_four_one.
Programming is an exploratory process.  Writing a draft of a program
often gives you insight into the problem, which might lead you to
rewrite the code to reflect the structure of the solution.
--- Allen
"""

print(comment)
'''
#def sqare_draw(x,y):
   
x = 10
y = x

plus   =  ('+')
minus   = ('--')
vertbar = ('|')
space = ('  ')


wight = int(x)
hight = int(y)

eqminus = int((wight-3)/2)
eqvertbar = int((hight-3)/2)
eqvertbar2 = int((hight-3)/2)



edgeH1 = plus+minus*eqminus+plus+minus*eqminus+plus
eqspace = eqminus
    
print (edgeH1)

while eqvertbar > 0:
        eqvertbar = eqvertbar-1
        print(vertbar+space*eqspace+vertbar+space*eqspace+vertbar)
       


print (edgeH1)

while eqvertbar2>0:
        eqvertbar2 = eqvertbar2-1
        print(vertbar+space*eqspace+vertbar+space*eqspace+vertbar)
    
print (edgeH1)


   # edgeH1 = plus+(minus*eqminus)+plus+(minus*eqminus)

    #print(edgeH1)

#sqare_draw(11,11)

