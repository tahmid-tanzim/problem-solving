def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        t = string[i: i + k]
        u = ""
        for j in range(0, k):
            if t[j] not in u:
                u += t[j]
        print(u)
        i += k


if __name__ == '__main__':
    merge_the_tools('AABCAAADA', 3)
