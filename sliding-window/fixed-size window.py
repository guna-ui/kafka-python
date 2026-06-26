# Maximum Sum Subarray of Size K (fixed-size window)

def maxsubarry(arr,k):
    if len(arr)==0 or k==0:
        return

    end=0
    best_sum=0

    current_sum=sum(arr[:k])
    best_sum=current_sum

    for i in range(k,len(arr)):
        current_sum=current_sum + arr[i]-arr[i-k]
        best_sum=max(current_sum,best_sum)
    return best_sum




print(maxsubarry([2, 1, 5, 1, 3, 2], 3))   # Expected: 9
print(maxsubarry([2, 3, 4, 1, 5], 5))      # Expected: 15
print(maxsubarry([-1, 2, 3, -4, 5, 1], 2)) # Expected: 6