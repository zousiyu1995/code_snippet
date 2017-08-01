from collections import Iterable


def unfold(items, unfolded=None, ignore_types=(str, bytes)):
    unfolded = list() if unfolded is None else unfolded

    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            unfold(item, unfolded=unfolded)
        else:
            unfolded.append(item)

    return unfolded
