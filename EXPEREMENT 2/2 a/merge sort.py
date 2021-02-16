def merge_sort(l, begin, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - begin > 1:
        mid = (begin + end)//2
        merge_sort(l, begin, mid)
        merge_sort(l, mid, end)
        merge_list(l, begin, mid, end)
 
def merge_list(l, begin, mid, end):
    left = l[begin:mid]
    right = l[mid:end]
    k = begin
    i = 0
    j = 0
    while (begin + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            l[k] = left[i]
            i = i + 1
        else:
            l[k] = right[j]
            j = j + 1
        k = k + 1
    if begin + i < mid:
        while k < end:
            l[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            l[k] = right[j]
            j = j + 1
            k = k + 1
 
 
l = input('Enter the list of numbers: ').split()
l = [int(x) for x in l]
merge_sort(l, 0, len(l))
print('Sorted list: ', end='')
print(l)