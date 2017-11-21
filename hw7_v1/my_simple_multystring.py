# module level variables
_MIN_LEN = 1
_MAX_LEN = 50
_DEFAULT = "undefined"
varx = "global"

print()
print("<< printing from my_simple_multystring.py >>")
print("module name:", __name__)
print('before class: varx =', varx)


def my_addition(x, y):
    return x + y


class Weight(object):
    def __init__(self, val, unit):
        self.val = val
        self.unit = unit


class TripleString(object):
    """TripleString docstrings."""


    _count = 0  # class level variables
    LUCKY_NUM = 3
    varx = "class"
    print("from class: varx =", varx)

    @staticmethod
    def _is_valid(the_str):
        varx = "static method"
        if not (_MIN_LEN <= len(the_str) <= _MAX_LEN):
            raise ValueError('String length must be between {} and {} chars long'.format(_MIN_LEN, _MAX_LEN))
        return True

    def __init__(self, string1=_DEFAULT, string2=_DEFAULT, string3=_DEFAULT):
        """Must provide string1, string2, string3."""

        varx = "init"
        self.string1 = string1  # calls setters
        self.string2 = string2
        self.string3 = string3
        self.simple_var = 5
        TripleString._count += 1

    def abbreviate(self):
        return "".join([self.string1[0], self.string2[0], self.string3[0]])

    def __repr__(self):
        return '{0.__name__} ("{1}", "{2}", "{3}")'.format(
            type(self), self.string1, self.string2, self.string3)

    def __eq__(self, other):
        return self.string1 == other.string1 and self.string2 == other.string2 and self.string3 == other.string3

    @property
    def string1(self):
        varx = "property"
        return self.__string1

    @string1.setter
    def string1(self, value):
        varx = "setter"
        if TripleString._is_valid(value):
            self.__string1 = value

    @property
    def string2(self):
        return self.__string2

    @string2.setter
    def string2(self, value):
        if self._is_valid(value):
            self.__string2 = value

    @property
    def string3(self):
        return self.__string3

    @string3.setter
    def string3(self, value):
        if self._is_valid(value):
            self.__string3 = value

    @classmethod
    def from_list(cls, lst):
        varx = "class method"
        if not isinstance(lst, list) or len(lst) > 3:
            raise ValueError("expected 3 list items")

        l = len(lst)
        if l == 0:
            return cls()
        elif l == 1:
            return cls(string1=lst[0])
        elif l == 2:
            return cls(string1=lst[0], string2=lst[1])
        elif l == 3:
            return cls(string1=lst[0], string2=lst[1], string3=lst[2])


print('after class, varx =', varx, '\n--------------------------\n')

if __name__ == '__main__':
    print('Testing TripleString')

    t = TripleString(string1='1test', string2='2test', string3='3test')
    print(t)
