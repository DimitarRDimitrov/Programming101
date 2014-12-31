def member(x, xs):
    if len(xs) == 0:
        return False

    if x == xs[0]:
        return True

    return member(x, xs[1:])


class Person():
    def __init__(self, name, uniqueid):
        self.name = name
        self.uniqueid = uniqueid

    def __eq__(self, other):
            return self.uniqueid == other.uniqueid


def main():
    p1 = Person("Ivo", 1)
    p2 = Person("Rado", 2)
    p3 = Person("Maria", 1)

    a = member(Person("", 1), [p1, p2, p3])
    return a


f = lambda x: x + 1
type(f)

f(2)


def map2(func, items):
    result = []

    for item in items:
        result.append(f(item))

    return result


def compose(f,g):
    return lambda x: f(g(x))