def min_jumps(arr, n):
    # code here
    start = 0
    jump = 0

    if n == 1:
        return jump
    while start <= n - 1:

        if arr[start] == 0:
            return -1
        maxi = -99999999

        # if arr[start] + start  == n-1:
        #     return jump

        if arr[start] + start >= n - 1:
            return jump + 1

        for curr in range(start + 1, arr[start] + start + 1):
            if arr[curr] + curr > maxi:
                maxi = arr[curr] + curr
                start = curr
        # print(start)
        jump += 1
    return -1


print(min_jumps([1, 4, 3, 2, 6, 7], 6))
