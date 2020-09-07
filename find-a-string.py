def count_substring(string, sub_string):
    count = 0
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(0, l1 - l2 + 1):
        if string[i:l2+i] == sub_string:
            count += 1
    return count


print(count_substring('ABCDCDC', 'CDC'))
