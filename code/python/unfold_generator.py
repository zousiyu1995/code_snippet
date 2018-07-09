from collections import Iterable


def unfold(items, ignore_types=(str, bytes)):

    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from unfold(item)
        else:
            yield item
