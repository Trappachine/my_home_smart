def f(*args):
    return {x[1]: x[0] for x in args}
dct = {1: 'bob', 2: 'bib'}
print(dct)
print(f(*dct.items()))
