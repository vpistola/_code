def part(xs):  # generate all partitions of xs
    xs = tuple(xs)
    n = len(xs)
    def extend(i):
        if i == n:
            yield ()
            return
        this = xs[i]
        for o in extend(i+1):
            yield ((this,),) + o
            for j, p in enumerate(o):
                yield o[:j] + ((this,) + p,) + o[j+1:]
    for o in extend(0):
        yield o

def upart(xs):  # weed out dups, and partitions with a piece bigger than 2
    from collections import Counter
    seen = []
    for p in part(xs):
        if all(len(chunk) <= 2 for chunk in p):
            c = Counter(p)
            if c not in seen:
                seen.append(c)
                yield p

xs = [1,1,1,1,2,2]
for o in upart(xs):
    print(o)