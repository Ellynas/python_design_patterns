def is_singleton(factory):
    o1 = factory()
    o2 = factory()
    return o1 == o2 and o1 is o2

