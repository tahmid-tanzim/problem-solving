#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/longest-common-subsequence/


def longest_common_subsequence(text1, text2):
    common_subsequence = []

    i = 0
    j = 0
    
    while i < len(text1):
        while j < len(text2):
            # if text1[i] == text2[j]:
            print('Common: ', text1[i])
            j += 1
        i += 1


if __name__ == '__main__':
    print(longest_common_subsequence("abcde", "aaccee")) # 3
    # print(longest_common_subsequence("abc", "abc")) # 3
    # print(longest_common_subsequence("abc", "def")) # 0
