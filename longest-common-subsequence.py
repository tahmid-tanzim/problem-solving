#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/longest-common-subsequence/


def longest_common_subsequence(text1: str, text2: str) -> int:
    len_text1 = len(text1)
    len_text2 = len(text2)

    memoization_table = [[None for _ in range(len_text1 + 1)] for _ in range(len_text2 + 1)]

    def lcs(i, j):
        if i >= len_text1 or j >= len_text2:
            return 0
        elif memoization_table[i][j] is not None:  # Memoization
            return memoization_table[i][j]
        elif text1[i] == text2[j]:
            memoization_table[i][j] = 1 + lcs(i + 1, j + 1)
            return memoization_table[i][j]
        else:
            memoization_table[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            return memoization_table[i][j]

    return lcs(0, 0)


if __name__ == '__main__':
    print(longest_common_subsequence("abcde", "aaccee"))  # 3
    print(longest_common_subsequence("abc", "abc"))  # 3
    print(longest_common_subsequence("abc", "def"))  # 0
