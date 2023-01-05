#!/usr/bin/python3
# https://leetcode.com/problems/isomorphic-strings/


def isIsomorphic(s: str, t: str) -> bool:
    n = len(s)
    s_mapper = dict()
    t_mapper = dict()
    for i in range(n):
        if (s[i] not in s_mapper and t[i] not in t_mapper) or (s[i] in s_mapper and t[i] in t_mapper and s_mapper[s[i]] == t[i] and t_mapper[t[i]] == s[i]):
            s_mapper[s[i]] = t[i]
            t_mapper[t[i]] = s[i]
        else:
            return False
    return True


if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))  # True
    print(isIsomorphic("foo", "bar"))  # False
    print(isIsomorphic("paper", "title"))  # True
    print(isIsomorphic("badc", "baba"))  # False
