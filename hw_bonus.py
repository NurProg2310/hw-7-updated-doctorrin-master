def longest_consecutive(my_list: list[int]) -> int:
    nums = set(my_list)
    longest = 0
    for n in nums:
        if n - 1 not in nums:
            length = 1
            while n + length in nums:
                length += 1
            longest = max(longest, length)
    return longest


def find_missing(my_list: list[int]):
    if not my_list:
        return None
    n = len(my_list) + 1
    missing = n * (n + 1) // 2 - sum(my_list)
    return missing if missing != n else None


def find_duplicate(my_list: list[int]) :
    seen = set()
    for x in my_list:
        if x in seen:
            return x
        seen.add(x)
    return None


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return list(groups.values())
