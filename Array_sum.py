def subArraySum(arr, n, s):
    start = 0
    curr_sum = 0
    if s == 0:
        return [-1]
    for curr in range(n):
        curr_sum += arr[curr]

        if curr_sum > s:
            while curr_sum > s:
                curr_sum -= arr[start]
                start += 1

        if curr_sum == s:
            return start + 1, curr + 1

    return [-1]


print(subArraySum([1, 2, 3, 7, 5], 5, 12))
