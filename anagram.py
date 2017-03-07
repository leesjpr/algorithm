def anagram(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    if len(a_list1) != len(a_list2):
        return False

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False


    return matches


print anagram('abcde', 'edcba')


def anagram_2(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = Flase

    return still_ok


print anagram_2('apple', 'pleap')


