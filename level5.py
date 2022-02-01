def SynchronizingTables(N: int, ids: list, salary: list) -> list:

    # check if len of arrays dosnt match
    if N != len(ids) or N != len(salary):
        return [0, 0, 0]

    # service ordered array of ids
    ids_ordered = ids.copy()
    ids_ordered.sort()

    # result salary array filled by zeros
    salary_ordered = salary.copy()
    salary_ordered.sort()

    # rebuild array salary
    for i in range(N):
        ind = ids.index(ids_ordered[i])
        salary[ind] = salary_ordered[i]

    return salary
