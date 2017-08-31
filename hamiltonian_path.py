def psieve():
    import itertools
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step

def build_graph(n):
    primes = set()
    for p in psieve():
        if p > 2*n:
            break
        else:
            primes.add(p)

    np1 = n+1
    adj = [set() for i in range(np1)]
    for i in range(1, np1):
        for j in range(i+1, np1):
            if i+j in primes:
                adj[i].add(j)
                adj[j].add(i)
    return set(range(1, np1)), adj

def ham(nodes, adj):
    class EarlyExit(Exception):
        pass

    def inner(index):
        if index == n:
            raise EarlyExit
        avail = adj[result[index-1]] if index else nodes
        for i in sorted(avail, key=lambda j: len(adj[j])):
            # Remove vertex i from the graph.  If this isolates
            # more than 1 vertex, no path is possible.
            result[index] = i
            nodes.remove(i)
            nisolated = 0
            for j in adj[i]:
                adj[j].remove(i)
                if not adj[j]:
                    nisolated += 1
                    if nisolated > 1:
                        break
            if nisolated < 2:
                inner(index + 1)
            nodes.add(i)
            for j in adj[i]:
                adj[j].add(i)

    n = len(nodes)
    result = [None] * n
    try:
        inner(0)
    except EarlyExit:
        return result

def solve(n):
    nodes, adj = build_graph(n)
    return ham(nodes, adj)