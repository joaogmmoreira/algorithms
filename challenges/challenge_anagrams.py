def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_i, right_i = 0, 0

    for index in range(start, end):
        if left_i >= len(left):
            string[index] = right[right_i]
            right_i = right_i + 1
        elif right_i >= len(right):
            string[index] = left[left_i]
            left_i = left_i + 1
        elif left[left_i] < right[right_i]:
            string[index] = left[left_i]
            left_i = left_i + 1
        else:
            string[index] = right[right_i]
            right_i = right_i + 1


def is_anagram(first_string, second_string):
    to_lower_first = list(first_string.lower())
    to_lower_second = list(second_string.lower())

    merge_sort(to_lower_first)
    merge_sort(to_lower_second)

    i_first = "".join(to_lower_first)
    i_second = "".join(to_lower_second)

    if not first_string or not second_string:
        return (i_first, i_second, False)

    if len(i_first) != len(i_second):
        return (i_first, i_second, False)

    for index in range(len(i_first)):
        if i_first[index] != i_second[index]:
            return (i_first, i_second, False)

    return (i_first, i_second, True)
