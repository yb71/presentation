# 1a ---------------------------------------------------------------------
# import triplestring

# 1b ---------------------------------------------------------------------
# import triplestring
#
# print("<< printing from module {} >>".format(__name__))
# print()


# 2 ---------------------------------------------------------------------
# import triplestring as ms
#
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
# pi = 5
# # print('my pi =', pi)
# print('math.pi =', math.pi)
# math.pi = 666  # you are unlikely do it just by accident
# print('my pi =', pi)
# print('math.pi =', math.pi)

# from math import *
#
# print(pi)
# pi = 777  # intended? much easier to overwrite by accident
# print(pi)

# from math import sqrt, log
#
# # print(pi)
# # print(math.pi)  # gives you no direct access to pi
# pi = 5            # clearly a local variable
# print('pi =', pi)
# x = sqrt(pi)
# y = log(pi)


# 4a ---------------------------------------------------------------------
# from triplestring import TripleString, varx
#
# assert varx == "triplestring global"
#
# varx = "test"
# t = TripleString.from_list(['one'])
# print(t)
# print('varx =', varx)
# print()

# 4b ---------------------------------------------------------------------
# from triplestring import TripleString
# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
#
# graphviz = GraphvizOutput()
# graphviz.output_file = 'diagram.png'
#
# with PyCallGraph(output=graphviz):
#     t = TripleString.from_list(['one', 'two', 'three'])


# 5a ---------------------------------------------------------------------
# from triplestring import TripleString
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
# print("t1.LUCKY_NUM ->", t1.LUCKY_NUM)
# print("t2.LUCKY_NUM ->", t2.LUCKY_NUM)
# print()
#
# t1.LUCKY_NUM = 666
# print("TripleString.LUCKY_NUM ->", TripleString.LUCKY_NUM)
# print("t1.LUCKY_NUM ->", t1.LUCKY_NUM)
# print("t2.LUCKY_NUM ->", t2.LUCKY_NUM)
# print()
# print(t1.__dict__)
# print(t2.__dict__)


# 5b ---------------------------------------------------------------------

# t1.new_var = 'hello'  # additional attributes can be created on the fly
# print()
# print(t1.__dict__)


# 6a ---------------------------------------------------------------------
# from triplestring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# t2 = TripleString.from_list(['a', 'b', 'c'])
#
# print(t1)
# print(t2)        # uses __str__ method
# print(t1 == t2)  # uses __eq__ method


# 6b ---------------------------------------------------------------------
# from triplestring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# print(t1)
#
# print(t1.abbreviate)
# print(t1.abbreviate())
# print(TripleString.abbreviate(t1))  # alternative syntax for instance methods


# 7a ---------------------------------------------------------------------
# from triplestring import TripleString
#
# print('Class attributes:\n')
# for item in dir(TripleString):
#     print(item, getattr(TripleString, item, None))

# 7b ---------------------------------------------------------------------
# from triplestring import TripleString
#
# t1 = TripleString('a', 'b', 'c')
# print('Object attributes:\n')
# for item in dir(t1):
#     print(item, getattr(t1, item, None))

# 8 ---------------------------------------------------------------------
# from triplestring import TripleString
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
