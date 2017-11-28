# module level variables
_MIN_LEN = 1
_MAX_LEN = 150
_DEFAULT = "undefined"
varx = "global"

print()
print("<<< printing from module {} >>>".format(__name__))
print('*** before class varx =', varx)


def my_addition(x, y):
    return x + y


class TripleString(object):
    """TripleString docstring"""

    _count = 0  # class level variables
    LUCKY_NUM = 5
    varx = "class"
    print("*** from class varx =", varx)

    @staticmethod
    def _is_valid(the_str):
        varx = "static method"
        if not (_MIN_LEN <= len(the_str) <= _MAX_LEN):
            raise ValueError('String length must be between {} and {} chars long'.format(_MIN_LEN, _MAX_LEN))
        return True

    def __init__(self, string1=_DEFAULT, string2=_DEFAULT, string3=_DEFAULT):
        varx = "init"
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        TripleString._count += 1
        self.id = TripleString._count

    def abbreviate(self):
        return "".join([self.string1[0], self.string2[0], self.string3[0]])

    def __repr__(self):
        return '{0.__name__} ("{1}", "{2}", "{3}")'.format(
            type(self), self.string1, self.string2, self.string3)

    def __str__(self):
        return '{0.__name__} #{1}:\n- string1: "{2}"\n- string2: "{3}"\n- string3: "{4}"\n'.format(
            type(self), self.id, self.string1, self.string2, self.string3)

    def __eq__(self, other):
        return self.string1 == other.string1 and self.string2 == other.string2 and self.string3 == other.string3

    @property
    def string1(self):
        return self.__s1

    @string1.setter
    def string1(self, value):
        varx = "setter"
        if TripleString._is_valid(value):
            self.__s1 = value

    @property
    def string2(self):
        return self.__s2

    @string2.setter
    def string2(self, value):
        if self._is_valid(value):
            self.__s2 = value

    @property
    def string3(self):
        return self.__s3

    @string3.setter
    def string3(self, value):
        if self._is_valid(value):
            self.__s3 = value

    @classmethod
    def from_list(cls, lst):
        varx = "class method"
        list_len = len(lst)
        if not isinstance(lst, list) or list_len > 3:
            raise ValueError("expected 3 list items")

        if list_len == 0:
            return cls()
        elif list_len == 1:
            return cls(string1=lst[0])
        elif list_len == 2:
            return cls(string1=lst[0], string2=lst[1])
        elif list_len == 3:
            return cls(string1=lst[0], string2=lst[1], string3=lst[2])


print('*** after class varx =', varx, '\n-------------------------------------------\n')


if __name__ == '__main__':
    the_three_laws = TripleString(
        string1='''A robot may not injure a human being or, through inaction, 
            allow a human being to come to harm.''',
        string2='''A robot must obey the orders given to it by human beings, 
            except where such orders would conflict with the First Law.''',
        string3='''A robot must protect its own existence 
            as long as such protection does not conflict 
            with the First or Second Law.''')
    print(the_three_laws)
