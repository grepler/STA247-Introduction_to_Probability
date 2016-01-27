from random import randint


def roll_triples(n, sides):
    """
    Return a list of n triples, each value in triple a random integer
    from 1 to sides.

    :param n: int
    :type n: int
    :param sides:  int
    :type sides: int
    :return: list
    :rtype: list
    """

    lst = []

    for i in range(1, n):
        lst.append((randint(1, 6), randint(1, 6), randint(1, 6)))

    return lst

def count_sums(rolls):
    """
    Return a dictionary of sums and their counts.


    :param rolls:
    :type rolls:
    :return: dict
    :rtype: dict
    """
    counts = {}
    for triple in rolls:
        s = sum(triple)
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1

    return counts


rolls = roll_triples(200,6)