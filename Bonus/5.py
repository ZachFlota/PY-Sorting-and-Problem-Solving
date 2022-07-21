# Write your solution for algorithm 5 below

def pair(lst, target):
    sorted_lst = sorted(lst)
    left = 0
    right = len(sorted_lst)-1

    while left < right:
        if sorted_lst[left] + sorted_lst[right] == target:
            return(sorted_lst[left], sorted_lst[right])

        if sorted_lst[left] + sorted_lst[right] < target:
            left = left + 1
        else:
            right = right -1

    return('no pairs sum to the target')

sample_lst = [3, 7, 6, 8]
print(pair(sample_lst, 10))