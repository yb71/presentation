# 1 ---------------------------------------------------------------------
#######  module name
import my_simple_multystring

print()
# print("<< printing from hw7.py >>")
# print("file name:", __file__)
# print("this module's name:", __name__)
# print()

# 2 ---------------------------------------------------------------------
#######  the only true global variables are module level variables

# import my_simple_multystring as ms
#
# print()
# print("_MIN_LEN =", ms._MIN_LEN)
# print("_MAX_LEN =", ms._MAX_LEN)
#
# print()
# ms._MIN_LEN = 100
# ms._MAX_LEN = 0
# print("_MIN_LEN =", ms._MIN_LEN)
# print("_MAX_LEN =", ms._MAX_LEN)

# 3 ---------------------------------------------------------------------
#######  import statements

# import math
#
# print(math.pi)
# math.pi = 666
# print(math.pi)

# from math import *
#
# print(pi)
# pi = 777
# print(pi)

# from math import sqrt
# math.pi
# gives you no direct access to pi

# 4 ---------------------------------------------------------------------
#######  class level variable

# from my_simple_multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# t2 = TripleString('x', 'y', 'z')
# print(t1)
# print(t2)
# print()
#
# print("TripleString.LUCKY_NUM ->", TripleString.LUCKY_NUM)
# print("t1.LUCKY_NUM ->", t1.LUCKY_NUM)
# print("t2.LUCKY_NUM ->", t2.LUCKY_NUM)
# print()
#
# TripleString.LUCKY_NUM = 200
# print("TripleString.LUCKY_NUM ->", TripleString.LUCKY_NUM)
# print("t1.NUM ->", t1.LUCKY_NUM)
# print("t2.NUM ->", t2.LUCKY_NUM)
# print()
#
# t1.LUCKY_NUM = 666
# print("TripleString.LUCKY_NUM ->", TripleString.LUCKY_NUM)
# print("t1.NUM ->", t1.LUCKY_NUM)
# print(t1.__dict__)
# print("t2.NUM ->", t2.LUCKY_NUM)
# print(t2.__dict__)
# print()


####### Python classes are created at runtime, and can be modified further after creation

# t1.new_var = 'привет'  # additional attributes can be created
# print(t1.__dict__)


# 5 ---------------------------------------------------------------------
#######  class methods as alternative constructors

# from my_simple_multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# t3 = TripleString.from_tripleString(t1)
# print(t1)
# print(t3)
# print(t1 == t3)  # uses __eq__ method


# 6 ---------------------------------------------------------------------
#######  methods vs properties

# from my_simple_multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# print(type(t1))

# print(t1.abr())  # print(t1.abr)
# print(TripleString.abr(t1))

# for item in dir(TripleString):
#     print(item, getattr(TripleString, item, None))

# print('\n--------------------')
# print('"Public" attributes:\n')
# for item in dir(t1):
#     if item[0] != '_':
#         print(item, '=', getattr(t1, item, None))
# print()
#
#
# print('\n--------------------')
# print('"Private" attributes:\n')
# for item in dir(t1):
#     if item[0] == '_' and item[1] != '_':
#         print(item, '=', getattr(t1, item, None))
#
#
# print('\n--------------------')
# print('"Magic" methods:\n')
# for item in dir(t1):
#     if item[0] == '_' and item[1] == '_':
#         print(item, '=', getattr(t1, item, None))


