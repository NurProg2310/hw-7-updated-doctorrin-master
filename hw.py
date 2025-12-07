def count_unique_elements(lst):
    return len(set(lst))


def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def reverse_list(lst):
    return lst[::-1]

def max_value(lst):
    return max(lst)


def min_value(lst):
    return min(lst)


def sum_values(lst):
    return sum(lst)


def average(lst):
    return sum(lst) / len(lst) if lst else 0


def find_index(lst, value):
    for i, x in enumerate(lst):
        if x == value:
            return i
    return -1

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def count_frequency(lst, value):
    return lst.count(value)

def find_mode(lst):
    if not lst:
        return None
    freq = {}
    best_val = None
    best_count = 0
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] > best_count:
            best_count = freq[x]
            best_val = x
    return best_val


def remove_all(lst, value):
    return [x for x in lst if x != value]


def rotate_left(lst, k):
    if not lst:
        return []
    k %= len(lst)
    return lst[k:] + lst[:k]


def rotate_right(lst, k):
    if not lst:
        return []
    k %= len(lst)
    return lst[-k:] + lst[:-k]


def find_intersection(a, b):
    set_b = set(b)
    result = []
    seen = set()
    for x in a:
        if x in set_b and x not in seen:
            seen.add(x)
            result.append(x)
    return result


def find_union(a, b):
    result = []
    seen = set()
    for x in a:
        if x not in seen:
            seen.add(x)
            result.append(x)
    for x in b:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def find_difference(a, b):
    set_b = set(b)
    return [x for x in a if x not in set_b]
