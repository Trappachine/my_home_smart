def tpl_sort(bob):
    for element in bob:
        if not isinstance(element, int):
            return bob
    return tuple(sorted(bob))
print(tpl_sort((57, 12, 34, "32s")))
print(tpl_sort((11, 123, 654, 1, 2, 3)))

