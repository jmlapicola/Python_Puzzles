def powerSet(set0):
    if len(set0) == 1:
        return {frozenset(set0)}
    list0 = list(set0)
    subPowerSet = powerSet(set(list0[1:]))
    pSet = set(subPowerSet)
    for s in subPowerSet:
        unfrozenset = set(s)
        unfrozenset.add(list0[0])
        pSet.add(frozenset(unfrozenset))
        pSet.add(frozenset({list0[0]}))
    return pSet

print(powerSet({0,1,2}))
