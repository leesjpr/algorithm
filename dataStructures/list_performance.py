import timeit
from timeit import Timer

def concat():
    l = []
    for i in range(1000):
        l = l + [i]


def append():
    l = []
    for i in range(1000):
        l.append(i)


def comprehension():
    l = [i for i in range(1000)]


def list_range():
    l = list(range(1000))



t1 = Timer("concat()", "from __main__ import concat")
print "concat ", t1.timeit(number=1000), "milliseconds"

t2 = Timer("append()", "from __main__ import append")
print "append ", t2.timeit(number=1000), "milliseconds"

t3 = Timer("comprehension()", "from __main__ import comprehension")
print "comprehension", t3.timeit(number=1000), "milliseconds"

t4 = Timer("list_range()", "from __main__ import list_range")
print "list_range", t4.timeit(number=1000), "milliseconds"
