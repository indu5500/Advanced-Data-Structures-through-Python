def quicksort(l, begin, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - begin > 1:
        p = partition(l, begin, end)
        quicksort(l, begin, p)
        quicksort(l, p + 1, end)
 
 
def partition(l, begin, end):
    pivot = l[begin]
    i = begin + 1
    j = end - 1
 
    while True:
        while (i <= j and l[i] <= pivot):
            i = i + 1
        while (i <= j and l[j] >= pivot):
            j = j - 1
 
        if i <= j:
            l[i], l[j] = l[j], l[i]
        else:
            l[begin], l[j] = l[j], l[begin]
            return j
 
 
l = input('Enter the list of numbers: ').split()
l = [int(x) for x in l]
quicksort(l, 0, len(l))
print('Sorted list: ', end='')
print(l)
