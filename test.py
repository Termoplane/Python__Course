import functools

x = [
    ("Guido" , "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

sort_by_lastname  = functools.partial(list.sort, key = lambda x : len(" ".join(x)))
print(x)
sort_by_lastname(x)
print(x)