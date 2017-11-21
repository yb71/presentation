'''
Classes with no explicit metaclass are built by the type metaclass

clattered namespace

an "ordinary" class defines the behavior of the instances of the class,
a metaclass defines the behavior of classes and their instances.
'''


def init(self, string1="undefined", string2="undefined", string3="undefined"):
    self.string1 = string1
    self.string2 = string2
    self.string3 = string3

def abbreviate(self):
    return "".join([ self.string1[0], self.string2[0], self.string3[0] ])

def repr(self):
        return '{0.__module__}.{0.__name__} ("{1}", "{2}", "{3}")'.format(
            type(self), self.string1, self.string2, self.string3)


attrs = {'__init__': init, 'abr': abbreviate, '__repr__': repr, 'LUCKY_NUM': 3}
superclasses = (object,)

TripleString = type('TripleString', superclasses, attrs)  # a new type

t1 = TripleString('a', 'b', 'c')
print(t1)
print(type(t1))

