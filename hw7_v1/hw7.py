# 1a ---------------------------------------------------------------------
# import multystring


# 1b ---------------------------------------------------------------------
# import multystring
#
# print("<< printing from module {} >>".format(__name__))
# print()


# 2 ---------------------------------------------------------------------
# import multystring as ms
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

# from math import sqrt, log
#
# math.pi  # gives you no direct access to pi
# pi = 5
# print('pi =', pi)
# x = sqrt(pi)
# y = log(pi)


# 4a ---------------------------------------------------------------------
# from multystring import TripleString, varx
#
# assert varx == "global"
# varx = "test"
#
# t = TripleString.from_list(['one'])
# print(t)


# 4b ---------------------------------------------------------------------
# from multystring import TripleString, varx
# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
#
# graphviz = GraphvizOutput()
# graphviz.output_file = 'basic.png'
#
# with PyCallGraph(output=graphviz):
#     t = TripleString.from_list(['one', 'two', 'three'])


# 5a ---------------------------------------------------------------------
from multystring import TripleString

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
# print("t2.NUM ->", t2.LUCKY_NUM)
# print()
# print(t1.__dict__)
# print(t2.__dict__)


# 5b ---------------------------------------------------------------------

# t1.new_var = 'привет'  # additional attributes can be created
# print()
# print(t1.__dict__)


# 6a ---------------------------------------------------------------------
# from multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# t2 = TripleString.from_list(['a', 'b', 'c'])
#
# print(t1)
# print(t2)        # uses __repr__ method
# print(t1 == t2)  # uses __eq__ method


# 6b ---------------------------------------------------------------------
# from multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# print(t1)
#
# print(t1.abbreviate())
# print(TripleString.abbreviate(t1))  # alternative syntax for instance methods


# 7 ---------------------------------------------------------------------
# from multystring import TripleString
#
# print('Class attributes:\n')
# for item in dir(TripleString):
#     print(item, getattr(TripleString, item, None))

# 9 ---------------------------------------------------------------------
# from multystring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
#
# print('"Public" instance attributes:\n')
# for item in dir(t1):
#     if item[0] != '_':
#         print(item, '=', getattr(t1, item, None))
#
# print('\n--------------------\n')
# print('"Private" instance attributes:\n')
# for item in dir(t1):
#     if item[0] == '_' and item[1] != '_':
#         print(item, '=', getattr(t1, item, None))
#
#
# print('\n--------------------\n')
# print('"Magic" instance methods:\n')
# for item in dir(t1):
#     if item[0] == '_' and item[1] == '_':
#         print(item, '=', getattr(t1, item, None))
