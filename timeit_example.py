import timeit
import collections

def wrap_args(func, *args, **kargs):
    def wrapped():
        return func(*args, **kargs)
    return wrapped

def code_sort(s1, s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    return l1==l2

def code_hash(s1, s2):
    d1 = collections.defaultdict(int)
    d2 = collections.defaultdict(int)
    for c in s1:
        d1[c] += 1
    for c in s2:
        d2[c] += 1
    for k,v in d1.items():
        if d2[k] != v:
           return False
    return True

s1 = "xstjzkfpkggnhjzkpfjoguxvkbuopi"
s2 = "xbouipkvxugojfpkzjhnggkpfkzjts"

code_sort_w = wrap_args(code_sort, s1, s2)
code_hash_w = wrap_args(code_hash, s1, s2)

print(code_sort_w())
print(code_hash_w())

print(timeit.timeit(code_sort_w, number=1000))
print(timeit.timeit(code_hash_w, number=1000))


# The takeaway is that Hash isn't much faster! esp, small hashing input
