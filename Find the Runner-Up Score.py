if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max1 = max(arr)
    max2 = float('-inf')
    for item in arr:
        if item > max2 and item < max1:
            max2 = item
    print max2 
    
    #Another Approach
    # arr = sorted(arr,reverse=True)
    # print arr[arr.count(arr[0])]
